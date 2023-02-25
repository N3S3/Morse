import tkinter as tk
import pyttsx3

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
        self.morse_to_german_button = tk.Button(master, text="Morse to German", command=self.convert_morse_to_german)
        self.morse_to_german_button.grid(row=5, column=0, pady=5)
        self.german_to_morse_button = tk.Button(master, text="German to Morse", command=self.convert_german_to_morse)
        self.german_to_morse_button.grid(row=6, column=0, pady=5)

        # Create the text-to-speech checkbox
        self.text_to_speech_var = tk.IntVar()
        self.text_to_speech_checkbox = tk.Checkbutton(master, text="Text-to-speech (Morse to German only)", variable=self.text_to_speech_var)
        self.text_to_speech_checkbox.grid(row=7, column=0)

    # Define the Morse to German conversion method
    def convert_morse_to_german(self):
        morse_code = self.input_text.get("1.0", "end-1c")
        german_text = morse_to_german(morse_code)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", german_text)

        # Perform text-to-speech if the checkbox is checked
        if self.text_to_speech_var.get() == 1:
            engine = pyttsx3.init()
            engine.say(german_text)
            engine.runAndWait()

    # Define the German to Morse conversion method
    def convert_german_to_morse(self):
        german_text = self.input_text.get("1.0", "end-1c")
        morse_code = german_to_morse(german_text)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", morse_code)

# Create the GUI window and start the main event loop
root = tk.Tk()
my_gui = MorseCodeConverterGUI(root)
root.mainloop()
