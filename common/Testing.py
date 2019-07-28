#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import os
import json
import traceback
import config as cfg
from common.request import Request
from common.HtmlController import HtmlController
from common.ExcelController import ExcelController
from common.EmailController import sendMsg
from common.compare import compare
from common.logger import logger


class Testing(object):
	def __init__(self):
		self.is_to_excel = cfg.IS_TO_EXCEL
		self.is_email = cfg.IS_EMAIL

		self.request = Request()
		self.html = HtmlController()
		self.excel = ExcelController()

	def run(self):
		logger.logger.info('开始测试')
		try:
			for ele in self.excel.readExcel():
				response = ''
				responseTime = 0
				result = 'Failure'
				reason = ''
				flag = 0
				try:
					res = self.request.request(method=ele['method'], protocol=ele['protocol'], interface=ele['interface'], data=ele['data'], timeout=ele['timeout'])
					if res.status_code == 200:
						response = json.loads(res.content.decode())
						responseTime = int(res.elapsed.microseconds / 1000)

						if ele['key'] and ele['name']:
							self.excel.global_variable = {ele['name']: response[ele['key']]}

						if ele['assertion']:
							if ele['assertion'] in str(response):
								result = 'Success'
								reason = ''
								flag = 1

							if flag == 0:
								reason = 'Assertion failure message:text expected to contain {}'.format(ele['assertion'])

						elif ele['expectedResult']:
							flag, reason = compare().compare(json.loads(ele['expectedResult']), response)
							if flag == 0:
								result = 'Failure'
							elif flag == 1:
								result = 'Success'
								reason = ''

						else:
							result = 'Unknown'
							reason = 'Warning: Not verify the result'

					else:
						logger.logger.error(f'Response status code is {res.status_code}')
						reason = f'Response status code is {res.status_code}'
						result = 'Failure'

				except Exception as err:
					reason = err
					logger.logger.error(traceback.format_exc())

				case_result = {
					'caseId': ele['caseId'],
					'interface': ele['interface'],
					'method': ele['method'],
					'param': ele['data'] if ele['method'] == 'post' else '',
					'response': response if result != 'Success' else '',
					'responseTime': responseTime,
					'result': result,
					'reason': reason}

				self.html.all_case = case_result

				if self.is_to_excel:
					self.excel.writeExcel()

			fail_html, html_name = self.html.writeHtml()

			if self.is_email:
				mail_group = '{}.txt'.format(cfg.RECEIVER_NAME)
				with open(mail_group, 'r') as f:
					receiver = f.readline().strip()
				msg = {
					'subject': html_name,
					'smtp_server': cfg.SMTP_SERVER,
					'sender_name': cfg.SENDER_NAME,
					'sender_email': cfg.SENDER_EMAIL,
					'password': cfg.PASSWORD,
					'receiver_name': cfg.RECEIVER_NAME,
					'receiver_email': receiver,
					'fail_test': fail_html,
					'all_test': os.path.join(cfg.RESULT_PATH, html_name + '.html')}
				sendMsg(msg)

			logger.logger.info('测试完成')

		except Exception as err:
			logger.logger.error(traceback.format_exc())

	def __del__(self):
		del self.html
		del self.excel
		del self.request
