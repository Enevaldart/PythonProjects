from PyPDF2 import PdfFileReader
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)

def talk(text):
    engine.say(text)
    engine.runAndWait()

#create a pdfFilereader object
reader = PdfFileReader("Son_of_Fate_by_Kiriamiti_John.pdf")
#page = reader.pages[78]
for page in reader.pages:
    text = page.extractText()
    text = ' '.join(text.splitlines())
    #print(text)
    talk(text)

    #The codes below is used to convert the pdf into audio file (mp3 file)

    #engine.save_to_file(text, 'Son_of_Fate_by_Kiriamiti_John.mp3')

#These codes were made on 5th of November 2022. It was a success with not much of trial and error cases.