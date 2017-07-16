'''
@author：KongWeiKun
@file: test_12.py
@time: 17-6-21 上午11:49
@contact: 836242657@qq.com
'''
'''
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
'''
world_file=set()
with open('/home/kongweikun/PycharmProjects/leanning/train/text/sensitive_worlds.txt') as f:
    for w in f.readlines():
        world_file.add(w.strip())
while True:
    s=input()
    if s =='exit':
        break
    if s in world_file:
        print("Freedom")
    else:
        print("Human Rights")
