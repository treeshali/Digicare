from tkinter import *
import os
import cv2
import random
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib
import string
import psutil
import requests
import pyautogui
import time as tt
import pywhatkit
import clipboard
import pyjokes
from time import sleep
from requests import get
import speech_recognition as sr
from secrets import senderemail, epwd, to
from email.message import EmailMessage
from nltk.tokenize import word_tokenize




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoices(voice):
    voices = engine.getProperty("voices")
    if voice == "1":
        engine.setProperty("voice", voices[0].id)
    else:
        engine.setProperty("voice", voices[1].id)

    speak("voice changed succesfully ")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    speak("I am your voice Assistant")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is  ")
    speak(Time)
    print(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is  ")
    speak(date)
    speak(month)
    speak(year)
    print(date, "/", month, "/", year)


def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    speak("How can i Help you")


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        speak("say that again Please....")
        return "None"

    return query

def send_email(receiver, subject, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    ## Transport layer security (TLS)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email["From"] = senderemail
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()


def send_whatsapp_msg(phone_no, message):
    Message = message
    webbrowser.open(
        "https://web.whatsapp.com/send?phone=" + phone_no + "&text=" + Message
    )
    sleep(10)
    pyautogui.press("enter")


def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)


def covid():
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    covid_data = f'Confirmed cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'
    print(covid_data)
    speak(covid_data)


def screen_shot():
    name_img = tt.time()
    name_img = f"H:\\Ri8thik\\PYTHON\\PROJECT\\Collage\\Screen_Shot\\{name_img}.png"
    img = pyautogui.screenshot(name_img)
    img.show()


def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = "".join(s[0:passlen])
    print(newpass)
    speak(newpass)


def flip():
    speak("okey sir, flipping a coin")
    coin = ["heads", "tails"]
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = "".join(toss[0])
    speak("i fliped the coin you got" + toss)
    print(toss)


def roll():
    speak("okey sir, rolling a die for you")
    die = ["1", "2", "3", "4", "5", "6"]
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = "".join(roll[0])
    speak("i roled a die and you got " + roll)
    print(roll)


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)


