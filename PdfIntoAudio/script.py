import PyPDF2
import pyttsx3
import pdfplumber
from flask import send_file
import os


def convert(file):
     book = open(file, 'rb')
     try:
         pdfReader = PyPDF2.PdfFileReader(book)
         pages = pdfReader.numPages
         finalText = ""
         with pdfplumber.open(file) as pdf:
             for i in range(0, pages):
                 page = pdf.pages[i]
                 text = page.extract_text()
                 finalText += text
                 finalText = ' '.join(finalText.splitlines())

         engine = pyttsx3.init()
         voices = engine.getProperty('voices')
         engine.setProperty('voice', voices[1].id)
         engine.setProperty('rate', 170)
         new_file = file.replace('pdf', 'mp3')
         new_file = new_file.replace('uploads', 'downloads')
         engine.save_to_file(finalText, new_file)
         engine.runAndWait()
     except ValueError:
         return " Invalid input"
