#pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
#pdfplumber : Plumb a PDF for detailed information about each text character, rectangle, and line. Plus: Table extraction and visual debugging
#pypdf2 : PyPDF2 is a pure-python PDF library capable of splitting, merging together, cropping, and transforming the pages of PDF files
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
