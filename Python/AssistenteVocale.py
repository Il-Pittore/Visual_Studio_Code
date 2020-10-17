from playsound import playsound
from random import randrange
import pyttsx3
import os
import speech_recognition as sp
import datetime
import shlex
import pyaudio

muto = ["stop", "basta", "stai zitta"]
luna = ["luna"]
arresto = ["spegniti", "alt f 4"]
time_calendar_clock = ["data e ora", "dimmi la data e l'ora"]
time_clock = ["che ore sono", "orario", "ora", "dimmi che ore sono"]
time_calendar = ["che giorno è oggi", "data", "dimmi che giorno è"]
saluti_in = ["ciao", "ciao luna", "ehi", "eccomi"]
saluti_out = ["ehi", "ciao", "sono felice che tu mi abbia salutato"]
insulto_in = ["stai zitta puttana", "stai zitta troia", "puttana", "troia", "ritardata", "aborto"]
insulto_out = ["hai ragione", "non è correttoso nei miei confronti"]

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-25)

    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sp.Recognizer()
    with sp.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
        result = ""
        try:
            result = r.recognize_google(audio, language = 'it')
            print(result)
        except Exception as e:
            print("errore")
    return result

muta = 0
while True:
    print("sono in ascolto...")
    #text_in = get_audio()
    text_in = input()
    print("sto elaborando...")
    text_in = text_in.lower()
    text_out = text_in
    if text_in != None and text_in != "":
        if text_in in saluti_in:
            ran = randrange(len(saluti_out))
            text_out = saluti_out[ran]
        elif text_in in time_clock or text_in in time_calendar or text_in in time_calendar_clock:
            data_ora = datetime.datetime.now()
            data_ora = str(data_ora)
            data_ora_split = data_ora.split()
            if text_in in time_clock:
                text_out = "sono le " + data_ora_split[1]
            elif text_in in time_calendar:
                text_out = "oggi è il " + data_ora_split[0]
            else:
                text_out = "oggi è il " + data_ora_split[0] + " e sono le " + data_ora_split[1]
        elif text_in in muto:
            text_out = "Ok a presto"
            muta = 1
            #speak(text_out)
            print(text_out)
        elif text_in in luna:
            text_out = "Dimmi"
            muta = 0
        elif text_in in arresto:
            text_out = "Mi sono spenta, ciao"
            break
        else:
            text_out = "Non conosco questo comando, scusa."
        if muta == 0:
            #speak(text_out)
            print(text_out)
            print("-----ho risposto-----")