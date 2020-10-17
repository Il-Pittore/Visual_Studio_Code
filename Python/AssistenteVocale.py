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
calcoli = ["calcola", "fammi una'operazione"]
operazioni = ["somma", "sottrazione", "moltiplicazione", "divisione"]
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

def richiesta_numeri():

    #def controllo_numeri(operandi_split):
    #    errore = "-99"
    #    i = 0
    #    while i in len(operandi_split) and i != int(errore):
    #        if type(operandi_split[i]) != type(i):
    #            if modalita == 1 or modalita == 3:
    #                print("sei un coglione")
    #            if modalita == 2 or modalita == 4:
    #                speak("sei un coglione")
    #            i = int(errore)
    #            print(i)
    #    if i == int(errore):
    #        if modalita == 1 or modalita == 3:
    #            print("non hai inseriro numeri")
    #        if modalita == 2 or modalita == 4:
    #            speak("non hai inseriro numeri")
    #        return 1
    #    else:
    #        return 0

    while True:
        if modalita == 2 or modalita == 4:
            speak("dimmi i numeri")
        if modalita == 1 or modalita == 3:
            print("dimmi i numeri")
        if modalita == 3 or modalita == 4:
            operandi = get_audio()
        if modalita == 1 or modalita == 2:
            operandi = input()
        operandi_split = operandi.split()
        i = 0
        while i < len(operandi_split):
            if type(int(operandi_split[i])) != type(i):
                if modalita == 1 or modalita == 3:
                    print("sei un coglione")
                if modalita == 2 or modalita == 4:
                    speak("sei un coglione")
                    i = 0
                break
            else:
                i = i + 1
        if i == 0:
            if modalita == 1 or modalita == 3:
                print("non hai inseriro numeri")
            if modalita == 2 or modalita == 4:
                speak("non hai inseriro numeri")
            controllo = 1
        else:
            controllo = 0
        if controllo == 0:
            break
    return operandi_split

def calc_somma(operandi_split):
    i = 0
    operando_uno = 0
    while i < len(operandi_split):
        operando_due = operandi_split[i]
        operando_due = int(operando_due)
        operando_uno = operando_uno + operando_due
        i = i + 1
    text_out = "Il risultato della somma è " + str(operando_uno)
    return text_out

def calc_sottrazione(operandi_split):
    i = 1
    operando_uno = operandi_split[0]
    operando_uno = int(operando_uno)
    while i < len(operandi_split):
        operando_due = operandi_split[i]
        operando_due = int(operando_due)
        operando_uno = operando_uno - operando_due
        i = i + 1
    text_out = "Il risultato della sottrazione è " + str(operando_uno)
    return text_out

def calc_moltiplicazione(operandi_split):
    i = 0
    operando_uno = 1
    while i < len(operandi_split):
        operando_due = operandi_split[i]
        operando_due = int(operando_due)
        operando_uno = operando_uno * operando_due
        i = i + 1
    text_out = "Il risultato della moltiplicazione è " + str(operando_uno)
    return text_out

def calc_divisione(operandi_split):
    i = 1
    operando_uno = operandi_split[0]
    operando_uno = float(operando_uno)
    while i < len(operandi_split):
        operando_due = operandi_split[i]
        operando_due = float(operando_due)
        operando_uno = operando_uno / operando_due
        i = i + 1
    text_out = "Il risultato della sottrazione è " + str(operando_uno)
    return text_out

muta = 0
modalita = 0
text_in = None
text_out = None
modalita = input("L'assistente lo vuoi utilizzare in modalità \n 1: completamente testuale \n 2: comandi testuali ma riposta vocale \n 3: comandi vocali ma riposta testuale \n 4: completamente vocale \n Inserisci il numero della scelta che vuoi eseguire: ")
modalita = int(modalita)
while True:
    if modalita == 1 or modalita == 3:
        print("sono in ascolto...")
    if modalita == 3 or modalita == 4:
        text_in = get_audio()
    if modalita == 1 or modalita == 2:
        text_in = input()
    if modalita == 1  or modalita == 3:
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
        elif text_in in calcoli:
            if modalita == 2 or modalita == 4:
                speak("Che operazione vuoi fare?")
            if modalita == 1 or modalita == 3:
                print("Che operazione vuoi fare?")
            if modalita == 3 or modalita == 4:
                operazione = get_audio()
            if modalita == 1 or modalita == 2:
                operazione = input()
            if operazione == "somma":
                operandi_split = richiesta_numeri()
                text_out = calc_somma(operandi_split)
            elif operazione == "sottrazione":
                operandi_split = richiesta_numeri()
                text_out = calc_sottrazione(operandi_split)
            elif operazione == "moltiplicazione":
                operandi_split = richiesta_numeri()
                text_out = calc_moltiplicazione(operandi_split)
            elif operazione == "divisione":
                operandi_split = richiesta_numeri()
                text_out = calc_divisione(operandi_split)
            else:
                if modalita == 2 or modalita == 4:
                    ("Non conosco questa operazione, scusa")
                if modalita == 1 or modalita == 3:
                    print("Non conosco questa operazione, scusa")
        elif text_in in operazioni:
            if text_in == "somma":
                operandi_split = richiesta_numeri()
                text_out = calc_somma(operandi_split)
            elif text_in == "sottrazione":
                operandi_split = richiesta_numeri()
                text_out = calc_sottrazione(operandi_split)
            elif text_in == "moltiplicazione":
                operandi_split = richiesta_numeri()
                text_out = calc_moltiplicazione(operandi_split)
            elif text_in == "divisione":
                operandi_split = richiesta_numeri()
                text_out = calc_divisione(operandi_split)

        elif text_in in muto:
            text_out = "Ok a presto"
            muta = 1
            if modalita == 2 or modalita == 4:
                speak(text_out)
            if modalita == 1 or modalita == 3:
                print(text_out)
        elif text_in in luna:
            text_out = "Dimmi"
            muta = 0
        elif text_in in arresto:
            text_out = "Mi sono spenta, ciao"
            if modalita == 1 or modalita == 3:
                print(text_out)
            break
        else:
            text_out = "Non conosco questo comando, scusa."
        if muta == 0:
            if modalita == 2 or modalita == 4:
                speak(text_out)
            if modalita == 1 or modalita == 3:
                print(text_out)
            print("-----ho risposto-----")