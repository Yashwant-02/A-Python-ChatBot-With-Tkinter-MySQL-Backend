import pyttsx3 
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes
import os
import time
import random

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Could Not Understand ")
        # except Exception as e:
        #     return None

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == "__main__":

    #speechtx("Hello Welcome to Zeetron Network Private Limited.")

    voice_assistant_name = "alexa"
    exit_flag = False
    try:
        #while True:
        if  voice_assistant_name in sptext().lower():
            #time.sleep(1)
            speechtx("Hello My name is " + voice_assistant_name +"How may I help you")
            while True:
                    data1 =  sptext().lower()
                    # if type(data1) != None:
                    #     data1 = sptext().lower()
                    # else: 
                    #     continue

                    if "name" in data1:
                        name = "Hi!!! My name is "+voice_assistant_name
                        speechtx(name)

                    elif "how are you" in data1:
                        speechtx("I am doing great.")

                    elif "old are you" in data1:
                        age = "i am two years old"
                        speechtx(age)

                    elif "time" in data1:
                        now_time = datetime.datetime.now().strftime("%I%M%p")
                        print(now_time)
                        speechtx(now_time)
                        # continue

                    elif "youtube" in data1:
                        webbrowser.open("http://www.youtube.com/")

                    elif "google" in data1:
                        webbrowser.open("http://www.google.com/")
                    
                    elif "joke" in data1:
                        jokes_1 = pyjokes.get_joke(language='en', category='neutral')
                        print(jokes_1)
                        speechtx(jokes_1)

                    elif 'song' in data1:
                        add = 'D:\EGDownloads\Music 2020'
                        listsong = os.listdir(add)
                        print(listsong)
                        #speechtx("Ok playing "+listsong[0])
                        #os.startfile(os.path.join(add, listsong[0]))
                        os.startfile(os.path.join(add, listsong[random.randint(0,10)]))
                    
                    elif "exit" in data1:
                        #exit_flag = True
                        speechtx("Thankyou and Have a nice rest of the day.")
                        break

                    else: 
                         #time.sleep(4)
                         continue
                    #time.sleep(4) # seconds to sleep/delay
            
        # else:
        #     print('I didn\'t understand.')
        #     speechtx('I didn\'t understand.')
            # if exit_flag == True:
            #     break
    except Exception as e:
        print(e)