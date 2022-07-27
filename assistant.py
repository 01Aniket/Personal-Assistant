from assistantUI import Ui_AssistantUI
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType 
import sys  

import pyttsx3 #python text to speech
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import pyjokes
import keyboard
import time
import os
import pywhatkit as kit
import smtplib

engine = pyttsx3.init('sapi5')#API provided by windows to take voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

import wolframalpha
try:
    app=wolframalpha.Client("Y252WT-6RVG8JXPYR")
except Exception:
    print("Check your connection")


#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"Good Morning, its{tt}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon, its{tt}")   

    else:
        speak(f"Good Evening, its{tt}")  

    speak("I am Natasha. Please tell me how may I help you") 

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__() 
    def run(self):
        self.TaskExecution()



    #to convert voice into text
    def takeCommand(self):
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)    

            print("Say that again please...")  
            return "None"
        return query



    '''def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()'''

    def TaskExecution(self):
        wishMe()
        while True:
        # if 1:
            self.query = self.takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")

            elif 'open google' in self.query:
                speak("What Should I Search")
                search=self.takeCommand().lower()
                webbrowser.open(f"{search}")

            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")   


            

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in self.query:
                codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            
            elif 'weather' in self.query:
                try:
                    res=app.query(self.query)
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except:
                    speak("Check Your Connection Sir!")

            elif 'play' in self.query:
                song=self.query.replace('play','')
                speak('playing'+song)
                kit.playonyt(song)

            elif 'joke' in self.query:
                speak(pyjokes.get_joke())

            elif 'close youtube' in  self.query:
                os.system("TASKKILL /F /im msedge.exe")    
            
            elif 'pause' in self.query:
                keyboard.press('space bar')

            elif 'full screen' in self.query:
                keyboard.press('f')
            
            
            elif 'exit' in self.query:
                speak("Thanks for having me sir!")
                speak("Have a Good Day!!")
                exit()
            
            # speak("Sir! do you have any other work")


            '''
            elif 'play music' in query:
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))'''


startFunctions=MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.assistant_ui=Ui_AssistantUI()
        self.assistant_ui.setupUi(self)

        self.assistant_ui.pushButton.clicked.connect(self.startFunc)
        self.assistant_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):
        self.assistant_ui.movies_label_2=QtGui.QMovie("../../New folder/Jarvis_Gui (1).gif")
        self.assistant_ui.label_2.setMovie(self.assistant_ui.movies_label_2)
        self.assistant_ui.movies_label_2.start()


        self.assistant_ui.movies_label_3=QtGui.QMovie("../../New folder/initial.gif")
        self.assistant_ui.label_3.setMovie(self.assistant_ui.movies_label_3)
        self.assistant_ui.movies_label_3.start()



        self.assistant_ui.movies_label_4=QtGui.QMovie("../../New folder/Code_Template.gif")
        self.assistant_ui.label_4.setMovie(self.assistant_ui.movies_label_4)
        self.assistant_ui.movies_label_4.start()



        self.assistant_ui.movies_label_5=QtGui.QMovie("../../New folder/Hero_Template.gif")
        self.assistant_ui.label_5.setMovie(self.assistant_ui.movies_label_5)
        self.assistant_ui.movies_label_5.start()

        startFunctions.start()

        



App=QApplication(sys.argv) 
assistant=Gui_Start()
assistant.show()
exit(App.exec_()) 