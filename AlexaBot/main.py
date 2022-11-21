import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import smtplib
from PyMultiDictionary import MultiDictionary
from PyPDF2 import PdfFileReader


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
dictionary = MultiDictionary()
#reader = PdfFileReader('C:\Users\hp\PycharmProjects\AlexaBot\resources\Son_of_Fate_by_kiriamiti_John.pdf')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
       print('Listening...')
       # listener.pause_threshold = 1
       # voice = listener.listen(source)

    try:
        print('Recognizing...')
      #  command = listener.recognize_google(voice)
        command = input('Enter your command instead: \n')
        print(command)
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)

    except:
        print('Please say that again...')
        talk('Please say that again...')
        return 'None'
        #pass
    return command


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('enevaldbravo80@gmail.com', '@enevald1')
    server.sendmail('enevaldbravo80@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
     talk('Alexa is running.')
     while True:
       command = take_command().lower()
       if 'wikipedia' in command:
         talk('Searching Wikipedia...')
         command = command.replace('wikipedia', '')
         results = wikipedia.summary(command, sentences=2)
         talk('According to wikipedia')
         print(results)
         talk(results)

       elif 'open youtube' in command:
         webbrowser.open("youtube.com")

       elif 'open google' in command:
         webbrowser.open("google.com")

       elif 'open stackoverflow' in command:
         webbrowser.open('stackoverflow.com')

       elif 'play' in command:
         song = command.replace('play', '')
         talk('playing ' + song)
         pywhatkit.playonyt(song)

       elif 'time' in command:
         time = datetime.datetime.now().strftime('%I:%M:%p')
         talk('Current time is ' + time)

       elif 'date' in command:
         talk('sorry, I have a headache')

       elif 'are you single' in command:
         talk('I am in a relationship with wifi')

       elif 'joke' in command:
         talk(pyjokes.get_jokes())

       elif 'meaning' in command:
         dic = command.replace('what is the meaning of', '')
         talk(dictionary.meaning('en', dic))
         print(dictionary.synonym('en', dic))

       elif 'shut down' in command:
           os.system('shutdown -s')

       elif 'email to' in command:
           try:
               talk('What should I say?')
               content = take_command()
               to = 'enevaldbravo@gmail.com'
               sendEmail(to, content)
               talk("Email has been sent!")
           except Exception as e:
               print(e)
               talk("Sorry, I am not able to send this email")

       else:
         talk('I, Alexa, cannot understand what you are saying.\n')

         #during the development of the program sme modules took longer to install.
         # such mudules include the dictionary module and therefore instead of taking
         # more time on the same thing, I had to put it out for later approach.

         # On 5th of November 2022, I had to work on the several issues. These included:
         # 1. The pdf to audio - DONE but the snippet isn't yet copied here
         # 2. My bot to play my local musics
         # 3. much more.
