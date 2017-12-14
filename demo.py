#!/usr/bin/env python
# coding=utf-8

import requests
from requests.packages import urllib3

urllib3.disable_warnings()
r = requests.get('https://192.168.1.100', verify = False)

# print(r.status_code)
# print(r.text)
# print(r.content)
print(r.headers)

# with open('headers.txt', 'wb') as f:
# 	f.write(r.headers)

