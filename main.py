#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari
# nohup python main.py &

import os
import time
import config as cfg
from common.Testing import Testing
from common.logger import logger


def getPID(port):
	pid = None
	try:
		'''result = os.popen('lsof -i:{} |tr -s " "'.format(port)).readlines()[1]
		res = result.strip().split(' ')
		pid = int(res[1])'''
		result = os.popen('netstat -nlp|grep {} |tr -s " "'.format(port)).readlines()
		res = [line.strip() for line in result if str(port) in line]
		logger.logger.debug(res[0])
		p = res[0].split(' ')
		pp = p[3].split(':')[-1]
		if str(port) == pp:
			pid = p[-1].split('/')[0]
	except IndexError as err:
		logger.logger.info('Querying whether the interface is started. INFO: {}'.format(err))

	return pid


def main():
	PID = 0
	port = cfg.PORT
	sleep = cfg.SLEEP

	while True:
		pid = getPID(port)

		if pid:
			if pid != PID:
				time.sleep(5)
				PID = pid
				test = Testing()
				test.run()
				time.sleep(3)
				del test
			else:
				time.sleep(sleep)
		else:
			time.sleep(sleep)


if __name__ == '__main__':
	main()
