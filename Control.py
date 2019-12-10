# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class CustControl(object):
	def __init__(self):
		self.dics = {}

	def openConfig(self):
		with open('./config.txt','r',encoding='utf-8') as f:
			dic = []
			for line in f.readlines():
				text = line.strip('\n')
				result = text.split(':')
				dic.append(result)
				print(dic)

		self.dics = dict(dic)
		print(self.dics)

c = CustControl()
c.openConfig()