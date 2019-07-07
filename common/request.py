#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import requests
import config as cfg
from common.logger import logger


class Request(object):
	def __init__(self):
		self.ip = cfg.IP
		self.port = cfg.PORT

	def get(self, protocol, interface, timeout):
		url = '{}://{}:{}{}'.format(protocol, self.ip, self.port, interface)
		res = requests.get(url=url, timeout=timeout)
		return res

	def post(self, protocol, interface, data, headers, timeout):
		url = '{}://{}:{}{}'.format(protocol, self.ip, self.port, interface)
		res = requests.post(url=url, data=data, headers=headers, timeout=timeout)
		return res

	def request(self, method, protocol, interface, data, headers=None, timeout=None):
		if timeout is None:
			timeout = cfg.TIMEOUT

		if headers is None:
			headers = cfg.HEADERS

		try:
			if method == 'get':
				res = self.get(protocol, interface, timeout)
			elif method == 'post':
				res = self.post(protocol, interface, data, headers, timeout)
			else:
				logger.logger.error('暂不支持其他请求方式')
				raise Exception('暂不支持其他请求方式')

			return res

		except Exception as err:
			logger.logger.error(err)
			raise Exception(err)

	def __del__(self):
		pass
