#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import config as cfg


class Database(object):
	def __init__(self):
		self.variable_name = ['name', 'password', 'id']       # 将数据库查询的值赋给指定变量名
		self.variables = {}      # 存储变量
		if cfg.DATABASE_NAME == 'MYSQL':
			self.read_data_from_mysql()
		if cfg.DATABASE_NAME == 'ORACLE':
			self.read_data_from_oracle()

	def read_data_from_mysql(self):
		"""
			从MySQL数据库中读取数据
		"""
		import pymysql
		db = pymysql.connect(cfg.MYSQL_IP, cfg.MYSQL_USERNAME, cfg.MYSQL_PASSWORD, cfg.MYSQL_DATABASE)
		cursor = db.cursor()

		sql = 'select name, pwd from user order by rand() limit 1;'     # sql语句
		cursor.execute(sql)         # 执行sql语句
		res = cursor.fetchall()     # 获取执行结果
		self.variables.update({self.variable_name[0]: res[0][0]})   # 将数据库查询的name值，赋给name
		self.variables.update({self.variable_name[1]: res[0][1]})   # 将数据库查询的pwd值，赋给password

		cursor.close()
		db.close()

		# 其他变量的赋值可在此进行
		self.variables.update({self.variable_name[2]: 3})

	def read_data_from_oracle(self):
		"""
			从Oracle数据库中读取数据
		"""
		# import cx_Oracle
		pass

	def __del__(self):
		pass
