import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import os
import cv2
import datetime


print("Welcome to our project")
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Welcome to our Project')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
   command =""
   try:
      with sr.Microphone() as source:
        print("listening.....")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        if 'iris' in command:
            command=command.replace('iris','')
            print(command)
   except:
      pass
   return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
        print(song)
    elif 'search' in command:
        gs=" ".join(list(command.split())[1:])
        try:
            pywhatkit.search(gs)
            print("Searching...")
        except:
            print("An unknown error occurred")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%p')
        print(time)
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'send' in command:
        time1 = datetime.datetime.now().strftime('%H')
        time2 = datetime.datetime.now().strftime('%M')
        time1=int(time1)
        time2=int(time2)+2
        name=list(command.split())[1]
        msg = " ".join(list(command.split())[2:])
        dict={
            "nishanth":"+919080344966",
            "naveen": "+919629896597",
            "navin": "+919629896597",
            "raghav": "+917358286096",
            "kishore": "+917994933210",
            "mohan":"+919487047170",
            "kavinesh":"+917358747465",
            "kamines":"+917358747465",
            "karthik":"+917305783764",
            "karan":"+916374687701"
        }
        # print(time1,time2)
        # print(type(time1),type(time2))
        talk("Will send the msg to the given number in few seconds")
        message=pywhatkit.sendwhatmsg(dict[name],msg,time1,time2)
    elif 'climate' in command:
        location = input("Enter the city name: ")
        with sr.Microphone() as source:
            talk("Enter location")
            # voice1=listener.listen(source)
            # location=listener.recognize_google(voice1)
            location=location.lower()
            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+"5559eaf3500ffa540c7d1a27841305e7"
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()
        #create variables to store and display data
            temp_city = ((api_data['main']['temp']) - 273.15)
            weather_desc = api_data['weather'][0]['description']
            hmdt = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
            print ("-------------------------------------------------------------")
            print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
            print ("-------------------------------------------------------------")
            print ("Current temperature is: {:.2f} deg C".format(temp_city))
            print ("Current weather desc  :",weather_desc)
            print ("Current Humidity      :",hmdt, '%')
            print ("Current wind speed    :",wind_spd ,'kmph')
            talk("current temperature at"+location+"is".format(temp_city)+"with humidity"+hmdt+"and windspeed"+wind_spd)
    elif 'mouse' in command:
        pywhatkit.start_server()
    elif 'joke' in command:
        jk=pyjokes.get_joke()
        print(jk)
        talk(jk)
    elif 'introduce' in command:
        talk('Hi Everyone. I am iris and i was developed by many members. But now i was developed by the two coders. My Important job is I wish to help many people')

    elif 'purpose' in command:
        talk("Yes. My purpose is to help and serve people by some works. I wish to spend most of the time with people. I also be a best friend for everyone")

    elif 'thank' in command:
        talk('Dont mention it.Its my Service for everyone')
    elif 'exit yourself' in command:
        talk("Ok.Thank you for your obedience with me.")
        exit()
    elif 'camera' in command:
        cam_port = 0
        cam = cv2.VideoCapture(cam_port)
        result, image = cam.read()
        if result:
            cv2.imshow("gfg", image)
            cv2.imwrite("C:/Footer/image.png", image)
            waitKey(5000)
            destroyWindow("gfg")
        else:
	        print("No image detected. Please! try again")
    else:
        talk('Please say the command again.')

while True:
         run_alexa()






