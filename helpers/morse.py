import os
import pathlib
import json
from helpers import convert as call
from tkinter import *
from ttkbootstrap import *

# Constants

PATH = pathlib.Path(__file__).parent.resolve()
PATH = str(PATH).replace("/helpers","")
WINDOW_SIZE = "500x350"

# Useful Functions

def config():
    config = open(f"{PATH}/dictionaries/english_to_morse.json")
    english_to_morse = json.load(config)
    morse_to_english = dict([(value, key) for key, value in english_to_morse.items()])

    return english_to_morse, morse_to_english

english_to_morse, morse_to_english = config()

def clear():
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)

# Main Function

def start():

    # Define window settings using ttkboostrap

    global language, input_text, output_text

    style = Style()
    style.theme_use('darkly')
    root = style.master

    if os.name in ["nt"]: # This is just for windows users, linux doesn't support .ico images.
        root.iconbitmap(f"{PATH}/images/icon.ico")
    
    root.title("Morse Code - Translator")
    root.geometry(WINDOW_SIZE)
    root.resizable(0,0)

    # Creating frames

    input_frame = ttk.Frame(root)
    input_frame.pack(padx = 16, pady = (16,8))

    output_frame = ttk.Frame(root)
    output_frame.pack(padx = 16, pady = (8,16))

    # Creating the input's 

    input_text = Text(input_frame, height = 8, width = 30)
    input_text.grid(row = 0, column = 1, rowspan = 3, padx = 5, pady = 5)

    language = IntVar()
    language.set(1)

    morse_button = ttk.Radiobutton(input_frame, text = "English --> Morse Code", variable = language, value = 1)
    morse_button.grid(row = 0, column = 0, pady = (15,0))

    english_button = ttk.Radiobutton(input_frame, text = "Morse Code --> English", variable = language, value = 2)
    english_button.grid(row = 1, column = 0)

    guide = ttk.Button(input_frame, text = "Guide")
    guide.grid(row = 2, column = 0, sticky = "WE", padx = 10, ipadx = 56)

    # Creating the outputs

    output_text = Text(output_frame,height = 8,width = 30)
    output_text.grid(row = 0, column = 1, rowspan = 4, padx = 5, pady = 5)

    convert_button = ttk.Button(output_frame, text = "Convert", command = call.convert)
    convert_button.grid(row = 0, column = 0, padx = 10, ipadx = 50)

    play_button = ttk.Button(output_frame, text = "Play Morse")
    play_button.grid(row = 1, column = 0, padx = 10, sticky = "WE")

    clear_button = ttk.Button(output_frame, text = "Clear", command = clear)
    clear_button.grid(row = 2, column = 0, padx = 10, sticky = "WE")

    quit = ttk.Button(output_frame, text = "Quit", command = root.destroy)
    quit.grid(row = 3, column = 0, padx=10, sticky = "WE")

    # Running the mainloop for our window 

    root.mainloop()