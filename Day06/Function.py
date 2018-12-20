#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""
函数的定义和使用 - 计算组合数C(7,3)
"""

# 将求阶乘的功能封装成一个函数

def factorial(n : int):
    result = 1
    for num in range(1,n + 1):
        result *= num
    return  result
print(factorial(7) // factorial(3) // factorial(4))


"""
函数的定义和使用 - 求最大公约数和最小公倍数
"""

def gcd(x,y):
    if x > y:
        (x,y) = (y,x)
    for factor in range(x,1,-1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1
def lcm(x,y):
    return  x * y // gcd(x,y)

print(gcd(15,27))
print(lcm(15,17))


"""
Python的内置函数
	- 数学相关: abs / divmod / pow / round / min / max / sum
	- 序列相关: len / range / next / filter / map / sorted / slice / reversed
	- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
	- 数据结构: dict / list / set / tuple
	- 其他函数: all / any / id / input / open / print / type
"""
def myfilter(myStr):
    return  len(myStr) == 6

# help()
print(chr(0x9a86))
print(hex(ord('裴')))
print(abs(-1.2345))
print(round(-1.2345))
print(pow(1.2345,5))
fruits = ['orange','peach','durian']
print(fruits[slice(1,3)])
fruits2 = list(filter(myfilter,fruits))
print(fruits)
print(fruits2)

"""
Python常用模块
	- 运行时服务相关模块: copy / pickle / sys / ...
	- 数学相关模块: decimal / math / random / ...
	- 字符串处理模块: codecs / re / ...
	- 文件处理相关模块: shutil / gzip / ...
	- 操作系统服务相关模块: datetime / os / time / logging / io / ...
	- 进程和线程相关模块: multiprocessing / threading / queue
	- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
	- Web编程相关模块: cgi / webbrowser
	- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...
"""

import  time
import  shutil
import  os

seconds = time.time()
print(seconds)
localTime = time.localtime(seconds)
print(localTime)
print(localTime.tm_year)
print(localTime.tm_mon)
print(localTime.tm_mday)
asctime = time.asctime(localTime)
print(asctime)
strTime = time.strftime('%Y-%m-%d %H:%M:%s',localTime)
print(strTime)
myDate = time.strptime('2018-1-1','%Y-%m-%d')
print(myDate)

shutil.copy('/Users/pxh/Documents/MyPython-100-Days/Day06/Test1.py', '/Users/pxh/Documents/MyPython-100-Days/Day06/Test2.py')
os.system('ls -1')
os.chdir('/Users/pxh')
os.system('ls -1')
# os.mkdir('test')

"""
函数的参数
	- 默认参数
	- 可变参数
	- 关键字参数
	- 命名关键字参数
"""

# 参数默认值
def f1(a,b = 5,c = 10):
    return  a + b * 2 + c * 3

print(f1(1,2,3))
print(f1(100,200))
print(f1(100))
print(f1(c = 2,b = 3, a = 1))

# 可变参数
def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(f2(1,2,3))
print(f2(1,2,3,4,5))
print(f2())

# 关键字参数
def f3(**kw):
    if 'name' in kw:
        print('欢迎你%s'% kw['name'])
    elif 'tel' in kw:
        print('你的联系电话是：%s'% kw['tel'])
    else:
        print('没找到你的个人信息')
param = {'name':'裴新华','age':'29'}
f3(**param)
f3(name = '裴新华',age = 29,tel ='12223222222')
f3(user = '裴新华',age = 29,tel = '1122122222')
f3(user = '裴新华',age = 29,mobile = '122222222')


"""
作用域问题
"""

# 局部作用域
def foo1():
    a = 5

foo1()

# 全局作用域
bb = 10

def foo2():
    print(bb)
foo2()

def foo3():
    b = 100 #局部变量
    print(b)

foo3()
print(bb)

def foo4():
    global  b
    b = 200 #全局变量
    print(b)

foo4()
print(b)