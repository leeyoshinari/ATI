#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import re
import xlrd
import config as cfg
from common.TxtToDict import txt_dict
from common.DatabaseController import Database
from common.logger import logger


class ExcelController(object):
	def __init__(self):
		self.path = cfg.TESTCASE_PATH
		self.timeout = cfg.TIMEOUT
		self._global_variable = txt_dict()  # 初始化全局变量

		if cfg.IS_DATABASE:     # 如果需要从数据库中初始化变量
			self._global_variable.update(Database().variables)

	@property
	def global_variable(self):
		return self._global_variable

	@global_variable.setter
	def global_variable(self, value):
		self._global_variable.update(value)     # 更新全局变量

	def readExcel(self):
		excel = xlrd.open_workbook(self.path)   # 打开excel表格
		sheets = excel.sheet_names()        # 获取excel中所有的sheet
		for sheet in sheets:
			table = excel.sheet_by_name(sheet)      # 获取sheet中的单元格
			for i in range(1, table.nrows):     # 遍历所有非空单元格
				if table.cell_value(i, 0):      # 用例ID非空
					caseId = table.cell_value(i, 0).strip()     # 用例ID

					if not int(table.cell_value(i, 2)):
						logger.logger.info(f'用例Id {caseId} 不执行，已跳过')
						continue

					caseName = table.cell_value(i, 1).strip()
					priority = int(table.cell_value(i, 3))
					interface = table.cell_value(i, 4).strip()
					protocol = table.cell_value(i, 5)
					method = table.cell_value(i, 6)
					data = self.compile(table.cell_value(i, 7))
					key = table.cell_value(i, 8)
					name = table.cell_value(i, 9)
					timeout = table.cell_value(i, 10)
					expectedResult = table.cell_value(i, 11)
					assertion = table.cell_value(i, 12).strip()

					if '{}' in interface and data:    # 如果是url接口需要传参，且有请求参数
						request_data = data.split(',')
						interface = interface.format(*request_data)     # 直接将请求参数放到接口中

					yield {
						'caseId': caseId,
						'caseName': caseName,
						'priority': priority,
						'interface': interface,
						'protocol': protocol,
						'method': method,
						'data': data,
						'key': key,
						'name': name,
						'timeout': float(timeout) if timeout else self.timeout,     # 如果为空或0，则接口响应超时时间默认为配置文件中的值
						'expectedResult': expectedResult,
						'assertion': assertion}     # 返回接口相关的所有数据

	def writeExcel(self):
		"""
			将测试结果存在excel中
		"""
		pass

	def compile(self, data):
		pattern = '<(.*?)>'     # 如果请求参数中有变量，则需要加<>，以表明是变量
		res = re.findall(pattern, data)     # 找出所有的变量
		try:
			for r in res:
				data = data.replace(f'<{r}>', str(self._global_variable[r]))     # 将变量替换成真实值
		except Exception as err:
			logger.logger.error(err)

		return data

	def __del__(self):
		pass
