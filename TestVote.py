'''
Created on 2012-5-16

@author: wendel
'''

import urllib
import urllib2

content=urllib.urlopen('http://www.huameizx.com/lyhmzx/Vote.asp?id=4783')
for line in content:
	result = 0
	if line.find('CYanZheng') != -1 and line.find('div') != -1:
		line = line.strip()
		line = line[line.find('ff0000'):line.find('CYanZheng')]
		line = line[8:line.find('font')-5]
		strlist = line.split(' ')
		num1 = strlist[0]
		op = strlist[1]
		num2 = strlist[2]
		print num1, op, num2
		if op == '+':
			result = int(num1) + int(num2)
		elif op == '-':
			result = int(num1) - int(num2)
		elif op == '*':
			result = int(num1) * int(num2)
		elif op == '/':
			result = int(num1) / int(num2)
		print result
		url = 'http://www.huameizx.com/lyhmzx/Vote.asp?a=a&id=4783'
		data = {'CYanZheng':str(result) , 'Submit':'%C8%B7%B6%A8%CD%B6%C6%B1'}
		param = urllib.urlencode(data)
		req = urllib2.Request(url,param)
		req.add_header('Content-Type', 'application/x-www-form-urlencoded')
		req.add_header('Referer', 'http://www.huameizx.com/lyhmzx/Vote.asp?id=4783')
		res = urllib2.urlopen(req)
		print res
content.close()
