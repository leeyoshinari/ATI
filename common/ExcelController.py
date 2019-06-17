#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import xlrd
import config as cfg
from common.logger import logger


class ExcelController(object):
	def __init__(self):
		self.path = cfg.TESTCASE_PATH

	def readExcel(self):
		excel = xlrd.open_workbook(self.path)
		sheets = excel.sheet_names()
		for sheet in sheets:
			table = excel.sheet_by_name(sheet)
			for i in range(1, table.nrows):
				if table.cell_value(i, 0):
					caseId = table.cell_value(i, 0)

					if not int(table.cell_value(i, 1)):
						logger.logger.info('用例Id {} 不执行，已跳过'.format(caseId))
						continue

					# priority = int(table.cell_value(i, 2))
					interface = table.cell_value(i, 3).strip()
					protocol = table.cell_value(i, 4)
					method = table.cell_value(i, 5)
					data = table.cell_value(i, 6)
					# expected_result = table.cell_value(i, 7)
					assertion = table.cell_value(i, 8).strip()

					yield {'caseId': caseId,
					       'interface': interface,
					       'protocol': protocol,
					       'method': method,
					       'data': data,
					       'assertion': assertion}

	def writeExcel(self):
		pass

	def __del__(self):
		pass
