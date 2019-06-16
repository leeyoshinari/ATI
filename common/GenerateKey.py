#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari
"""
password为你的邮箱登陆密码，输入后，运行该程序，生成加密后的密码，然后将加密后的密码赋值到config.py文件中的PASSWORD。
例如：密码为123456，加密后为UjBWYVJFZE9RbFpIV1QwOVBUMDlQUT09，config.py中的PASSWORD='UjBWYVJFZE9RbFpIV1QwOVBUMDlQUT09'
"""
from Encrypt import encrypt

password = '123456'
print(encrypt(password))
