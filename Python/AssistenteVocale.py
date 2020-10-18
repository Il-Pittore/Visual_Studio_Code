from playsound import playsound
from random import randrange
import pyttsx3
import os
import speech_recognition as sp
import datetime
import shlex
import pyaudio
import webbrowser

luna = ["luna"]
lista_comandi = ["lista comandi", "comandi"]
muto = ["stop", "basta", "stai zitta", "muta"]
arresto = ["spegniti", "alt f4", "spegni"]
time_calendar_clock = ["data e ora", "dimmi la data e l'ora"]
time_clock = ["che ore sono", "orario", "ora", "dimmi che ore sono"]
time_calendar = ["che giorno è oggi", "data", "dimmi che giorno è"]
calcoli = ["calcola", "fammi una'operazione"]
operazioni = ["somma", "sottrazione", "moltiplicazione", "divisione"]
cerca = ["cerca"]
saluti_in = ["ciao", "ciao luna", "ehi", "eccomi"]
saluti_out = ["ehi", "ciao", "sono felice che tu mi abbia salutato"]
insulto_in = ["stai zitta puttana", "stai zitta troia", "puttana", "troia", "ritardata", "aborto", "zoccola"]
insulto_out = ["hai ragione", "non è corretto nei miei confronti"]
stato_in = ["come stai", "come va", "come ti senti"]
stato_out = ["bene", "male", "ho bisogno di quelche aggiornamento ma nulla di grave"]

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
        result = result.lower()
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
                print("non hai inserito numeri")
            if modalita == 2 or modalita == 4:
                speak("non hai inserito numeri")
            controllo = 1
        else:
            controllo = 0
        if controllo == 0:
            break
    return operandi_split

def lista_comandi_gestione():
    lista = "Muto: "
    i = 0
    while i < len(muto):
        lista = lista + ", " + muto[i]
        i = i + 1
    lista = lista + "\nSpegnimento: "
    i = 0
    while i < len(arresto):
        lista = lista + ", " + arresto[i]
        i = i + 1
    lista = lista + "\nData e Ora: "
    i = 0
    while i < len(time_calendar_clock):
        lista = lista + ", " + time_calendar_clock[i]
        i = i + 1
    lista = lista + "\nData: "
    i = 0
    while i < len(time_calendar):
        lista = lista + ", " + time_calendar[i]
        i = i + 1
    lista = lista + "\nOra: "
    i = 0
    while i < len(time_clock):
        lista = lista + ", " + time_clock[i]
        i = i + 1
    lista = lista + "\nRichiesta di un calcolo: "
    i = 0
    while i < len(calcoli):
        lista = lista + ", " + calcoli[i]
        i = i + 1
    lista = lista + "\nRichiesta diretta di una operazione specifica: "
    i = 0
    while i < len(operazioni):
        lista = lista + ", " + operazioni[i]
        i = i + 1
    lista = lista + "\nRicerca su internet: "
    i = 0
    while i < len(cerca):
        lista = lista + ", " + cerca[i]
        i = i + 1
    lista = lista + "\nEsempi di dialoghi: "
    i = 0
    while i < len(saluti_in):
        lista = lista + ", " + saluti_in[i]
        i = i + 1
    return lista

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

def saluti():
    ran = randrange(len(saluti_out))
    text_out = saluti_out[ran]
    return text_out

def insulto():
    ran = randrange(len(insulto_out))
    text_out = insulto_out[ran]
    return text_out

def stato():
    ran = randrange(len(stato_out))
    text_out = stato_out[ran]
    return text_out

def prelievo_data_ora():
    data_ora = datetime.datetime.now()
    data_ora = str(data_ora)
    data_ora_split = data_ora.split()
    return data_ora_split

def ora(ora_split):
    ora_split = ora_split.split(':')
    text_out = "sono le ore " + ora_split[0] + " " + ora_split[1] + " minuti e " + ora_split[2] + " secondi"
    return text_out

def data(data_split):
    mesi = ["", "gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]

    data_split = data_split.split('-')
    numero_mese = int(data_split[1])
    mese = mesi[numero_mese]
    text_out = "oggi è il " + data_split[2] + " " + mese + " " + data_split[0] 
    
    return text_out

def esecuzione_operazioni(operazione):
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
        text_out = "Non conosco questa operazione, scusa"
    return text_out

def search(ricerca):
    url = "https://www.google.com/search?q=" + ricerca
    webbrowser.get().open(url)
    text_out = "ecco cosa ho trovato riguardo " + ricerca
    return text_out

def scelta_modalita():
    while True:
        modalita = input("L'assistente lo vuoi utilizzare in modalità \n 1: completamente testuale \n 2: comandi testuali ma riposta vocale \n 3: comandi vocali ma riposta testuale \n 4: completamente vocale \n Inserisci il numero della scelta che vuoi eseguire: ")
        if modalita == "1" or modalita == "2" or modalita == "3" or modalita == "4":
            modalita = int(modalita)
            break
        else:
            print("input errato")
    return modalita
        
muta = 0
text_in = None
text_out = None
modalita = scelta_modalita()
while True:
    print("sono in ascolto...")
    if modalita == 3 or modalita == 4:
        text_in = get_audio()
    if modalita == 1 or modalita == 2:
        text_in = input()
    print("sto elaborando...")
    text_out = text_in
    if text_in != None and text_in != "":
        if text_in in lista_comandi:
            text_out = lista_comandi_gestione()
        elif text_in in saluti_in:
            text_out = saluti()
        elif text_in in stato_in:
            text_out = stato()
        elif text_in in insulto_in:
            text_out = insulto()
        elif text_in in time_clock or text_in in time_calendar or text_in in time_calendar_clock:
            data_ora_split = prelievo_data_ora()
            if text_in in time_clock:
                text_out = ora(data_ora_split[1])
            elif text_in in time_calendar:
                text_out = data(data_ora_split[0])
            else:
                data = data(data_ora_split[0])
                ora = ora(data_ora_split[1])
                text_out = data + " e " + ora
        elif text_in in calcoli:
            if modalita == 2 or modalita == 4:
                speak("Che operazione vuoi fare?")
                print("sono in ascolto...")
            if modalita == 1 or modalita == 3:
                print("Che operazione vuoi fare?")
            if modalita == 3 or modalita == 4:
                operazione = get_audio()
            if modalita == 1 or modalita == 2:
                operazione = input()
            text_out = esecuzione_operazioni(operazione)
        elif text_in in operazioni:
            text_out = esecuzione_operazioni(text_in)
        elif text_in in cerca:
            if modalita == 2 or modalita == 4:
                speak("Che cosa vuoi cercare?")
                print("sono in ascolto...")
            if modalita == 1 or modalita == 3:
                print("Che cosa vuoi cercare?")
            if modalita == 3 or modalita == 4:
                ricerca = get_audio()
            if modalita == 1 or modalita == 2:
                ricerca = input()
            text_out = search(ricerca)
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
            if modalita == 2 or modalita == 4:
                speak(text_out)
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