import speech_recognition as sr
import pyttsx3
import datetime
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Hello sir, Good Morning !")
  
    elif hour>= 12 and hour<18:
        speak("Hello sir, Good Afternoon !")  
  
    else:
        speak("Hello sir, Good Evening !") 
  
    #assname =("")
    #speak("I am your Assistant")
    #speak(assname)

def help():

    speak("How can i help you, sir")

def take_command():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Voice can not be recognized.")
        return "None"

    return query

def main():
    clear = lambda: os.system('cls')

    clear()

    while True:

            query = take_command().lower()

            if 'hello jarvis' in query:
                welcome()
                help()

            elif 'the time please' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}, sir")

            elif 'turn left' in query:
                servo_write = "180"
                #arduino.write(servo_write.encode())

            elif 'turn right' in query:
                servo_write = "0"
                #arduino.write(servo_write.encode())

            elif 'off please' in query:
                speak("See you next time sir")
                break

            else:
                speak("Sorry sir, i can not recognize your voice")


if __name__ == '__main__':
    main()