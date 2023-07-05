#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  morse.py
#  
#  Copyright 2023 Sebastian Nestler
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import tkinter as tk
from pil_plus import PilPlus
import pyttsx3
import re
import pyperclip

# Define the Morse code to German conversion function
morse_to_german_dict = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
}

def morse_to_german(morse_code):
    german_text = ""
    morse_words = morse_code.split("  ")
    for morse_word in morse_words:
        morse_letters = morse_word.split(" ")
        for morse_letter in morse_letters:
            if morse_letter in morse_to_german_dict:
                german_text += morse_to_german_dict[morse_letter]
            else:
                german_text += "?"
        german_text += " "
    return german_text.strip()

# Define the German to Morse code conversion function
german_to_morse_dict = {value: key for key, value in morse_to_german_dict.items()}

def german_to_morse(german_text):
    morse_code = ""
    german_text = german_text.upper()
    for char in german_text:
        if char in german_to_morse_dict:
            morse_code += german_to_morse_dict[char] + " "
        elif char == " ":
            morse_code += " "
        else:
            morse_code += "? "
    return morse_code.strip()

# Define the GUI
class MorseCodeConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Morse Code Converter DE")
        master.geometry("500x500")
        # load the image file
        #imagel = PilPlus("/home/logout/Downloads/bw.png")
        #width = imagel.resize(new_width=80)
        #width = imagel.resize(new_height=80)
        # create a label widget with the image
        #imagel.show()

        # place the label widget in the main window
        #label.place(x=0, y=0, relwidth=1, relheight=1)
        background_image = tk.PhotoImage(file="/home/logout/Downloads/bw.png")
        background_label = tk.Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=25, relheight=25)
        # Create the input and output text boxes
        self.input_label = tk.Label(master, text="Eingabe:")
        self.input_label.grid(row=0, column=0)

        self.input_text = tk.Text(master,insertbackground="green", height=5, width=50)
        self.input_text.grid(row=1, column=0, padx=10, pady=5)

        self.output_label = tk.Label(master, text="Ausgabe:")
        self.output_label.grid(row=2, column=0)

        self.output_text = tk.Text(master,insertbackground="green", height=5, width=50)
        self.output_text.grid(row=3, column=0, padx=10, pady=5)

        # Create the conversion buttons
        self.morse_to_german_button = tk.Button(master, text="Morse zu Deutsch", command=self.convert_morse_to_german)
        self.morse_to_german_button.grid(row=5, column=0, pady=5)
        self.german_to_morse_button = tk.Button(master, text="Deutsch zu Morse", command=self.convert_german_to_morse)
        self.german_to_morse_button.grid(row=6, column=0, pady=5)

        # Create the text-to-speech checkbox
        self.text_to_speech_var = tk.IntVar()
        self.text_to_speech_checkbox = tk.Checkbutton(master,foreground="black", background="white", text="Text-zu-Sprache (nur Morse zu Deutsch)", variable=self.text_to_speech_var)
        self.text_to_speech_checkbox.grid(row=7, column=0)

    # Define the Morse to German conversion method
    def convert_morse_to_german(self):
        morse_code = self.input_text.get("1.0", "end-1c")
        german_text = morse_to_german(morse_code)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", german_text)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
                engine.setProperty('voice', voices[0].id)
        # Perform text-to-speech if the checkbox is checked
        if self.text_to_speech_var.get() == 1:
            # Set the text-to-speech engine properties
            engine.setProperty("rate", 150)
            engine.setProperty("volume", 1)
            engine.setProperty("voice", "de")
            # speak the Code
            engine.say(german_text)                
            engine.say('Dieser Service wurde von Sebastian Nestler erstellt.')
            engine.runAndWait()    
        #engine.save_to_file('Hello World' , 'test.mp3')
                

    # Define the German to Morse conversion method
    def convert_german_to_morse(self):
        german_text = self.input_text.get("1.0", "end-1c")
        morse_code = german_to_morse(german_text)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", morse_code)
        
    def copy_output(self):
        # Copy the output text to the clipboard
        output_text = self.output_text.get("1.0", "end-1c")
        pyperclip.copy(output_text)

    def paste_input(self):
        # Paste the clipboard contents into the input text box
        clipboard_text = pyperclip.paste()
        self.input_text.delete("1.0", "end")
        self.input_text.insert("1.0", clipboard_text)

# Create the GUI window and start the main event loop
root = tk.Tk()
my_gui = MorseCodeConverterGUI(root)
root.mainloop()
