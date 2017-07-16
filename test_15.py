'''
@author：KongWeiKun
@file: test_15.py
@time: 17-6-26 下午12:04
@contact: 836242657@qq.com
'''
'''
将.txt 存入到excel
'''
import  json
import xlwt
from collections import OrderedDict
with open('/home/kongweikun/PycharmProjects/leanning/train/text/student.txt') as f:
    data=json.load(f,object_hook=OrderedDict)  #编码和解码Json数据
    workbook=xlwt.Workbook()
