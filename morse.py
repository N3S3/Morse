import tkinter as tk
import pyttsx3

# Define the Morse code to Latin conversion function
morse_to_latin_dict = {
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

def morse_to_latin(morse_code):
    latin_text = ""
    morse_words = morse_code.split("  ")
    for morse_word in morse_words:
        morse_letters = morse_word.split(" ")
        for morse_letter in morse_letters:
            if morse_letter in morse_to_latin_dict:
                latin_text += morse_to_latin_dict[morse_letter]
            else:
                latin_text += "?"
        latin_text += " "
    return latin_text.strip()

# Define the Latin to Morse code conversion function
latin_to_morse_dict = {value: key for key, value in morse_to_latin_dict.items()}

def latin_to_morse(latin_text):
    morse_code = ""
    latin_text = latin_text.upper()
    for char in latin_text:
        if char in latin_to_morse_dict:
            morse_code += latin_to_morse_dict[char] + " "
        elif char == " ":
            morse_code += " "
        else:
            morse_code += "? "
    return morse_code.strip()

# Define the GUI
class MorseCodeConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Morse Code Converter")

        # Create the input and output text boxes
        self.input_label = tk.Label(master, text="Input:")
        self.input_label.grid(row=0, column=0)

        self.input_text = tk.Text(master, height=5, width=50)
        self.input_text.grid(row=1, column=0, padx=10, pady=5)

        self.output_label = tk.Label(master, text="Output:")
        self.output_label.grid(row=2, column=0)

        self.output_text = tk.Text(master, height=5, width=50)
        self.output_text.grid(row=3, column=0, padx=10, pady=5)

        # Create the conversion buttons
        self.morse_to_latin_button = tk.Button(master, text="Morse to Latin", command=self.convert_morse_to_latin)
        self.morse_to_latin_button.grid(row=5, column=0, pady=5)
        self.latin_to_morse_button = tk.Button(master, text="Latin to Morse", command=self.convert_latin_to_morse)
        self.latin_to_morse_button.grid(row=6, column=0, pady=5)

        # Create the text-to-speech checkbox
        self.text_to_speech_var = tk.IntVar()
        self.text_to_speech_checkbox = tk.Checkbutton(master, text="Text-to-speech (Morse to Latin only)", variable=self.text_to_speech_var)
        self.text_to_speech_checkbox.grid(row=7, column=0)

    # Define the Morse to Latin conversion method
    def convert_morse_to_latin(self):
        morse_code = self.input_text.get("1.0", "end-1c")
        latin_text = morse_to_latin(morse_code)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", latin_text)

        # Perform text-to-speech if the checkbox is checked
        if self.text_to_speech_var.get() == 1:
            engine = pyttsx3.init()
            engine.say(latin_text)
            engine.runAndWait()

    # Define the Latin to Morse conversion method
    def convert_latin_to_morse(self):
        latin_text = self.input_text.get("1.0", "end-1c")
        morse_code = latin_to_morse(latin_text)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", morse_code)

# Create the GUI window and start the main event loop
root = tk.Tk()
my_gui = MorseCodeConverterGUI(root)
root.mainloop()
