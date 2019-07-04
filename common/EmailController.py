#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from common.Encrypt import emailServer
from common.logger import logger


def sendMsg(msg):
	logger.logger.info(msg)
	message = MIMEMultipart()
	if msg['smtp_server'] == 'smtp.sina.com':
		message['From'] = Header(msg['sender_name'])
	else:
		message['From'] = Header(msg['sender_name'], 'utf-8')
	message['To'] = Header(msg['receiver_name'], 'utf-8')
	message['Subject'] = Header(msg['subject'], 'utf-8')

	email_text = MIMEText(msg['fail_test'], 'html', 'utf-8')
	message.attach(email_text)

	all_test = MIMEText(open(msg['all_test'], 'rb').read(), 'base64', 'utf-8')
	all_test['Content-Type'] = 'application/octet-stream'
	all_test['Content-Disposition'] = 'attachment; filename="All Cases Result.html"'
	message.attach(all_test)

	try:
		# server = smtplib.SMTP_SSL(msg['smtp_server'], 465)
		# server.login(msg['sender'], msg['password'])
		server = emailServer(msg['smtp_server'], 465, msg['sender_email'], msg['password'])
		server.sendmail(msg['sender_email'], msg['receiver_email'].split(','), message.as_string())
		server.quit()
		logger.logger.info('邮件发送成功')
	except Exception as err:
		logger.logger.error(traceback.format_exc())
		sendMsg(msg)
