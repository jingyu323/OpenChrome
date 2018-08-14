#-*- coding:utf-8 -*-
from html.parser import HTMLParser
import urllib
import urllib.request
import sys

url = "https://www.baidu.com/"

resp=urllib.request.urlopen('http://www.baidu.com')
html=resp.read()
# print(html)


#自定义解析方式
class parseLinks(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if  name == 'href':
                    print('value =' +value)
                    print('tarttag_text() == '+self.get_starttag_text()) #获取开始标签中的内容


# html 中会有非字符串的 转换下就好 用str()转为字符串
paser = parseLinks()  #初始化解析对象
paser.feed(str(html))

#这里报错的意思就是这个语句里面含有对象为整型的数据，不能直接赋予字符串类型。

