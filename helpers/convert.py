import os
from helpers import morse as s
from playsound import playsound
from PIL import Image, ImageTk

def convert():
    if s.language.get() == 1:
        get_morse()
    elif s.language.get() == 2:
        get_english()

# Convert a english text to morse code

def get_morse():
    morse_code = ""

    # Making all the text lowercase

    text = s.input_text.get("1.0", s.END)
    text = text.lower()

    # Remove any letters or symbols not in our dicts

    for letter in text:
        if letter not in s.english_to_morse.keys():
            text = text.replace(letter, '')
    
    # Breaking up into individual words based on spaces 

    word_list = text.split(" ")

    # Breaking up again to a list of letters

    for word in word_list:
        letters = list(word)
        # For each letter we get the morse representation
        for letter in letters:
            morse_char = s.english_to_morse[letter]
            morse_code += morse_char
            morse_code += " "

        morse_code += "|"
        
    s.output_text.insert("1.0", morse_code)

def get_english():
    english = ""

    text = s.input_text.get("1.0", s.END)

    # Remove all letters and symbols

    for letter in text:
        if letter not in s.morse_to_english.keys():
            text = text.replace(letter, '')
    
    # Break each word with the |

    word_list = text.split("|")

    # Turn each word into a list of letters

    for word in word_list:
        letters = word.split(" ")
        # For each letter we get the english representation
        for letter in letters:
            english_char = s.morse_to_english[letter]
            english += english_char
        # Seperate individuals words with a space
        english += " "

    s.output_text.insert("1.0", english)

def play():

    # Finding where the morse code is

    if s.language.get() == 1:
        text = s.output_text.get("1.0", s.END)   
    elif s.language.get() == 2:
        text = s.input_text.get("1.0", s.END)
    
    # Play the tones

    for value in text:
        if value == ".":
            playsound(f'{s.PATH}/sounds/dot.mp3')
            s.root.after(100)
        elif value == "-":
            playsound(f'{s.PATH}/sounds/dash.mp3')
            s.root.after(200)
        elif value == " ":
            s.root.after(300)
        elif value == "|":
            s.root.after(700)

def hide_guide():
    s.guide.config(state=s.NORMAL)
    guide.destroy()

def show_guide():
    global morse, guide 

    # Creating another window

    guide = s.Toplevel() 
    guide.title("Morse Guide")

    if os.name in ["nt"]:
        guide.iconbitmap(f"{s.PATH}\images\icon.ico")

    guide.geometry("350x350+"+str(s.root.winfo_x() + 500) + "+" + str(s.root.winfo_y()))

    morse = s.ImageTk.PhotoImage(Image.open(f'{s.PATH}/images/morse_chart.jpg'))
    label = s.ttk.Label(guide, image = morse)
    label.pack(padx = 5, pady = 5, ipadx = 5, ipady = 5)

    # Defining a close button

    close = s.ttk.Button(guide, text = "Close", command = hide_guide)
    close.pack(padx = 10, pady = 5, ipadx = 50)

    # Disable guide button pop up

    s.guide.config(state=s.DISABLED)