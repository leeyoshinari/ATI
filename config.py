#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import os

# 是否在Linux上使用，0为在Windows上使用，1为在Linux上使用
IS_LINUX = 1
# 日志级别
LOG_LEVEL = 'INFO'
# 接口响应超时时间
TIMEOUT = 0.5
# 检查端口是否存在间隔时间
SLEEP = 60

# ip地址和端口
IP = '127.0.0.1'
PORT = '8888'
# 请求头
HEADERS = {}

# 定时任务设置
# 0为只执行一次，1为每隔INTERVAL(单位s)执行一次，2为每天TIMER_SET执行一次
# 在Linux和Windows上均可以设置为0，1和2仅对Linux上有效
QUERY_TYPE = 0
# 执行间隔时间，单位为秒
INTERVAL = 120
# 定时任务执行时间
TIMER_SET = '23:59:00'
# 服务重启后是否执行。如果服务重新启动，则立即执行，仅QUERY_TYPE为1或2时有效，如果QUERY_TYPE为1，INTERVAL将重新计算
IS_START = True

# 测试用例路径
TESTCASE_PATH = os.path.join(os.path.dirname(__file__), 'testCase', 'testCase.xlsx')
# 全局变量路径
GLOBAL_VARIABLES = os.path.join(os.path.dirname(__file__), 'testCase', 'globalVariables.txt')
# 测试结果存放路径
RESULT_PATH = os.path.join(os.path.dirname(__file__), 'result')
# 日志路径
LOG_PATH = os.path.join(os.path.dirname(__file__), 'result')

# 数据库相关配置
# 是否需要从数据库中获取变量，参数化接口传参
IS_DATABASE = False
# 配置使用数据库名称，MYSQL、OCACLE
DATABASE_NAME = 'MYSQL'
# MySQL数据库配置
MYSQL_IP = '127.0.0.1'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DATABASE = 'ATI'

# 是否将测试结果保存到excel
IS_TO_EXCEL = False

# 测试完成后是否自动发送邮件
IS_EMAIL = True
# 邮箱配置，qq邮箱为smtp.qq.com
# 所用的发件邮箱必须开启SMTP服务
SMTP_SERVER = 'smtp.sina.com'
# 发件人
SENDER_NAME = '张三'
SENDER_EMAIL = 'zhangsan@qq.com'
# 邮箱登陆密码，经过base64编码
PASSWORD = 'UjBWYVJFZE9RbFpIV1QwOVBUMDlQUT09'
# 收件人，对应 baidu_all.txt 文件，该文件为邮件组名。
RECEIVER_NAME = 'baidu_all'
# RECEIVER_EMAIL = 'baidu_all.txt'    多个收件人用英文逗号分隔

# 测试报告相关的html，可不用修改
# 每行表格背景颜色，白灰相间，根据用例ID计算得到
BG_COLOR = ['FFFFFF', 'E8E8E8']
# 表格模板
HEADER = '接口自动化测试报告'
HTML = '<html><meta http-equiv="Content-Type";content="text/html";charset="utf-8"><body>{}</body></html>'
TITLE = '<h2 align="center">{}</h2>'
TEST_TIME = '<p align="right">测试时间：{}</p>'
H3 = '<h3>{}</h3>'
SPAN = '<span style="font-size:14px; font-weight:normal">&nbsp;&nbsp;&nbsp;&nbsp;所有用例测试结果见邮件附件</span>'
OVERVIEW1 = '<p>&nbsp;&nbsp;&nbsp;&nbsp;用例总数：<font color="blue">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;用例执行总耗时：<font color="blue">{:.2f}</font> s</p>'
OVERVIEW2 = '<p>&nbsp;&nbsp;&nbsp;&nbsp;用例执行成功数：<font color="blue">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;用例执行失败数：<font color="red">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;成功率：<font color="red">{:.2f}%</font></p>'
TABLE = '<table width="100%" border="1" cellspacing="0" cellpadding="6" align="center">{}</table>'
TABLE_HEAD = '<tr bgcolor="#99CCFF" align="center"><th width="7%">用例ID</th><th width="12%">请求接口</th><th width="7%">请求方式</th><th width="20%">请求参数</th><th width="20%">响应值</th><th width="7%">响应时间</th><th width="7%">测试结果</th><th width="20%">失败原因</th></tr>'
TR = '<tr bgcolor="#{}">{}</tr>'
TD = '<td>{}</td>'
TD_FAIL = '<td><font color="red">Failure</font></td>'
TD_SUCCESS = '<td><font color="blue">Success</font></td>'
LAST = '<p style="color:blue">此邮件自动发出，如有疑问，请直接回复。</p>'
