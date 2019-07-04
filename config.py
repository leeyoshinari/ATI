#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import os

# 日志级别
LOG_LEVEL = 'INFO'
# 超时时间
TIMEOUT = 0.5
# 检查端口是否存在间隔时间
SLEEP = 30

# ip地址和端口
IP = '127.0.0.1'
PORT = '5555'
HEADERS = {}

# 测试用例路径
TESTCASE_PATH = os.path.join(os.path.dirname(__file__), 'testCase', 'testCase.xlsx')
# 测试结果存放路径
RESULT_PATH = os.path.join(os.path.dirname(__file__), 'result')
# 日志路径
LOG_PATH = os.path.join(os.path.dirname(__file__), 'result')

# 是否将测试结果保存到excel
IS_TO_EXCEL = True
# 是否将测试结果保存成html
IS_TO_HTML = True
# 是否将测试结果上传至FastDFS
IS_TO_FDFS = True

# 测试完成后是否自动发送邮件
IS_EMAIL = True
# 邮箱配置，qq邮箱为smtp.qq.com
# 所用的发件邮箱必须开启SMTP服务
SMTP_SERVER = 'smtp.sina.com'
# 发件人
SENDER_NAME = '张三'
SENDER_EMAIL = 'zhangsan@qq.com'
# 邮箱登陆密码，经过base64编码
PASSWORD = '123456'
# 收件人，对应 baidu_all.txt 文件，该文件为邮件组。
# 为什么这样，因为可以修改邮件组成员而不用重启程序
RECEIVER_NAME = 'baidu_all'


# 每行表格背景颜色
BG_COLOR = ['FFFFFF', 'E8E8E8']
# 表格模板
HEADER = '接口自动化测试报告'
HTML = '<html><meta charset="gbk"><body>{}</body></html>'
TITLE = '<h2 align="center">{}</h2>'
TEST_TIME = '<p align="right">测试时间：{}</p>'
H3 = '<h3>{}</h3>'
SPAN = '<span style="font-size:14px; font-weight:normal">&nbsp;&nbsp;&nbsp;&nbsp;所有用例测试结果见邮件附件</span>'
OVERVIEW1 = '<p>&nbsp;&nbsp;&nbsp;&nbsp;执行用例总数：<font color="blue">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;执行用例总耗时：<font color="blue">{:.2f}</font> s</p>'
OVERVIEW2 = '<p>&nbsp;&nbsp;&nbsp;&nbsp;执行成功用例数：<font color="blue">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;执行失败用例数：<font color="red">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;成功率：<font color="red">{}%</font></p>'
TABLE = '<table width="100%" border="1" cellspacing="0" cellpadding="6" align="center">{}</table>'
TABLE_HEAD = '<tr bgcolor="#99CCFF" align="center"><th width="7%">用例ID</th><th width="12%">请求接口</th><th width="7%">请求方式</th><th width="20%">请求参数</th><th width="20%">响应值</th><th width="7%">响应时间</th><th width="7%">测试结果</th><th width="20%">失败原因</th></tr>'
TR = '<tr bgcolor="#{}">{}</tr>'
TD = '<td>{}</td>'
TD_FAIL = '<td><font color="red">Fail</font></td>'
TD_SUCCESS = '<td><font color="blue">Success</font></td>'
LAST = '<p style="color:blue">此邮件自动发出，如有疑问，请直接回复。</p>'
