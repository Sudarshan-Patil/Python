import sys
import os
import hasher
import time
import schedule
import urllib.request
import smtplib
import pdb
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def is_connected():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except:
        return False

def MailSender(username, password, filename, time):
    try:
        fromaddr = username
        toaddr = 'marvellousinfosystem@gmail.com '

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
            Hello %s,
            Please find the attached log file for deleted duplicate files.
            Log file created at : %s
        """%(toaddr, time)

        subject = """
            Duplicate file deleted log : %s
        """%(filename)

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

        s.login(username, password)

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)

        s.quit()

        print("Log file sent through mail")
    except Exception as E:
        print("Unable to send mail. ", E)

def removeDuplicate(path):
    isabs = os.path.isabs(path)
    filelist = {}

    if isabs == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists == False:
        print("Provided argument is not a directory. Please provide valid directory")
        exit()

    for folder, subfolders, files in os.walk(path):
        for filename in files:
            filename = os.path.join(folder, filename)
            hashcode = hasher.hash(filename)
            if hashcode in filelist:
                filelist[hashcode].append(filename)
            else:
                filelist[hashcode] = [filename]

    data = list(filter(lambda x:len(x)>1, filelist.values()))

    foldername = os.path.abspath('Marvellous')
    if (os.path.isdir(foldername) == False):
        os.mkdir('Marvellous')

    logfile = os.path.join(foldername, 'Marvellous-%s.log'%(time.strftime("%Y-%m-%d-%H-%M-%S")))

    f = open(logfile, 'w')

    for files in data:
        cnt = 0
        for filename in files:
            cnt += 1
            if (cnt > 1):
                f.write('File Deleted : %s'%filename + '\n')
                os.remove(filename)

    f.close()

    connected = is_connected()

    username = '--------------------'
    password = '--------------------'

    if connected:
        startTime = time.time()
        MailSender(username, password, logfile, time.ctime())
        endtime = time.time()

        print("Took %s second to evaluate"%(endtime-startTime))
    else:
        print("There is no internet connection")

def main():
    print("Welcome to handler")

    if (sys.argv[1] == '-h' or sys.argv[1] == '-H'):
        print("Please provide the directory name to scan and remove duplicate files.\neg. python3 directory")
        exit()

    if (sys.argv[1] == '-u' or sys.argv[1] == '-U'):
        print("This script can be use to remove duplicate files in directory")
        exit()

    if (len(sys.argv) != 3):
        print("Invalid arguments")
        exit()

    try:
        schedule.every(int(sys.argv[2])).minutes.do(removeDuplicate, path=sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)
    except:
        print("Could not remove duplicate files. Error occured")

if __name__ == "__main__":
    main()