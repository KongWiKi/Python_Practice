'''
@author：KongWeiKun
@file: test_2.py
@time: 17-6-14 上午11:44
@contact: 836242657@qq.com
'''
'''
生成激活码200个
'''
import random
a="qwertyuiop[]a\sdfghjkl;'zxcvbnm,./789+4612305"
for i in range(1,201):
    print("".join(random.sample(a,16)))


