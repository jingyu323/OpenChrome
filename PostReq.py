import urllib

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


'''

values = {}
values["username"] = "kevinelstri"
values["password"] = "******"
data = urllib.urlencode(values)
