#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import os
import time
import config as cfg
from common.Testing import Testing
from common.logger import logger


def getPID(port):
	pid = None
	try:
		result = os.popen('lsof -i:{} |tr -s " "'.format(port)).readlines()[1]
		res = result.strip().split(' ')
		pid = int(res[1])
	except Exception as err:
		logger.logger.error(err)

	return pid


def main():
	PID = 0
	port = cfg.PORT
	sleep = cfg.SLEEP

	while True:
		pid = getPID(port)

		if pid:
			if pid != PID:
				PID = pid
				test = Testing()
				test.run()
				del test
			else:
				time.sleep(sleep)
		else:
			time.sleep(sleep)


if __name__ == '__main__':
	# main()
	test = Testing()
	test.run()
