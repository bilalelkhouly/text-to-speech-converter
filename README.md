# PDF Text to Speech Converter

Convert PDF documents into audio speech files using Python. This simple tool allows you to upload a PDF file and generate an MP3 audio file containing the spoken text from the PDF.

## Features

- Upload PDF files for conversion.
- Convert PDF text to speech.
- Save the generated audio as an MP3 file.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/bilalelkhouly/text-to-speech-converter.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pdf-text-to-speech-converter
   ```

3. Install the required Python packages from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. The application window will appear.

3. Click the "Upload file" button to select a PDF file you want to convert.

4. The text from the PDF will be extracted and converted into speech.

5. You will be prompted to choose a location to save the generated MP3 file.

6. After saving, a confirmation message will appear, indicating that the conversion is complete.

## Dependencies

- [PyPDF2](https://pypi.org/project/PyPDF2/): Python library for reading and manipulating PDF files.
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/): Python library and CLI tool to extract text from PDF files and convert it to speech.
- [Tkinter](https://docs.python.org/3/library/tkinter.html): Python standard library for creating graphical user interfaces.
your project's specific details and add any additional sections or information as needed.