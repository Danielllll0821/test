#!/usr/bin/env python
# coding=utf-8
import time
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

ipadd = {
	'192.168.255.1'	:	'1',
	'192.168.255.3'	:	'3',
	'192.168.255.13'	:	'220',
	'192.168.255.14'	:	'221',
	'192.168.255.5'	:	'5',
	'192.168.255.7'	:	'7',
	'192.168.255.9'	:	'9',
	'192.168.255.10'	:	'10',
	'192.168.255.15'	:	'234',
	'192.168.255.16'	:	'235',
	'192.168.9.4'		:	'438',
	'192.168.230.4'	:	'46',
	'172.16.0.1-0.3'	:	'195',
	'172.16.1.4'		:	'427',
	'172.17.1.5'		:	'428',
	'172.17.1.6'		:	'429',
	'172.17.1.7'		:	'430',
	'172.17.1.8'	:	'789',
	'192.168.1.9'		:	'788'
	}
print("开始下载：")
for ip,ipcode in ipadd.items():

	r = s.post('https://192.168.1.100/Orion/NetPerfMon/CustomChart.aspx?ChartName=HostAvgCPULoad&Title=&SubTitle=&SubTitle2=&Width=640&Height=0&SampleSize=30M&Period=LAST%207%20DAYS&ShowTrend=True&FontSize=1&NetObject=N:'+ str(ipcode), verify=False,headers=headers)

# print(r.text)
	p = re.compile(r'img src="(.+?)" /')

# image = p.findall(r.text)[0]
	image = re.findall(p, r.text)[1]
#print(image)




	ir = s.get('https://192.168.1.100'+ image)


#print(ir)
	img = ir.content
#print(ir.text)
	with open('D:/test/img/'+ str(ip) + ' - last7day.png', 'wb') as f:
		f.write(img)
	print("完成设备" + str(ip) + "的图片下载!\n")
	time.sleep(5)
print("全部下载完成！")
