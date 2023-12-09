import PyPDF2
from gtts import gTTS
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox

window = Tk()
window.title('PDF Text to Speech Converter')
window.minsize(width=500, height=300)


def extract_text(pdf_file):
    text = ''
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        page = reader.pages[0]
        text = page.extract_text()
        return text


def convert_to_speech(text):
    converter = gTTS(text=text, lang='en')
    file_path = asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        converter.save(file_path)
        tkinter.messagebox.showinfo("Complete", "Your text has been converted to speech and saved to your computer!")


def upload_file():
    text = ''
    file_types = [('PDF Files', '*.pdf')]
    file = askopenfilename(filetypes=file_types)
    if file:
        pdf_text = extract_text(file)
        if pdf_text:
            convert_to_speech(pdf_text)


title = Label(window, text='Choose the PDF file', font=('Arial', 30, 'bold'))
title.grid(row=0, column=1)

upload_file_button = Button(window, text='Upload file', command=upload_file)
upload_file_button.grid(row=1, column=1)

window.mainloop()
