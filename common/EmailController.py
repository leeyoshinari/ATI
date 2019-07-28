#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from common.PwdEncrypt import emailServer
from common.logger import logger


def sendMsg(msg):
	logger.logger.info(msg)
	message = MIMEMultipart()
	if msg['smtp_server'] == 'smtp.sina.com':   # 新浪邮箱的Header不能使用utf-8的编码方式
		message['From'] = Header(msg['sender_name'])    # 发件人名字
	else:
		message['From'] = Header(msg['sender_name'], 'utf-8')
	message['To'] = Header(msg['receiver_name'], 'utf-8')       # 收件人名字
	message['Subject'] = Header(msg['subject'], 'utf-8')        # 邮件主题

	email_text = MIMEText(msg['fail_test'], 'html', 'utf-8')
	message.attach(email_text)      # 添加邮件正文

	all_test = MIMEText(open(msg['all_test'], 'rb').read(), 'base64', 'utf-8')
	all_test['Content-Type'] = 'application/octet-stream'
	all_test['Content-Disposition'] = 'attachment; filename="All Cases Result.html"'    # 邮件附件的名字
	message.attach(all_test)        # 添加邮件附件

	try:
		# server = smtplib.SMTP_SSL(msg['smtp_server'], 465)
		# server.login(msg['sender'], msg['password'])      # 登陆邮箱
		server = emailServer(msg['smtp_server'], 465, msg['sender_email'], msg['password'])
		server.sendmail(msg['sender_email'], msg['receiver_email'].split(','), message.as_string())     # 发送邮件
		server.quit()
		logger.logger.info('邮件发送成功')
	except Exception as err:
		logger.logger.error(traceback.format_exc())
		sendMsg(msg)
