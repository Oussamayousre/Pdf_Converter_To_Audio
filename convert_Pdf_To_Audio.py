import pyttsx3
from PyPDF2 import PdfFileReader
import pdfplumber

pdfFile = open("contrats.pdf", "rb")
pdfObject = PdfFileReader(pdfFile)

pages = pdfObject.numPages 


with pdfplumber.open("contrats.pdf") as pdf:
    first_page = pdf.pages[0]

    for page in pdf.pages:
        text = page.extract_text()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices') 
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
    engine.stop()