import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# Voice engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="en-IN")
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        speak("Internet connection problem.")
        return ""

def jarvis():
    speak("Hello sankit. JARVIS is ready. \n today is nice day ")
    

    while True:
        command = listen()

        if "hello" in command or "hi" in command:
            speak("Hello sankit. How can I help you?")

        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak("sankit, the time is " + time)

        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + date)

        elif "youtube" in command:
            speak("Open YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif "google" in command:
            speak("Open Google.")
            webbrowser.open("https://www.google.com")

        elif "notepad" in command:
            speak("Open Notepad.")
            os.system("notepad")

        elif "calculator" in command:
            speak("Open Calculator.")
            os.system("calc")

        elif "exit" in command or "stop" in command or "bye" in command:
            speak("Goodbye sankit.")
            break

        else:
            speak("I don't know that command yet.")

jarvis()
