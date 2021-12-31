# 📡 Morse Translator 

Using the [Tkinter](https://docs.python.org/3/library/tkinter.html) library for tue UI and the [Ttkboostrap](https://pypi.org/project/ttkbootstrap/) 
library to add a theme to it, i made this program that basically takes a complete text of characters and converts them into morse code, 
using the [playsound](https://pypi.org/project/playsound/) library i manage to reproduce the morse code depending on it's value.

## To Run
Just run the program : 
```
python3 main.py
```

## Requirements

You need to install the ttkboostrap library to run the program :
```
pip install ttkbootstrap
```
And to hear the sounds you should install the playsound library : 
```
pip install playsound
```
## Screenshots
<p align="center">
  <img src="https://raw.githubusercontent.com/Thorns-H/morse-translator/main/images/screenshots/gui.jpg?token=ARSBEP3YJCR4YBLXFZLNQ5TB26NRE"/>
</p>

**ⓘ Important:** <br />
* If you don't install Ttkboostrap this script won't work, this is because i am using a `Style()` method.
* The program takes the morse code to play regardless where it is.
* Make sure to close the guide window using the close button, so the guide button enables again.
