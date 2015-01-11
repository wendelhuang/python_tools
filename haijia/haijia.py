#!/usr/bin/env python
#coding: utf8

import urllib2
from bs4 import BeautifulSoup, Tag
import re
import os
import requests

url = 'http://haijia.bjxueche.net'
username = '130182198908156263'
password = '0815'
header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
proxy_file = 'proxy.dat'
error_message = '当前访问人数过多，请稍后再试！'

'''
for line in open(proxy_file):
    try:
        proxy = {'http' : "http://" + line.strip()}
        response = requests.get(url, headers=header, proxies=proxy)
        soup = BeautifulSoup(response.content)
        #print soup.title
        body = response.content.strip()
        if body == error_message:
            print 'yes'
            print body
        else:
            print 'no'
            print body
    except Exception:
        print 'timeout'



#page = urllib2.urlopen(url)
#print page.read()
'''

response = requests.get(url, headers=header)
print response.content
soup = BeautifulSoup(response.content)
print soup.title
