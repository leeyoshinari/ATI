#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import os

# 日志级别
LOG_LEVEL = 'DEBUG'
TIMEOUT = 1
SLEEP = 60

# ip地址和端口
IP = '127.0.0.1'
PORT = '80'
HEADERS = {}

# 测试用例路径
TESTCASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testCase', 'testCase.xlsx')
# 测试结果存放路径
RESULT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'result')
# 日志路径
LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'result')

# 是否将测试结果保存到excel
IS_TO_EXCEL = True
# 是否将测试结果保存成html
IS_TO_HTML = True
# 是否将测试结果上传至FastDFS
IS_TO_FDFS = True

# 测试完成后是否自动发送邮件
IS_EMAIL = True
# 邮箱配置
SMTP_SERVER = 'smtp.qq.com'
# 发件人
SENDER = '123456789@qq.com'
# 邮箱登陆密码
PASSWORD = '123456'
# 收件人
RECEIVER = ['123456@qq.com', '234567@qq.com']


# 每行表格背景颜色
BG_COLOR = ['FFFFFF', 'E8E8E8']
# 表格模板
HEADER = '接口自动化测试报告'
HTML = '<html><body>{}</body></html>'
TITLE = '<h2 align="center">{}</h2>'
TEST_TIME = '<p align="right">测试时间：{}</p>'
H3 = '<h3>{}</h3>'
OVERVIEW1 = '<p>&nbsp;&nbsp;&nbsp;&nbsp;执行用例总数：<font color="blue">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;执行用例总耗时：<font color="blue">{}</font> s</p>'
OVERVIEW2 = '<p>&nbsp;&nbsp;&nbsp;&nbsp;执行成功用例数：<font color="blue">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;执行失败用例数：<font color="red">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;成功率：<font color="red">{}%</font></p>'
TABILE = '<table width="100%" border="1" cellspacing="0" cellpadding="6" align="center">{}</table>'
TABLE_HEAD = '<tr bgcolor="#99CCFF" align="center"><th>用例ID</th><th>请求接口</th><th>请求方式</th><th>请求参数</th><th>响应值</th><th>响应时间</th><th>测试结果</th><th>失败原因</th></tr>'
TR = '<tr bgcolor="#{}">{}</tr>'
TD = '<td>{}</td>'
TD_FAIL = '<td><font color="red">Fail</font></td>'
TD_SUCCESS = '<td><font color="blue">Success</font></td>'
LAST = '<p style="color:blue">此邮件自动发出，如有疑问，请直接回复。</p>'
