'''
@author：KongWeiKun
@file: test_14.py
@time: 17-6-21 下午1:47
@contact: 836242657@qq.com
'''
'''
爬虫爬取图片 [http://tieba.baidu.com/p/2166231880]
'''
import os
import  requests
from  bs4 import BeautifulSoup
# url='http://tieba.baidu.com/p/2166231880'
# save_path='/home/kongweikun/PycharmProjects/leanning/train/picture'
# html=requests.get(url)
# soup=BeautifulSoup(html.text,'html.parser')
# img_urls=soup.findAll('img',bdwater='杉本有美吧,1280,860')
# for img_url in img_urls:
#     img_src=img_url['src']
#     os.path.split(img_src)
#     with open(save_path+os.path.split(img_src)[1],'wb')as f:
#         f.write(requests.get(img_src).content)
url='http://tieba.baidu.com/p/2166231880'
def get_html(url):
    r=requests.get(url)
    return r.text
def extract_images(text):
    soup=BeautifulSoup(text)
    elems=soup.find_all("img",{'class',"BDE_Image"})
    return [elem.get("src") for elem in elems if elem.get('src').find('forum')>-1]

if __name__ == '__main__':
    html=get_html(url)
    img_urls=extract_images(html)
    print('\n'.join(img_urls))
