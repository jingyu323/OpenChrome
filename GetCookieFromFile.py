#!/usr/bin/env/python
#encoding: UTF-8

from urllib import request
from urllib import parse
from http import cookiejar


cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
req= request.Request('http://www.baidu.com')
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
response = opener.open(req)
print(response.read())