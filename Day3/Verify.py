#! /usr/bin/env python3
# -*- coding:utf-8 -*-

userName = input('请输入用户名：')
password = input('请输入密码：')

if userName == "admin" and password == "123456":
    print('账号密码正确')
else:
    print('请输入正确的账号密码')
