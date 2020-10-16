from playsound import playsound
import pyttsx3
import os
import speech_recognition as sp
from random import randrange
import pyaudio

saluti_in = ["ciao", "ciao luna", "ehi", "eccomi"]
saluti_out = ["ehi", "ciao", "sono felice che tu mi abbia salutato"]

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-25)

    engine.say(text)
    engine.runAndWait()

#def get_audio():
#    r = sp.Recognizer()
#    with sp.Microphone() as source:
#        r.adjust_for_ambient_noise(source, duration=1)
#        audio = r.listen(source)
#        result = ""
#        try:
#            result = r.recognize_google(audio, lanhuage = 'it-IT')
#            print(result)
#        except Exception as e:
#            print("Errore")
#    return result

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


while True:
    text_in = get_audio()
    text_in = text_in.lower()
    text_out = text_in
    if text_in != None and text_in != "":
        if text_in in saluti_in:
            ran = randrange(len(saluti_out))
            text_out = saluti_out[ran]
        else:
            text_out = "Non conosco queta parola, scusa."
        speak(text_out)

#text = input()