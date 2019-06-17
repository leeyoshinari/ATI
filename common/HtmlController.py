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
		self.start_time = time.time()
		date_time = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(self.start_time))
		test_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.start_time))
		today = date_time.split('_')[0]
		self.html = cfg.HTML
		self.name = '{}_{}'.format(cfg.HEADER, date_time)
		self.title = cfg.TITLE.format('{}_{}'.format(cfg.HEADER, today))
		self.test_time = cfg.TEST_TIME.format(test_time)
		self.overview = cfg.H3.format('概览')
		self.overview1 = cfg.OVERVIEW1 + cfg.OVERVIEW2
		self.fail = cfg.H3.format('失败用例详情')
		self.success = cfg.H3.format('测试结果详情')
		self.table = cfg.TABLE
		self.table_head = cfg.TABLE_HEAD
		self.tr = cfg.TR
		self.td = cfg.TD
		self.td_fail = cfg.TD_FAIL
		self.td_success = cfg.TD_SUCCESS
		self.bg_color = cfg.BG_COLOR
		self.last = cfg.LAST

		self._fail_case = []
		self._all_case = []

	@property
	def fail_case(self):
		return self._fail_case

	@fail_case.setter
	def fail_case(self, value):
		color = int(value['caseId'].split('_')[-1]) % 2
		caseId = self.td.format(value['caseId'])
		interface = self.td.format(value['interface'])
		method = self.td.format(value['method'])
		param = self.td.format(value['param'])
		response = self.td.format(value['response'])
		responseTime = self.td.format(value['responseTime'])
		result = self.td_fail.format(value['result'])
		reason = self.td.format(value['reason'])
		res = self.tr.format(self.bg_color[color], '{}{}{}{}{}{}{}{}'.format(caseId, interface, method, param, response,
		                                                                     responseTime, result, reason))
		self._fail_case.append(res)

	@property
	def all_case(self):
		return self._all_case

	@all_case.setter
	def all_case(self, value):
		color = int(value['caseId'].split('_')[-1]) % 2
		caseId = self.td.format(value['caseId'])
		interface = self.td.format(value['interface'])
		method = self.td.format(value['method'])
		param = self.td.format(value['param'])
		response = self.td.format(value['response'])
		responseTime = self.td.format(str(value['responseTime']) + ' ms')
		if value['result'] == 'Fail':
			result = self.td_fail.format(value['result'])
		else:
			result = self.td_success.format(value['result'])
		reason = self.td.format(value['reason'])
		res = self.tr.format(self.bg_color[color], '{}{}{}{}{}{}{}{}'.format(caseId, interface, method, param, response,
		                                                                     responseTime, result, reason))
		self._all_case.append(res)

	def writeHtml(self):
		fail_case_num = len(self._fail_case)
		all_case_num = len(self._all_case)
		success_rate = (1 - fail_case_num / all_case_num) * 100
		spend_time = time.time() - self.start_time

		fail_rows = ''.join(self._fail_case)
		all_rows = ''.join(self._all_case)

		fail_table = self.table.format('{}{}'.format(self.table_head, fail_rows))
		all_table = self.table.format('{}{}'.format(self.table_head, all_rows))

		detail = self.overview1.format(all_case_num, spend_time, all_case_num-fail_case_num, fail_case_num, success_rate)
		header = '{}{}{}{}'.format(self.title, self.test_time, self.overview, detail)

		fail_html = self.html.format('{}{}{}{}'.format(header, self.fail, fail_table, self.last))
		all_html = self.html.format('{}{}{}'.format(header, self.success, all_table))

		html_path = os.path.join(self.path, self.name + '.html')
		with open(html_path, 'w') as f:
			f.writelines(all_html)

		logger.logger.info('所有用例测试结果保存成功。')
		return fail_html, self.name

	def __del__(self):
		pass
