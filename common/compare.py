#!/usr/bin/env python
# -*- coding: utf-8 -*-


class compare(object):
	def __init__(self):
		self.flag = 1  # a flag, used to determine whether two files are same.
		self.reason = ''

	def compare(self, new_json, raw_json):
		if isinstance(new_json, dict) and isinstance(raw_json, dict):
			self.parser_dict(new_json, raw_json)
		elif isinstance(new_json, list) and isinstance(raw_json, list):
			self.parser_list(new_json, raw_json)
		else:
			self.flag = 0
			self.reason = 'Type error'

		return self.flag, self.reason

	def parser_dict(self, dict1, dict2):
		"""
		To deal the 'dict' type.
		"""
		for key, value in dict1.items():
			if key in dict2.keys():
				if isinstance(value, dict):  # dict type
					self.parser_dict(value, dict2[key])

				elif isinstance(value, list):  # list type
					self.parser_list(value, dict2[key])

				else:
					self.is_equal(value, dict2[key], key)

			else:
				self.flag = 0
				self.reason = '{} is not exist in response value'.format(key)

			if self.flag == 0:
				break

	def parser_list(self, list1, list2):
		"""
		To deal the 'list' type.
		"""
		if list2:
			for n in range(len(list1)):
				if isinstance(list1[n], dict):  # dict type
					try:
						self.parser_dict(list1[n], list2[n])
					except Exception as err:
						self.flag = 0
						self.reason = err
				else:
					self.flag = 0
					self.reason = 'Unknown error'

				if self.flag == 0:
					break

		else:
			self.is_equal(list1, list2)

	def is_equal(self, value1, value2, key=None):
		if str(value1) == str(value2):
			self.flag = 1
			self.reason = ''
		else:
			self.flag = 0
			self.reason = 'Value of "{}" is incorrect'.format(key)
