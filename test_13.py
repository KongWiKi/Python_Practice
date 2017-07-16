'''
@author：KongWeiKun
@file: test_13.py
@time: 17-6-26 上午11:43
@contact: 836242657@qq.com
'''
'''
敏感词汇用*表示
'''
world_file=set()
with open('/home/kongweikun/PycharmProjects/leanning/train/text/sensitive_worlds.txt') as f:
    for w in f.readlines():
        world_file.add(w.strip())
while True:
    s=input()
    # if s in world_file:
    #     print(s.replace(s,'*'*len(s)))
    if s == 'exit':
        break         #程序判断是否退出最先判断
    for w in world_file:
        if w in s:
            s=s.replace(w,'*'*len(w))
    # if s in world_file:
    #     s.replace(s,'*'*len(s))
    print(s)


# while True:
#     s=input()
#     if s == 'exit':
#         break
#     for w in world_file:
#         if w in s:
#             s= s.replace(w,'*'*len(w))
#     print(s)