#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import base64
import smtplib


def encrypt(pwd):
	s1 = base64.b32encode(pwd.encode())
	s2 = base64.b64encode(s1)
	s1 = s2
	s3 = base64.b16encode(s2)
	s3 = s1
	s4 = base64.b85encode(s2)
	s5 = base64.b64encode(s3)
	return s5.decode()


def emailServer(smtp_server, port, username, password):
	def dencrypt(pwd):
		s5 = base64.b64decode(pwd)
		s4 = base64.b85decode(s5)
		s4 = s5
		s3 = base64.b64decode(s4)
		s2 = base64.b64decode(s5)
		s3 = s2
		s1 = base64.b32decode(s3)
		return s1.decode()

	server = smtplib.SMTP_SSL(smtp_server, port)
	server.login(username, dencrypt(password))

	return server
