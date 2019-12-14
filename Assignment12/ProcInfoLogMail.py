import psutil
import urllib.request as urllib2
from sys import *
import time
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def processDisplay():
	listprocess=[]
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
			listprocess.append(pinfo)
		except:
			pass
	return listprocess

def is_connected():
	try:
		urllib2.urlopen('http://216.58.192.142', timeout=1)
		return True
	except:
		return False

def MailSender(filename, time):
	try:
		fromaddr = 'sudarshansp123@gmail.com'
		toaddr = 'rupeshbhagat93@gmail.com '

		msg = MIMEMultipart()

		msg['From'] = fromaddr
		msg['To'] = toaddr

		body=  """
		Hello %s,
			Please find the attached file for running process.
		Logfile is created at : %s
		"""%(toaddr, time)

		subject = """
		Process log generated at %s
		"""%(time)

		msg['Subject'] = subject

		msg.attach(MIMEText(body, 'plain'))

		attachment = open(filename, "rb")

		p = MIMEBase('aapplication', 'octet-stream')

		p.set_payload((attachment).read())

		encoders.encode_base64(p)

		p.add_header('Content-Disposition', "attachment; filename=%s"%(filename))

		msg.attach(p)

		s = smtplib.SMTP('smtp.gmail.com', 587)

		s.starttls()

		s.login('sudarshansp123@gmail.com', 'NeverBackDown@123')

		text = msg.as_string()

		s.sendmail(fromaddr, toaddr, text)

		s.quit()

		print("Log file sent through mail")
	except Exception as E:
		print("Unable to send", E)

def main():
	if (len(argv) != 2):
		print("Invalid arguments")
		exit()

	listprocess = processDisplay()

	f = open(argv[1], 'w')
	f.write("List of active processes" + '\n')

	for ele in listprocess:
		f.write('pid : ' + str(ele['pid']))
		f.write(' username : ' + str(ele['username']))
		f.write(' name : ' + str(ele['name']))
		f.write('\n')

	f.close()

	connected = is_connected()

	if connected:
		starttime = time.time()
		MailSender(argv[1], time.ctime())
		endtime = time.time()
		print("Took %s time to send mail"%(endtime-starttime))
	else:
		print("There is no internet")
if __name__ == "__main__":
	main()