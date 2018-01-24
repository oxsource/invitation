#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PIL import Image,ImageDraw,ImageFont
import yaml
import sys
import json

def fill_card(target, ptarget, keys, image_path='assets/image.jpeg', fpath='assets/font.ttf', fcolor=0):
    if len(target) != len(ptarget):
        print('参数长度不一致!')
        return
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    '''绘制邀请人和范围'''
    for i in range(0,len(target)):
        key = ptarget[i]
        value = target[i]
        font = ImageFont.truetype(fpath, key['size'])
        draw.text((key['x'],key['y']),value,fill=fcolor,font=font)
        del font
    '''绘制固定模板'''
    for i in range(0,len(keys)):
        key = keys[i]
        font = ImageFont.truetype(fpath, key['size'])
        draw.text((key['x'],key['y']),key['str'],fill=fcolor,font=font)
        del font
    img.save('喜帖_%s.jpg' % target[0],'jpeg')

fixed = [
        {'x':560,'y':487,'size':32,'str':'2017'},
        {'x':675,'y':487,'size':32,'str':'2'},
        {'x':735,'y':487,'size':32,'str':'21'},
        {'x':855,'y':508,'size':32,'str':'三'},
        {'x':600,'y':622,'size':33,'str':'冯鹏'},
        {'x':600,'y':693,'size':33,'str':'王闫岩'},
        {'x':562,'y':940,'size':30,'str':'三江红饭店'},
        {'x':562,'y':995,'size':30,'str':'下午17:30'},
        {'x':562,'y':1050,'size':30,'str':'玉水金岸好声音KTV旁'},
        ]
adjust =[
        {'x':580,'y':325,'size':40},
        {'x':665,'y':780,'size':35},
        ] 

if __name__ == '__main__':
    stream = open('template.yaml', 'r')
    data = yaml.load(stream)    
    fixed[0]['str'] = str(data['year'])
    fixed[1]['str'] = str(data['month'])
    fixed[2]['str'] = str(data['day'])
    fixed[3]['str'] = str(data['week'])
    fixed[4]['str'] = str(data['groom'])
    fixed[5]['str'] = str(data['bride'])
    fixed[6]['str'] = str(data['hotel'])
    fixed[7]['str'] = str(data['time'])
    fixed[8]['str'] = str(data['address'])
    '''获取邀请客人名单'''
    stream = open("guest.json", encoding='utf-8') 
    guest = json.load(stream)
    for i in range(0,len(guest)):
        g = guest[i]
        fill_card([g['n'], g['r']],adjust,fixed)
