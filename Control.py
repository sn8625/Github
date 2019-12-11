# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import cx_Oracle


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

		self.dics = dict(dic)

	def dataControl(self):
		dbserver = \
			self.dics['Dbuser'] + '/' + self.dics['Dbpwd'] + '@' + self.dics['Dbserver'] + ':' + \
			self.dics['Dbport'] + '/' + self.dics['Dbname']

		db = cx_Oracle.connect(dbserver)
		cursor = db.cursor()
		with open('./dbsql.txt','r',encoding='utf-8') as f:
			sql = f.read()

		cursor.execute(sql)
		db.commit()
		cursor.close()
		db.close()

	def sendMail(self):
		sender = self.dics['Sender']
		receiver = self.dics['Recevier']
		smtpserver = self.dics['Smtpserver']
		user = self.dics['MailUser']
		pwd = self.dics['MailPwd']
		subject = '顾客权益异常告警'

		msg = MIMEText('test','plain','utf-8')
		msg['Subject'] = Header(subject,'utf-8')
		msg['From'] = Header('Live Control','utf-8')
		msg['To'] = Header(';'.join(receiver.split(',')),'utf-8')

		smtp = smtplib.SMTP()
		smtp.connect(smtpserver)
		smtp.login(user=user,password=pwd)
		# smtp.sendmail(sender,receiver.split(','),msg.as_string())
		smtp.set_debuglevel(1)
		smtp.quit()

c = CustControl()
c.openConfig()
c.dataControl()
# c.sendMail()