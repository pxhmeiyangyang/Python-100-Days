#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""
用while循环实现1~100求和
"""

sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1
print("1~100和为：%d"%(sum))

"""
用while循环实现1~100之间的偶数求和
"""

sum2 = 0
num2 = 2
while num2 <= 100:
    sum2 += num2
    num2 += 2
print("1~100之间的偶数求和:%d"%(sum2))