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
		self.save_excel_path = cfg.EXCEL_RESULT_PATH
		self.is_email = cfg.IS_EMAIL

		self.request = Request()
		self.html = HtmlController()
		self.excel = ExcelController()

	def run(self):
		logger.logger.info('开始测试')
		try:
			for ele in self.excel.readExcel():      # 遍历所有用例
				response = ''       # 响应值
				response_time = 0    # 响应时间
				result = 'Failure'  # 测试结果，Success or Failure or Unknown
				reason = ''         # 失败原因
				flag = 0            # 测试结果标识
				try:
					res = self.request.request(
						method=ele['method'], protocol=ele['protocol'], interface=ele['interface'],
						data=ele['data'], headers=ele['header'], timeout=ele['timeout'], files=ele['files'])

					if res.status_code == 200:      # 如果响应状态码为200
						response = json.loads(res.content.decode())
						response_time = int(res.elapsed.microseconds / 1000)

						if ele['name']:      # 如果需要从接口响应值中获取结果保存到变量中
							self.excel.global_variable = {ele['name']: self.parse_response(response, ele['key'])}  # 更新全局变量

						if ele['assertion']:        # 如果响应断言不为空
							if ele['assertion'] in str(response):       # 如果断言成功
								result = 'Success'
								reason = ''
								flag = 1

							if flag == 0:   # 断言失败
								reason = f"Assertion failure: text expected to contain {ele['assertion']}"

						elif ele['expectedResult']:     # 如果响应断言为空，期望结果不为空
							flag, reason = compare().compare(json.loads(ele['expectedResult']), response)   # 逐层逐个比较响应结果
							if flag == 0:
								result = 'Failure'
							elif flag == 1:
								result = 'Success'
								reason = ''

						else:       # 如果响应断言为空，且期望结果为空
							result = 'Unknown'
							reason = 'Warning: Not verify the result'

					else:       # 如果响应状态码不为200
						reason = f'Response status code is {res.status_code}'
						result = 'Failure'

				except Exception as err:
					reason = err
					logger.logger.error(traceback.format_exc())

				# 组装测试结果
				case_result = {
					'caseId': ele['caseId'],
					'interface': ele['interface'],
					'method': ele['method'],
					'param': ele['data'] if ele['method'] == 'post' else '',
					'response': response if result != 'Success' else '',
					'responseTime': response_time,
					'result': result,
					'reason': reason}

				self.html.all_case = case_result    # 将测试结果组装成html

				if self.is_to_excel:    # 将测试结果写到excel
					self.excel.writeExcel({
						'caseId': ele['caseId'],
						'sheet': ele['sheet'],
						'nrow': ele['nrow'],
						'result': result,
						'reason': reason})

			fail_html, html_name = self.html.writeHtml()    # 生成测试报告

			if self.is_to_excel:
				self.excel.saveExcel(os.path.join(self.save_excel_path, html_name + '.xls'))      # 保存excel

			if self.is_email:   # 发送邮件
				mail_group = '{}.txt'.format(cfg.RECEIVER_NAME)
				with open(mail_group, 'r') as f:
					receiver = f.readline().strip()
				# 组装邮件体
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
				sendMsg(msg)    # 发送邮件

			logger.logger.info('测试完成')

		except Exception as err:
			logger.logger.error(traceback.format_exc())

	@staticmethod
	def parse_response(response, keys):
		"""
			从接口响应值中获取值
			根据keys的顺序，依次获取指定字段的值
		"""
		def get_value(input_dict, k):
			result = None
			if isinstance(input_dict, dict):
				result = input_dict.get(k)

			if isinstance(input_dict, list):
				result = input_dict[int(k)]

			return result

		try:
			res = None
			for key in keys:
				res = get_value(response, key)

			return res
		except Exception as err:
			logger.logger.error(err)
			raise Exception('ERROR: Get value from response!')

	def __del__(self):
		del self.html
		del self.excel
		del self.request
