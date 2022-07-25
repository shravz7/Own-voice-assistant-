import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
import datetime
import wikipedia
import pyjokes
import calendar
from datetime import date,time,datetime
import webbrowser
import site  #for exit
import random
import requests,json #to get data from api
from playsound import playsound
#import playsound as p
from plyer import notification
import time
import wolframalpha
import speedtest #for internet speedtest
import psutil   #for cpu usage
import os #for ram usage
import subprocess
import instaloader

#image to audio
from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string
import pytesseract




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
            listener.adjust_for_ambient_noise(source, duration=1)
            print('listening...')
            voice = listener.listen(source,timeout=8,phrase_time_limit=8)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'buddy' in command:
                command = command.replace('buddy', '')
                #print(command)
        return command
    except Exception as err:
        print("Issue in read_command(): {}".format(err))

def run_alexa():
    command = take_command()
    print(command)
    
    if 'play' in command:   #PJ
            song = command.replace('play', '')
            talk('playing ' + song)
            kt.playonyt(song)
    elif 'hai' in command or 'hello' in command or 'let\'s get started' in command:
            talk('Hey what can I do for you')
    elif 'who is pooja' in command:
            print("Pooja Nadiger is smart,intelligent,strong,independent and cute")
            talk("Pooja Nadiger is smart,intelligent,strong,independent and cute")
    elif 'top 10 news' in command:  #PN
            r=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=6721a0266ede408a9daffb592cec380a')
            data=json.loads(r.content)
            for i in range(10):
                News=data['articles'][i]['title']
                print("News ",i+1,":",News)
                talk(News)
    elif 'weather' in command:  #PN
            talk('Please tell the name of city')
            CITY=take_command()
            API_KEY= "a3296ddf78aa6b7a9f32ff2e6e55575d"
            talk('Enter the language in which you want the report')
            lang=take_command()
            BASE_URL = (f"https://api.openweathermap.org/data/2.5/weather?id=524901&{CITY}&lang={lang}&appid={API_KEY}")
            #URL = BASE_URL + "q=" + CITY +"&lang=" + lang +"&appid=" + API_KEY
            response = requests.get(BASE_URL)
            if response.status_code == 200:
            # getting data in the json format
                data = response.json()
            # getting the main dict block
                main = data['main']
            # getting temperature
                temperature = main['temp']
            # getting maximum temperature
                max_temperature = main['temp_max']
            # getting minimum temperature
                min_temperature = main['temp_min']
            # getting the humidity
                humidity = main['humidity']
            # getting the pressure
                pressure = main['pressure']
            # weather report
                report = data['weather']
                des=report[0]['description']
                print(f"{CITY:-^30}")
                print(f"Temperature: {temperature}")
                print(f"Minimum Temperature: {min_temperature}")
                print(f"Maximum Temperature: {max_temperature}")
                print(f"Humidity: {humidity}")
                print(f"Pressure: {pressure}")
                print(f"Weather Report:{des}")
                talk(f'Temperature is {temperature} kelvin Minimum Temperature is {min_temperature} kelvin Maximum Temperature is {max_temperature} kelvin Humidity is {humidity} percentage Pressure is {pressure}hPa and it is {des} right now')
            else:
            # showing the error message
                print("Error in the HTTP request")
    elif 'how are you' in command:  #PJ
            current_feelings = ["I'm okay.", "I'm doing well. Thank you.", "I am doing okay."]
            # selects a random choice of greetings
            greeting = random.choice(current_feelings)
            talk(greeting)
            talk("How are you")
    elif 'fine' in command or "good" in command:
            talk("It's good to know that your fine")
    elif "where is" in command: #S
            command = command.replace("where is", "")
            location = command
            talk("User asked to Locate")
            talk(location)
            webbrowser.open('https://www.google.com/maps/place/' + location)
    elif 'time' in command: #S
            ti=datetime.today().strftime("%H:%M %p")
            print(ti)
            talk(ti)
    elif 'search' in command:   #PJ
            talk('What do you want to search for')
            Search=take_command()
            kt.search(Search)
    elif 'who are you' in command or 'define yourself' in command:
            speak = '''Hello, I am Buddy. Your personal Assistant.
            I am here to make your life easier. You can command me to perform
            various tasks such as play songs tell joke set alarm etcetra'''
            talk(speak)
    elif "write a note" in command: #PG
            talk("What should i write")
            note = take_command()
            file = open('jarvis.txt', 'w')
            talk("Should i include date and time")
            snfm = take_command()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
            talk('Note added')
    elif "show note" in command:    #PG
            talk("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            talk(file.read(6))
    elif 'who is' in command:   #PG
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk('According to wikipedia' + info)
    elif 'open google' in command:  #PJ
            print("opening google...")
            talk('Opening google')
            webbrowser.open("https://google.com") 
    elif 'wish me' in command:  #S
            hour = int(datetime.now().hour)
            if hour>=0 and hour<12:
                talk("good morning sir!")
                print("good morning sir!")
            elif hour>=12 and hour<18:
                talk("good aternoon sir!")
                print("good aternoon sir!")
            else:
                talk("Good Evening sir!")
                print("good Evening sir!")
    elif 'date' in command: #S
            today = date.today()
            talk(today)
            print(today)
    elif 'question' in command: #PN
            talk('Ask your question')
            question=take_command()
            app_id = 'G5JUAG-5TRE8XAT2Q'
            # Instance of wolf ram alpha 
            # client class
            client = wolframalpha.Client(app_id)
            # Stores the response from 
            # wolf ram alpha
            res = client.query(question)
            # Includes only text from the response
            answer = next(res.results).text
            print(answer)
            talk(answer)
    elif 'next birthday' in command:    #PG
            talk('Enter your next birth date')
            birthday=input("What is your next B'day Date? (in DD/MM/YYYY) ")  
            birthdate=datetime.strptime(birthday,"%d/%m/%Y").date()
            today=date.today()  
            days=abs(birthdate-today) 
            print(days.days)
            talk('There are still '+str(days.days)+' days left for your next birthday')
    elif 'open youtube' in command: #PJ
            print("opening youtube...")
            webbrowser.open("youtube.com")
    elif 'are you single' in command or 'I love you' in command:
            talk('I am in a relationship with wifi')
    elif 'joke' in command: #PG
            talk(pyjokes.get_joke())
    elif 'show calendar' in command:    #S
            talk('Enter the year you want me to display')
            yy = int(input("Enter year: "))  
            talk('Enter the month you want me to display')
            mm = int(input("Enter month: "))  
            # display the calendar  
            print(calendar.month(yy,mm))
    elif 'set alarm' in command:    #S
            talk('Please enter the time')
            alarmHour=int(input("Enter hour: "))
            alarmMin=int(input("Enter Minutes: "))
            alarmAm=str(input("am/pm: "))
            if alarmAm == 'pm':
                alarmHour+=12
                while True:
                    if alarmHour==datetime.today().hour and alarmMin==datetime.today().minute:
                        print('Playing..')
                        playsound('E:/python_alexa/alarm.mp3')
                        break
                talk('Time up')
    elif 'set reminder' in command: #PJ
                while True:
                    notification.notify(title = "Drink Water!",
                    message="You need water to stay hydrated and maintain an adequate amount of fluid in your body.",
                    app_icon='E:/python_alexa/icon.ico',
                    timeout = 5)
                    time.sleep(20)     #60=>1 minute for 1 hour=>60*60
    elif 'internet speed' in command:
        st = speedtest.Speedtest()
        do=st.download() /(1025*1025)
        down="{:.2f}".format(do)
        up=st.upload() / (1025 * 1025)
        upload="{:.2f}".format(up)
        print(f"Your download speed: {down}Mbps")
        talk('Your download speed is'+down+'Mbps')
        print(f"Your upload speed: {upload}Mbps")
        talk('Your upload speed is' + upload+ 'Mbps')
        st.get_best_server()
        pi=st.results.ping
        print(f"Your ping is: {pi} ms")
        talk('Your ping speed is' + pi + 'ms')
    elif 'ram details' in command:
        # Calling psutil.cpu_precent() for 4 seconds
        print('The CPU usage is: ', psutil.cpu_percent(4),'%')
        #ram details(gives answers in bytes convert to megabytes)
        # Getting total size of virtual_memory (1st field)
        by1=psutil.virtual_memory()[0]
        gb1=by1/1024 / 1024 / 1024
        d1 = "{:.2f}".format(gb1)
        print('RAM total memory excluding swap:' , d1,'gb')

        # Getting available memory for processes of virtual_memory (2nd field)
        by2 = psutil.virtual_memory()[1]
        gb2 = by2 / 1024 / 1024 / 1024
        d2 = "{:.2f}".format(gb2)
        print('Available memory for processes:' , d2,'gb')

        # Getting % usage of virtual_memory ( 3rd field)
        print('RAM memory % used:', psutil.virtual_memory()[2],'%')

        # Getting the memory used of virtual_memory ( 4th field)
        by4 = psutil.virtual_memory()[3]
        gb4 = by4 / 1024 / 1024 / 1024
        d4 = "{:.2f}".format(gb4)
        print('RAM memory used:' , d4,'gb')
        # Getting memory not used at and is readily available of virtual_memory ( 3rd field)
        by5 = psutil.virtual_memory()[4]
        gb5 = by5 / 1024 / 1024 / 1024
        d5 = "{:.2f}".format(gb5)
        print('Memory not used at and is readily available:', d5,'gb')
    elif 'download instagram profile picture' in command:
        ig=instaloader.Instaloader()
        talk('Enter insta username')
        dp=input("Enter insta username: ")
        ig.download_profile(dp,profile_pic_only=True)
    elif 'convert image to audio' in command:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        loaded_image = Image.open(r'E:\python_alexa\image.jpg.png')
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        print(cleaned_text)
        sound = gTTS(cleaned_text, lang="el")
        sound.save("sound.mp3")
        playsound('sound.mp3')
        os.remove("sound.mp3")
    elif 'stop' in command or 'goodbye' in command: #PG
            talk('See you next time')
            exit()
    else:
            talk('Please say the command again.')
    



while True:
    run_alexa()
        
        