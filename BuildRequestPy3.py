from urllib import request
#python3的发起请求的方式方法
requestu = request.Request("http://www.baidu.com");
#开始一个请求
res = request.urlopen(requestu)
print(res.read().decode())


# response = urllib.request.urlopen(requestu)
# print(response.read().decode())