# -*- coding:utf-8 -*-
# __author__ = 'shishuai.yan'

import requests

address = input('请输入地点： ')
par = {'address':address,'key':'cb649a25c1f81c1451adbeca73623251'}
url = 'http://restapi.amap.com/v3/geocode/geo'
res = requests.get(url,par)
print(res.text)