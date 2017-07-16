'''
@author：KongWeiKun
@file: test_1.py
@time: 17-6-13 下午10:00
@contact: 836242657@qq.com
'''
'''
功能：图片右上角加数字
'''
from PIL import ImageDraw,Image,ImageColor,ImageFont
img = Image.open('/home/kongweikun/PycharmProjects/leanning/train/picture/black.jpg')
draw=ImageDraw.Draw(img)
myfont=ImageFont.truetype('/home/kongweikun/PycharmProjects/leanning/train/fonts/Arial.ttf',90)
fillcolor=ImageColor.colormap.get('red')
width,height=img.size
draw.text((width-100,0),'1',font=myfont,fill=fillcolor)
img.save('/home/kongweikun/PycharmProjects/leanning/train/picture/resul_black.jpg','jpeg')