def wiki():
    speak("what shoud i search in wikipedia ? ")
    word = takeCommand().lower()
    results = wikipedia.summary(word)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def thing():
            speak("welcome back ! ")
            wishMe()
            usrname()
            wakeword = "jarvis"
            while True:
                query = takeCommand().lower()
                query = word_tokenize(query)
                print(query)
                if wakeword in query:
                    if "wikipedia" in query:
                        wiki()

                    elif "voice" in query:
                        speak(
                            "ok, which voice would you prefer sir  1 for male and 2 for female"
                        )
                        voice_cmd = takeCommand().lower()
                        getvoices(voice_cmd)

                    elif "time" in query:
                        time()

                    elif "date" in query:
                        date()

                    elif "notepad" in query:
                        npath = "C:\\WINDOWS\\system32\\notepad.exe"
                        os.startfile(npath)

                    elif "cmd" in query:
                        os.system("start cmd")

                    elif "CMD" in query:
                        os.system("start cmd")

                    elif "camera" in query:
                        cap = cv2.VideoCapture(0)
                        while True:
                            ret, img = cap.read()
                            cv2.imshow("webcam", img)
                            k = cv2.waitKey(50)
                            if k == 27:
                                break
                        cap.release()
                        cv2.destroyAllWindows()

                    elif "ip" in query:
                        ip = get("https://api.ipify.org").text
                        print(ip)
                        speak(f"your ip address is :- {ip}")

                    elif "hello" in query:
                        speak("hello sir how can i help you")

                    elif "google" in query:
                        speak("What should i search for ?")
                        search = takeCommand()
                        webbrowser.open("https://www.google.com/search?q=" + search)

                    elif "stackoverflow" in query:
                        webbrowser.open("stackoverflow.com")

                    elif "music" in query:
                        music_dir = "H:\\Ri8thik\\PYTHON\\PROJECT\\Collage\\audio"
                        songs = os.listdir(music_dir)
                        print(songs)
                        os.startfile(os.path.join(music_dir, songs[0]))

                    elif "email" in query:
                        try:
                            speak("what should i say ")
                            content = takeCommand()
                            send_email(content)
                            speak("email has been send ")
                        except Exception as e:
                            print(e)
                            speak("unable to end the email")

                    elif "message" in query:
                        user_name = {"mi": "+91 8607729426", "atul": "+91 7973633885",'r':"+91 8607729426"}
                        try:
                            speak("To whome you want to send the whats app message  ?")
                            name = takeCommand().lower()
                            phone_no = user_name[name]
                            speak("What is the message ?")
                            message = takeCommand()
                            send_whatsapp_msg(phone_no, message)
                            speak("message has been send")
                        except Exception as e:
                            print(e)
                            speak("unable to send the message ")

                    elif "youtube" in query:
                        speak("what should i search for on youtube ?")
                        topic = takeCommand()
                        pywhatkit.playonyt(topic)

                    elif "weather" in query:
                        speak("tell me your city ")
                        city = takeCommand().lower()
                        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=fa46e5cb3399f5f4b1fc767ff261b1ed"
                        res = requests.get(url)
                        data = res.json()
                        weather = data["weather"][0]["main"]
                        temp = data["main"]["temp"]
                        desp = data["weather"][0]["description"]
                        temp = round((temp - 32) * 5 / 9)
                        print(weather)
                        print(temp)
                        print(desp)
                        speak(f"weather in {city} city is like")
                        speak(f"Temperatue : {temp} degree celcius")
                        speak(f"weather is {desp}")

                    elif "read" in query:
                        text2speech()

                    elif "covid" in query:
                        covid()

                    elif ("joke" or "jokes") in query:
                        j = pyjokes.get_joke()
                        print(j)
                        speak(j)

                    elif "screenshot" in query:
                        screen_shot()

                    elif "remember" in query:
                        speak("What should i remember ?")
                        data = takeCommand()
                        speak(f"you said me to remember that{data}")
                        remember = open("data.txt", "w")
                        remember.write(data)
                        remember.close()

                    elif ("do you know anything" or "anything") in query:
                        remember = open("data.txt", "r")
                        speak("you told me to remember that" + remember.read())

                    elif "password" in query:
                        passwordgen()

                    elif "flip" in query:
                        flip()

                    elif "roll" in query:
                        roll()

                    elif "cpu" in query:
                        cpu()

                    elif "offline" or "exit" in query:
                        quit()




def chatBot():
    print("Chat bot Start :------- ")
    while True:
        query=str(input(">> "))
        if "exit" in query:
            break
        
        word = query.lower()
        results = wikipedia.summary(word,sentences =5)
        med =word+" medicine"
        data = wikipedia.search(med)
        medicine = wikipedia.page(med).categories
        k=1
        
        for i in data:
            print(f" > {k} ",i)
            k+=1
            
        j=1
        print(" \n\nBrife about "+ word )
        for i in results.split(". "):
            print(f" > {j} ",i)
            j+=1
        j=1
        print("\n\n Url for reference ")
        print("\n\n "+wikipedia.page(word).url)
        
t=True

while(t):
    i = int(input("Press 1 To Start a Voice Assistant or \nPress 2 to Start a Chat-Bot\nPress 3 To Quit  "))
    if i==1:
        root = Tk()
        root.title("hello")
        root.geometry("1900x1000")

        bg = PhotoImage(file="ap.png")
        image_background = Label(root, image=bg)
        image_background.place(x=0,y=300,)

        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        mic_button = PhotoImage(file="220.png")
        main_button = Button(root, image=mic_button, command=thing, bg="white")
        main_button.place(x=800, y=600)
        root.mainloop()

    elif i==2:
        chatBot()
        
    elif i==3:
        t=False
    else:
        print("Enter valid input ")
        

# ---------------------------------------------------------------------------------------------------------------------------------
# IMAGE BUTTON


# ------------------------------------------------------------------------------------------------------------------------------------

