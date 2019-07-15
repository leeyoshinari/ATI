#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import re
import xlrd
import config as cfg
from common.TxtToDict import txt_dict
from common.logger import logger


class ExcelController(object):
	def __init__(self):
		self.path = cfg.TESTCASE_PATH
		self.global_variables = txt_dict()

	def readExcel(self):
		excel = xlrd.open_workbook(self.path)
		sheets = excel.sheet_names()
		for sheet in sheets:
			table = excel.sheet_by_name(sheet)
			for i in range(1, table.nrows):
				if table.cell_value(i, 0):
					caseId = table.cell_value(i, 0).strip()

					if not int(table.cell_value(i, 2)):
						logger.logger.info('用例Id {} 不执行，已跳过'.format(caseId))
						continue

					caseName = table.cell_value(i, 1).strip()
					priority = int(table.cell_value(i, 3))
					interface = table.cell_value(i, 4).strip()
					protocol = table.cell_value(i, 5)
					method = table.cell_value(i, 6)
					data = self.compile(table.cell_value(i, 7))
					expectedResult = table.cell_value(i, 8)
					assertion = table.cell_value(i, 9).strip()

					if method == 'get' and data:
						request_data = data.split(',')
						interface = interface.format(*request_data)

					yield {'caseId': caseId,
					       'caseName': caseName,
					       'priority': priority,
					       'interface': interface,
					       'protocol': protocol,
					       'method': method,
					       'data': data,
					       'expectedResult': expectedResult,
					       'assertion': assertion}

	def writeExcel(self):
		pass

	def compile(self, data):
		pattern = '#(.*?)#'
		res = re.findall(pattern, data)
		try:
			for r in res:
				data = data.replace(f'#{r}#', self.global_variables[r])
		except Exception as err:
			logger.logger.error(err)

		return data

	def __del__(self):
		pass
