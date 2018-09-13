# -*- coding:utf-8 -*-
# __author__ = 'shishuai.yan'

#正则表达式爬糗事百科

import requests
import re

info_lists = []
gl_counter = 0

f = open("D:\Desktop\shishuai.yan\Desktop\我的坚果云\CODE\Python\Python爬虫\my_crawler/chapter4.txt","w")
f.close()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

def judgment_sex(class_name):
    if class_name == 'manIcon':
        return '男'
    else:
        return '女'

def get_info(url):
    global gl_counter
    counter=0
    res = requests.get(url)
    sexs = re.findall('<div class="articleGender (.*?)">',res.text,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>.*?</div>',res.text,re.S)
    ids = re.findall('<h2>(.*?)</h2>',res.text,re.S)
    pages=re.findall('<span class="current" >(.*?)</span>',res.text,re.S)
    for i in range(len(ids)-1):
        pages.append(pages[0])
    for sex,content,id,page in zip(sexs,contents,ids,pages):
        counter+=1
        info = {
            "sex":judgment_sex(sex),
            'content':content,
            'id':id,
            'page':page.strip("\n"),
            'counter':counter
        }
        info_lists.append(info)
        gl_counter+=1


def main():
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i))for i in range(1,36)]
    for url in urls:
        get_info(url)
    for info_list in info_lists:
        f = open("D:\Desktop\shishuai.yan\Desktop\我的坚果云\CODE\Python\Python爬虫\my_crawler/chapter4.txt","a+")
        try:
            f.write('ID: '+info_list['id'].strip('\n')+'\n')
            f.write('Sex: '+info_list['sex'].strip('\n')+'\n')
            f.write('Content: '+info_list['content'].strip('\n')+'\n')
            f.write('Gl_counter: '+str(gl_counter)+'\t')
            f.write('Page: '+info_list['page']+'\t')
            f.write('Counter: '+str(info_list['counter'])+'\n\n')
            f.close()
        except UnicodeEncodeError:
            pass

main()



