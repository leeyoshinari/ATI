#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import os
import traceback
import config as cfg
from common.request import Request
from common.HtmlController import HtmlController
from common.ExcelController import ExcelController
from common.EmailController import sendMsg
from common.logger import logger


class Testing(object):
	def __init__(self):
		self.is_to_excel = cfg.IS_TO_EXCEL
		self.is_to_html = cfg.IS_TO_HTML
		self.is_email = cfg.IS_EMAIL

		self.request = Request()
		self.html = HtmlController()
		self.excel = ExcelController()

	def run(self):
		try:
			for ele in self.excel.readExcel():
				response = None
				responseTime = 0
				result = 'Fail'
				reason = None
				try:
					res = self.request.request(method=ele['method'], protocol=ele['protocol'],
					                           interface=ele['interface'], data=ele['data'])
					response = res.content.decode()
					responseTime = int(res.elapsed.microseconds / 1000)

					if ele['assertion'] in response:
						result = 'Success'
					else:
						reason = ''
				except Exception as err:
					reason = err

				case_result = {'caseId': ele['caseId'],
				               'interface': ele['interface'],
				               'method': ele['method'],
				               'param': ele['data'],
				               'response': response,
				               'responseTime': responseTime,
				               'result': result,
				               'reason': reason}

				if self.is_to_html:
					self.html.all_case = case_result
					if result == 'Fail':
						self.html.fail_case = case_result

				if self.is_to_excel:
					self.excel.writeExcel()

			if self.is_to_html:
				fail_html, html_name = self.html.writeHtml()

			if self.is_email:
				msg = {'subject': html_name,
				       'smtp_server': cfg.SMTP_SERVER,
				       'sender': cfg.SENDER,
				       'password': cfg.PASSWORD,
				       'receiver': cfg.RECEIVER,
				       'fail_test': fail_html,
				       'all_test': os.path.join(cfg.RESULT_PATH, html_name + '.html')}
				sendMsg(msg)

			del self.html
			del self.excel
			del self.request

		except Exception as err:
			logger.logger.error(traceback.format_exc())
