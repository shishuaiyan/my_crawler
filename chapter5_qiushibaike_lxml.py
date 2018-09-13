# -*- coding:utf-8 -*-
# __author__ = 'shishuai.yan'

import requests
from lxml import etree


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

url = 'https://www.qiushibaike.com/text/page/1/'

res = requests.get(url,headers=headers)
selector = etree.HTML(res.text)
url_lists = selector.xpath('//*div[@class="article block untagged mb15"')