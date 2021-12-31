from helpers import morse as s

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