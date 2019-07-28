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
	"""
		根据端口号查询进程号
	"""
	pid = None
	try:
		'''result = os.popen('lsof -i:{} |tr -s " "'.format(port)).readlines()[1]
		res = result.strip().split(' ')
		pid = int(res[1])'''
		result = os.popen(f'netstat -nlp|grep {port} |tr -s " "').readlines()
		res = [line.strip() for line in result if str(port) in line]
		logger.logger.debug(res[0])
		p = res[0].split(' ')
		pp = p[3].split(':')[-1]
		if str(port) == pp:
			pid = p[-1].split('/')[0]
	except IndexError as err:
		logger.logger.info(f'Querying whether the interface is started. INFO: {err}')

	return pid


def run():
	"""
		开始测试
	"""
	test = Testing()
	test.run()
	time.sleep(3)
	del test


def main():
	PID = 0
	port = cfg.PORT
	sleep = cfg.SLEEP

	if cfg.IS_LINUX:
		if cfg.QUERY_TYPE == 1:     # 如果周期性执行
			start_time = time.time()
			while True:
				if time.time() - start_time > cfg.INTERVAL:     # 如果满足时间间隔
					run()
					start_time = time.time()

				if cfg.IS_START:
					pid = getPID(port)
					if pid:
						if pid != PID:      # 如果服务重启，则立即执行
							time.sleep(5)
							PID = pid
							run()
							start_time = time.time()    # 重置周期性执行开始时间

				time.sleep(sleep)
		elif cfg.QUERY_TYPE == 2:   # 如果定时执行
			set_hour = int(cfg.TIMER_SET.split(':')[0])
			set_minute = int(cfg.TIMER_SET.split(':')[1])
			while True:
				current_hour = int(time.strftime('%H', time.localtime(time.time())))
				if current_hour - set_hour == 0:
					current_minute = int(time.strftime('%M', time.localtime(time.time())))
					if current_minute - set_minute == 0 or current_minute - set_minute == 1:    # 如果满足时、分
						run()

				if cfg.IS_START:
					pid = getPID(port)
					if pid:
						if pid != PID:      # 如果服务重启，则立即执行
							time.sleep(5)
							PID = pid
							run()

				time.sleep(sleep)

	else:
		run()


if __name__ == '__main__':
	main()
