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
					caseId = table.cell_value(i, 0).strip()

					if not int(table.cell_value(i, 2)):
						logger.logger.info('用例Id {} 不执行，已跳过'.format(caseId))
						continue

					caseName = table.cell_value(i, 1).strip()
					priority = int(table.cell_value(i, 3))
					interface = table.cell_value(i, 4).strip()
					protocol = table.cell_value(i, 5)
					method = table.cell_value(i, 6)
					data = table.cell_value(i, 7)
					expectedResult = table.cell_value(i, 8)
					assertion = table.cell_value(i, 9).strip()

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

	def __del__(self):
		pass
