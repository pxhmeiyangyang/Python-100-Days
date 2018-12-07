#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""
掷骰子决定做什么事情

"""

from random import randint

face = randint(1,6)
if face == 1:
    result = '跳个舞'
elif face == 2:
    result = '学狗叫'
elif face == 3:
    result = '打太极'
elif face == 4:
    result = '学鸡跳'
elif face == 5:
    result = '呱呱叫'
else:
    result = '吃口屎'
print('您投掷的结果为：',result)
