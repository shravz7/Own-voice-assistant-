import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
#import random
import datetime
from datetime import date, time, datetime
import wikipedia

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    #command = ''
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration=1)
            print('listening...')
            voice = listener.listen(source,timeout=8,phrase_time_limit=8)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                #print(command)
        return command
    except Exception as err:
        print("Issue in read_command(): {}".format(err))
 

def run_alexa():
    command = take_command()
    print(command)
    
    if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            kt.playonyt(song)
    elif 'time' in command:
            now = datetime.now()
            current_time = time(now.hour,now.minute,now.second).strftime('%I:%M %p')
            talk('Current time is ' + current_time)
            print(current_time)
    elif 'date' in command:
            today = date.today()
            talk(today)
            print(today)
    elif 'who is' in command:
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk('According to wikipedia' + info)
    elif 'stop' in command or 'bye' in command:
            talk('See you next time')
            exit()
    else:
            talk('Please say the command again.')
    
while True:
    run_alexa()