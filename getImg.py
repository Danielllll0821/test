#!/usr/bin/env python
# coding: utf8

import re
import urllib.request


def getHtml(url):

    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImg(html):

    reg = r'content="(.+?\.jpeg)"'
    imgre = re.compile(reg)
    html = html.decode('utf-8')  # python3
    imglist = re.findall(imgre, html)
    return imglist  #返回一个list

    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpeg' % x)
        x = x + 1

html = getHtml("http://tech.ifeng.com/a/20171204/44789677_0.shtml")
print(getImg(html))
