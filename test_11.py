'''
@author：KongWeiKun
@file: test_11.py
@time: 17-6-20 下午4:38
@contact: 836242657@qq.com
'''
'''
生成图片验证码
'''
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random,string
font_path='/home/kongweikun/PycharmProjects/leanning/train/fonts/Arial.ttf'
# 获取随机的四个字母
def getrandomChar():
    return  [''.join(random.choice(string.ascii_letters)) for x in range(4)]
# 获取颜色
def getRandomColor():
    return (random.randint(30,100), random.randint(30,100),random.randint(30,100))
# 获取随机的验证码图片
def getCodePicture():
    width=240
    heigh=60
    # 创建画布
    image=Image.new('RGB',(width,heigh),(180,180,180))
    font=ImageFont.truetype(font_path,40)
    draw=ImageDraw.Draw(image)
    # 创建验证码对象
    code=getrandomChar()
    # 把验证码放置画布上
    for t in range(4):
            draw.text((60*t+10,0),code[t],font=font,fill=getRandomColor())

    #填充噪点
    for x in range(random.randint(1500,3000)):
        draw.point((random.randint(0,width),random.randint(0,heigh)),fill=getRandomColor())
        # draw.point((random.randint(0, width), random.randint(0, heigh)), fill=getRandomColor())

    #模糊处理
    image=image.filter(ImageFilter.BLUR)
    #保存名字为验证码图片
    image.save('/home/kongweikun/PycharmProjects/leanning/train/picture/code.jpg','jpeg')
if __name__=='__main__':
    getCodePicture()

