#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import config as cfg


class Database(object):
	def __init__(self):
		self.variable_name = ['name', 'password']       # 变量名，和数据库查询字段顺序保持一致
		self.varibles = {}      # 存储变量
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

		sql = 'select name, password from user order by rand() limit 1;'
		cursor.execute(sql)
		res = cursor.fetchall()
		for i in range(len(res)):
			self.varibles.update({self.variable_name[i]: res[i][0]})

	def read_data_from_oracle(self):
		"""
			从Oracle数据库中读取数据
		"""
		# import cx_Oracle
		pass

	def __del__(self):
		pass
