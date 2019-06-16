#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import json
import traceback
import requests
import config as cfg
from common.logger.Logger import logger


class Request(object):
	def __init__(self):
		self.ip = cfg.IP
		self.port = cfg.PORT

	def get(self, protocol, interface, timeout):
		url = '{}://{}:{}{}'.format(protocol, self.ip, self.port, interface)
		logger.debug(url)
		res = requests.get(url=url, timeout=timeout)
		logger.debug(json.loads(res.content.decode()))
		return res

	def post(self, protocol, interface, data, headers, timeout):
		url = '{}://{}:{}{}'.format(protocol, self.ip, self.port, interface)
		logger.debug(url)
		logger.debug(data)
		res = requests.post(url=url, data=json.dumps(data), headers=headers, timeout=timeout)
		logger.debug(json.loads(res.content.decode()))
		return res

	def request(self, method, protocol, interface, data=None, headers=None, timeout=None):
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
				logger.error('暂不支持其他请求方式')
				raise Exception('暂不支持其他请求方式')

			return res

		except Exception as err:
			logger.error(err)
			raise Exception(traceback.format_exc())
