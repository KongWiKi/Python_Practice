'''
@author：KongWeiKun
@file: test_5.py
@time: 17-6-17 上午10:20
@contact: 836242657@qq.com
'''
'''
任一个英文的纯文本文件,统计其中的单词出现的个数
'''
'''
统计词频
'''
import re,collections
def get_words(file):
    with open(file) as f:
        words_box=[]
        for line in f:
            if re.match(r'[a-zA-Z0-9]',line):
                words_box.extend(line.strip().split())
    return  collections.Counter(words_box)
a=get_words('/home/kongweikun/PycharmProjects/leanning/train/text/word.txt')
print(a.most_common())