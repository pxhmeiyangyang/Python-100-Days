#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import math


radius = float(input('请输入圆的半径：'))
perimeter = math.pi * radius * 2
area = math.pi * math.pow(radius,2)

print('circle周长为：%.1f' % perimeter)
print('Circle面积为：%.1f' % area)
