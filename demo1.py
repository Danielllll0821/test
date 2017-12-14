#!/usr/bin/env python
# coding: utf8


import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
import requests


def ungzip(data):
    try:  # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data


def getXSRF(data):
    cer = re.compile('name="_xsrf" value="(.*)"', flags=0)
    strlist = cer.findall(data)
    return strlist[0]


def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': '192.168.1.100',
    #'DNT': '1'
}

url = 'https://192.168.1.100/Orion/Login.aspx?ReturnUrl=%2f'
opener = getOpener(header)
op = opener.open(url)
data = op.read()
data = ungzip(data)  # 解压
_xsrf = getXSRF(data.decode())

# url += 'login'
id = 'admin'
password = 'x19990211;'
postDict = {
    '_xsrf': _xsrf,
    'email': id,
    'password': password,
    #'rememberme': 'y'
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)

print(data.decode())