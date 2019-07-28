#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari
"""
将txt文档中的全局变量转换成字典
"""

import config as cfg


def txt_dict():
	global_variable = {}

	with open(cfg.GLOBAL_VARIABLES, 'r') as f:
		lines = f.readlines()

	for line in lines:
		res = line.strip().split(' ')
		key = res[0].strip()
		value = res[1].strip()
		global_variable.update({key: value})

	return global_variable
