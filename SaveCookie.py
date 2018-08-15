#!/usr/bin/env/python
#encoding: UTF-8


from urllib import request
from urllib import parse
from http import cookiejar


#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookiejar.MozillaCookieJar(filename)
#利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = request.build_opener(handler)
#创建一个请求，原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)

