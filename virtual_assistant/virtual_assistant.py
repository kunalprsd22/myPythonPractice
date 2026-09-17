from calendar import calendar
from operator import truediv

import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

id1 = "com.apple.speech.synthesis.voice.Albert"
id2 = "com.apple.voice.compact.it-IT.Alice"
id3 = "com.apple.voice.compact.sv-SE.Alva"
id4 = "com.apple.voice.compact.fr-CA.Amelie"
id5 = "com.apple.voice.compact.en-GB.Daniel"
id6 = "com.apple.voice.compact.en-IN.Rishi"

# hear the microphone and return audio as text
def transfer_audio_into_text():

    # store recognizer
    r = sr.Recognizer()
    # set microphone
    with sr.Microphone() as source:
      # waiting time
      r.pause_threshold = 0.8

      # report that recorning has begun
      print("You can now speak")

      # save what you hear as audio
      audio = r.listen(source)

      try:
         # search on google
         request = r.recognize_google(audio, language='en-US')

         # test in text
         print("you said: " + request)

         # return request
         return  request
      except sr.UnknownValueError:
       print("Google Speech Recognition could not understand audio")
       return "Google Speech Recognition could not understand audio"
      except sr.RequestError:
        print("Google Speech Recognition could not understand audio")
        return "Google Speech Recognition could not understand audio"
      except:
         return "Google Speech Recognition could not understand audio"

# function that speak the audio
def speak(message):

     #start engine of pyttsx3
     engine = pyttsx3.init()

     engine.setProperty('voice', id6)

     #delivery message
     engine.say(message)
     engine.runAndWait()

def ask_day():
    day = datetime.date.today()
    print(day)

    week_day = day.weekday()

    calendar = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    speak(f"Today is {calendar[week_day]}")

def ask_time():
    time = datetime.datetime.now()
    speak(f"at this moment it is, {time.hour} hour {time.minute} minute")

def initial_greeting():
    speak("Hello I am adam, how can I help you?")

def my_assistant():

    #greeting message
    initial_greeting()

    # cut off
    go_on = True

    while go_on:

        #activate microphone and conver to text
        my_reuest = transfer_audio_into_text().lower()

        if 'open youtube' in my_reuest:
          speak("opening youtube")
          webbrowser.open("https://www.youtube.com/")
          continue
        elif 'open web browser' in my_reuest:
          speak("opening web browser")
          webbrowser.open("https://www.google.com/")
          continue
        elif 'what day today' in my_reuest:
          ask_day()
          continue
        elif 'what time today' in my_reuest:
          ask_time()
          continue
        elif 'do wikipedia search for' in my_reuest:
            speak("searching wikipedia")
            search_query = my_reuest.lower().replace("do wikipedia search for", "").strip()
            if search_query:
                answer = wikipedia.summary(search_query, sentences=1)
                speak("According to Wikipedia")
                speak(answer)
            else:
                speak("Please tell me what you want to search on Wikipedia.")
        elif 'search the internet for' in my_reuest:
            speak("searching google")
            reuest = my_reuest.replace('search the internet for', '')
            pywhatkit.search(reuest)
            speak('this is what i found')
        elif 'stop' in my_reuest:
          speak("Thanks for using me")
          go_on = False
          break


my_assistant()







