from urllib import parse
from urllib.parse import urlencode
from urllib import request
from urllib.request import urlopen

'''
import 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *

数字(Number)类型
1.整型 int longint 为长整型
2.布尔 true false
3.浮点 float
4.复数  complex

================================
标准数据类型
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：
====================================
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）
===================================
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，
用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加

========
数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
在混合计算时，Python会把整型转换成为浮点数。

======= 字符串
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
    print(r'Ru\noob') -->> Ru\noob
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。

=====List 就是数组

list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
 
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表


1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的

======Tuple（元组）

元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

可以把字符串看作一种特殊的元组

虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。

构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

=====  set 集合

集合（set）是一个无序不重复元素的序列。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式：
parame = {value01,value02,...}
或者
set(value)

===== Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。


'''

values = {}
values["username"] = "15829779349"
values["password"] = "qq123456789"
values["lt"] = "LT-1178243-ow9Q740Ugbl6JY2vj2S4pDo923cRcf"
values["execution"] = "e10s1"
values["fkid"] = "fkid"
values["_eventId"] = "_eventId"
values["gps"] = "39.9805012,116.302993"
# data=urlencode(values)#将字典类型的请求数据转变为url编码

#https://passport.csdn.net/account/login

url = 'https://www.zhihu.com/#signin'
data = parse.urlencode(values).encode('utf-8')   # 提交类型不能为str，需要为byte类型
request = request.Request(url, data)
response = urlopen(request)

# print(response)
print(response.read().decode())
