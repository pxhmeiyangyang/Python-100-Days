#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只
"""

# 要理解程序背后的算法 穷举法

for x in range(0,20): #100元最多买20只5块的公鸡  遍历0到20
    for y in range(0,33):#100元最多买33只3元的小鸡
        z = 100 -  x -  y
        if z / 3 + 5 * x + 3 * y == 100:
            print('1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡公鸡:%d只 母鸡：%d只 小鸡%d只'%(x,y,z))

"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...
"""

a = 0
b = 1
for _ in range(20):
    (a,b) = (b,a + b)
    print(a)



"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

import random

answer = random.randint(1,100)

counter =  0

while True:
    counter += 1
    count = int(input('请猜一个数字：'))
    if count > answer:
        print('小一点')
    if count < answer:
        print('大一点')
    if count == answer:
        print('恭喜你答对了！')
        break
    if counter > 7:
        print('你的智商欠费了！')
        break

"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3
"""

for i in range(100,1000):
    low = i % 10
    mid = i // 10 % 10
    high = i // 100
    if i == low ** 3 + mid ** 3 + high ** 3:
        print(i)

"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
"""

num = int(input('请输入一个整数'))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    num2 += temp % 10
    temp //= 10
if num == num2:
    print('这是一个回文数')
else:
    print('这不是一个回文数')

"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""

import  time
import math
start = time.process_time()
for i in range(1,10000):
    sum2 = 0
    for factor in range(1,int(math.sqrt(i)) + 1):
        if num % factor == 0:
            sum2 += factor
            if factor > 1 and i / factor != factor :
                sum2 += num / factor
    if sum2 == i:
        print(i)
end = time.process_time()
print("执行时间：",(end - start),"秒")
# 通过比较上面两种不同的解决方案的执行时间 意识到优化程序的重要性

"""
输出2~99之间的素数
"""

for i in range(2,100):
    is_prise = True
    for j in range(2,int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prise = False
            break
    if is_prise:
        print("%d为素数"%(i))


"""
输出乘法口诀表(九九表)
"""

for i in range(1,10):
    for j in range(1,i + 1):
        print('%d * %d = %d'%(j,i,i * j),end = '\t')
    print()

