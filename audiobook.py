from tkinter import filedialog

import PyPDF2
import pyttsx3

engine = pyttsx3.init()

filename = filedialog.askopenfilename()

startPage = int(
    input("Enter the page number from which the audio will start: "))
with open(filename, 'rb') as book:
    pdfReader = PyPDF2.PdfFileReader(book, strict=False)

    for page in range(startPage-1, pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        text = pageObj.extractText()
        engine.say(text)
        engine.runAndWait()
    book.close()
