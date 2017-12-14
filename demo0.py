#!/usr/bin/env python
# coding=utf-8
import re
import requests
from requests.packages import urllib3

urllib3.disable_warnings()

s = requests.Session()
#s.auth = ('admin', 'x19990211;')
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': '192.168.1.100',
    }
datas = {
	'__EVENTTARGET': 'ctl00%24BodyContent%24ctl05',
	'__VIEWSTATEGENERATOR': '01070692',
	'ctl00$BodyContent$Username': 'admin',
	'ctl00$BodyContent$Password': 'x19990211;'
	}

# l = s.get('https://192.168.1.100', verify = False, headers = s.headers)

login = s.post('https://192.168.1.100/Orion/Login.aspx?sessionTimeout=yes', verify=False, data= datas, headers=headers)

# print(login.cookies)

# print(login.status_code)
# print(login.text)

# with open('yict.txt', 'wb') as f:
 	# f.write(login.content)

	

r = s.post('https://192.168.1.100/Orion/NetPerfMon/CustomChart.aspx?chartName=HostAvgCPULoad&NetObject=N:429&Period=Today', verify=False,headers=headers)

# print(r.text)
p = re.compile(r'img src="(.+?)" /')

# image = p.findall(r.text)[0]
image = re.findall(p, r.text)[1]
#print(image)




ir = s.get('https://192.168.1.100'+ image)


#print(ir)
img = ir.content
#print(ir.text)
with open('D:/test/img/logo.png', 'wb') as f:
	f.write(img)

