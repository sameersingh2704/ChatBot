import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from random import randint


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

def Rand():
    return randint(1,21)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")
    elif hour>=12 and hour< 16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Friday. I am designed by Sameer, How may i help you")

def takeCommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        
        print (e)
        return "None"
    return query

if __name__ == "__main__":
    
    wishMe()
    while True:
        query=takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("www.google.com")
        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
        
        elif 'play music' in query:
            i = Rand()
            music_dir = 'D:\\Songs'
            songs= os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[i]))
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        
        elif 'play pubg' in query:
            pubg_path = 'C:\\Users\\TechAce\\Desktop\\shortcuts\\PUBGLITE'
            os.startfile(pubg_path)

        elif 'open eclipse' in query:
            elcipse_path = 'C:\\eclipse\\eclipse.exe'
            os.startfile(elcipse_path)
        
        elif 'run c m d' in query:
            cmd_path = 'C:\\WINDOWS\\system32\\cmd.exe'
            os.startfile(cmd_path)

        elif 'open visual code' in query:
            code_path = 'C:\\Users\\TechAce\\Desktop\\shortcuts\\vscode.exe'
            os.startfile(code_path)  

