#!/usr/bin/env python
#_*_coding:utf-8_*_
#author:doo

#requests请求获取网页内容
import requests

cookie='aliyungf_tc=AQAAAIF+UwaRPg4A3giO2x1CyLzBo4yb; channel=baidu; Hm_lvt_52d64b8d3f6d42a2e416d59635df3f71=1516347989,1516347994,1516584038,1516584249; cookieShowLoginTip=2; sid=s%3AvgSEL5lkwvZGWnQeyF_L_vO0p7tRsjt_.FrIua8BdP0x%2FmhTAKyer2jMk%2FOeDMQy7qGb6sXk7xdk; _zg=%7B%22uuid%22%3A%20%221600b1279d96d9-005a007f61f399-5b452a1d-e1000-1600b1279da71a%22%2C%22sid%22%3A%201516591979.752%2C%22updated%22%3A%201516592109.049%2C%22info%22%3A%201516257906352%2C%22cuid%22%3A%20%22e4ab0934-9940-49db-b8ef-4ea9e8f60850%22%7D; Hm_lpvt_52d64b8d3f6d42a2e416d59635df3f71=1516592109; responseTimeline=124'
cookies={}
for line in cookie.split(';'):
    key,value=line.split('=',1)
    cookies[key]=value

headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

url='https://news.baidu.com/'
response=requests.get(url,headers=headers,cookies=cookies)

#网页源码
web_content=response.content
# print web_content

#解析网页源码方式：正则表达式，beautifulsoup,Lxml(css)
#1.正则表达式
import re
content1=re.findall('<title>(.*?)</title>',web_content)
print content1[0]

#2.BeautifulSoup
from bs4 import BeautifulSoup
soup=BeautifulSoup(web_content,'html.parser')
content2=soup.find('title')
print content2


