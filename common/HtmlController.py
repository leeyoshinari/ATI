#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import os
import time
import config as cfg
from common.logger import logger


class HtmlController(object):
	def __init__(self):
		self.path = cfg.RESULT_PATH
		self.start_time = time.time()       # 测试开始时间
		date_time = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(self.start_time))
		test_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.start_time))
		today = date_time.split('_')[0]
		self.html = cfg.HTML
		self.name = '{}_{}'.format(cfg.HEADER, date_time)       # 保存测试结果的文件名，如“接口自动化测试报告_2019-01-01_11-11-11.html”
		self.title = cfg.TITLE.format('{}_{}'.format(cfg.HEADER, today))    # 测试报告标题，如“接口自动化测试报告_2019-01-01”
		self.test_time = cfg.TEST_TIME.format(test_time)        # 测试时间
		self.overview = cfg.H3.format('概览')
		self.overview1 = cfg.OVERVIEW1 + cfg.OVERVIEW2      # 概览详情
		self.fail1 = cfg.H3.format('失败用例详情' + cfg.SPAN)     # 如果有失败的用例
		self.fail2 = cfg.H3.format(cfg.SPAN)        # 如果所有用例都成功
		self.success = cfg.H3.format('测试结果详情')      # 测试结果详情
		self.table = cfg.TABLE      # 表格
		self.table_head = cfg.TABLE_HEAD    # 表头
		self.tr = cfg.TR    # 表格中的每一行
		self.td = cfg.TD    # 每一个单元格
		self.td_fail = cfg.TD_FAIL      # 失败用例测试结果红色展示
		self.td_success = cfg.TD_SUCCESS    # 成功用例测试结果蓝色展示
		self.bg_color = cfg.BG_COLOR        # 每行表格的底色
		self.last = cfg.LAST        # 最后一句话

		self._fail_case = []
		self._all_case = []

	@property
	def all_case(self):
		return self._all_case

	@all_case.setter
	def all_case(self, value):
		color = int(value['caseId'].split('_')[-1]) % 2
		caseId = self.td.format(value['caseId'])
		casename = self.td.format(value['caseName'])
		interface = self.td.format(value['interface'])
		method = self.td.format(value['method'])
		param = self.td.format(value['param'])
		response = self.td.format(value['response'])
		responseTime = self.td.format(str(value['responseTime']) + ' ms')
		if value['result'] == 'Failure':
			result = self.td_fail.format(value['result'])
		else:
			result = self.td_success.format(value['result'])
		reason = self.td.format(value['reason'])
		# 把所有结果写到一行里
		res = self.tr.format(self.bg_color[color], '{}{}{}{}{}{}{}{}{}'.format(caseId, casename, interface, method, param, response, responseTime, result, reason))

		if value['result'] == 'Failure':    # 失败用例单独存储
			self._fail_case.append(res)

		self._all_case.append(res)

	def writeHtml(self):
		"""
			生成html测试报告
		"""
		fail_case_num = len(self._fail_case)    # 失败用例数
		all_case_num = len(self._all_case)      # 所有用例数
		success_rate = (1 - fail_case_num / all_case_num) * 100     # 计算成功率
		spend_time = time.time() - self.start_time      # 测试花费总时间

		# 把所有用例连接起来，拼成完整的表格
		fail_rows = ''.join(self._fail_case)
		all_rows = ''.join(self._all_case)

		# 失败用例表格和所有用例表格分开保存
		fail_table = self.table.format('{}{}'.format(self.table_head, fail_rows))
		all_table = self.table.format('{}{}'.format(self.table_head, all_rows))

		# 测试结果概览详情
		detail = self.overview1.format(all_case_num, spend_time, all_case_num-fail_case_num, fail_case_num, success_rate)
		# 测试报告标题
		header = '{}{}{}{}'.format(self.title, self.test_time, self.overview, detail)

		# 根据成功率决定邮件正文内容，生成失败用例测试报告
		if success_rate == 100:
			fail_html = self.html.format('{}{}{}'.format(header, self.fail2, self.last))
		else:
			fail_html = self.html.format('{}{}{}{}'.format(header, self.fail1, fail_table, self.last))

		# 生成所有用例测试报告
		all_html = self.html.format('{}{}{}'.format(header, self.success, all_table))

		# 将所有用例测试报告保存到本地
		html_path = os.path.join(self.path, self.name + '.html')
		with open(html_path, 'w') as f:
			f.writelines(all_html)

		logger.logger.info('所有用例测试结果保存成功。')
		return fail_html, self.name

	def __del__(self):
		pass
