#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""
用for循环实现1~100求和
"""

sum = 0
for i in range(101):
    sum += i
print(sum)


"""
使用for循环实现1~100之间的偶数求和
"""

sum2 = 0
for i in range(2,101,2):
    sum2 += i
print('1~100之间的偶数和为：%d'%(sum2))

"""
输入非负整数n计算n！ n!代表n的阶乘
"""

n = int(input('n = '))
result = 1
for i in range(1,n + 1):
    result *= i
print('n的阶乘为：%d'%(result))

"""
输入一个正数判断他是不是素数
"""

from math import sqrt
num = int(input('请输入一个整数：'))
end = int(sqrt(num))
is_prime = True
for i in range(2,end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数'%(num))
else:
    print('%d不是素数'%(num))

"""
输入两个正整数计算最大公约数和最小公倍数
"""
x = int(input('x = '))
y = int(input("y = "))

if x > y:
    (x,y) = (y,x)
for factor in range(x,0,-1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数：%d'%(x,y,factor))
        print('%d和%d的最大公倍数：%d' % (x, y, x * y // factor))
        break


"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""

row = int(input('请输入行数：'))
for i in range(row):
    for _ in range(i + 1):
        print('*',end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i -1:
            print(' ',end='')
        else:
            print('*',end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ',end='')
    for _ in range(2 * i + 1):
        print('*',end='')
    print()


