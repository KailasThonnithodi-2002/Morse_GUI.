from tkinter import *

import RPi.GPIO as GPIO

from time import sleep



window = Tk()

GPIO.setmode(GPIO.BOARD)  # setting up GPIO on the rpi

GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)  # red

window.geometry("500x100")

window.title("Morse Code Translator")



def translate():

    # Waiting for LED to print the command

    # print(textbox.get())



    button.config(text="translate")

    button.config(background="white")

    button.config(state="disabled")

    

    word = textbox.get()

    textbox.delete(0, END)



    print(f"({word})>>> ", end="")



    for letter in word:

        if letter == " ":  # if there is a space between a character

            next_word_7()

        else:

            print(f"({letter}): ", end="")

            letter = letter.lower()

            function = globals()[letter]  # converting the function into string form (e.g if a is the letter, then call a() as function)

            function()

            next_character_3()



    print("")

    button.config(text="translate")

    button.config(background="green")

    button.config(state="normal")





text = Label(window, text="Please enter word less than 12 characters long", font=("Arial", 10))

textbox = Entry(window, width=20, font=("Arial", 20))

button = Button(window, text="translate", width=20, font=("Arial", 10), command=translate, background="green")





# Morse code rules

def dot():

    # Add code for blinking (1 second)

    print(".", end="")

    GPIO.output(8, GPIO.HIGH)

    sleep(1)

    GPIO.output(8, GPIO.LOW)

    # turn off



def dash():

    # code for blinking (3 seconds)

    print("-", end="")

    GPIO.output(8, GPIO.HIGH)

    sleep(3)

    GPIO.output(8, GPIO.LOW)

    # turn off



def next_symbol_1():  # no led as it is a gap

    sleep(1)



def next_character_3():  # no led as it is a gap

    print(" ", end="")

    sleep(3)



def next_word_7():  # no led as it is a gap

    sleep(7)



# all letter morse code

def a():

    dot()

    next_symbol_1()

    dash()



def b():

    dash()

    next_symbol_1()

    dot()

    next_symbol_1()

    dot()

    next_symbol_1()

    dot()



def c():

    dash()

    next_symbol_1()

    dot()

    next_symbol_1()

    dash()

    next_symbol_1()

    dot()

    next_symbol_1()



def d():

    dash()

    next_symbol_1()

    dot()

    next_symbol_1()

    dot()



def e():

    dot()



def f():

    dot()

    next_symbol_1()

    dot()

    next_symbol_1()

    dash()

    next_symbol_1()

    dot()



def g():

    dash()

    next_symbol_1()

    dash()

    next_symbol_1()

    dot()



def h():

    dot()

    next_symbol_1()

    dot()

    next_symbol_1()

    dot()

    next_symbol_1()

    dot()



def i():

    dot()

    next_symbol_1()

    dot()



def j():

    dot()

    next_symbol_1()

    dash()

    next_symbol_1()

    dash()

    next_symbol_1()

    dash()



def k():

    dash()

    next_symbol_1()

    dot()

    next_symbol_1()

    dash()



def l():

    dot()

    next_symbol_1()

    dash()

    next_symbol_1()

    dot()

    next_symbol_1()

    dot()



def m():

    dash()

    next_symbol_1()

    dash()



def n():

    dash()

    next_symbol_1()

    dot()



def o():

    dash()

    next_symbol_1()

    dash()

    next_symbol_1()

    dash()



def p():

    dot()

    next_symbol_1()

    dash()

    next_symbol_1()

    dash()

    next_symbol_1()

    dot()



def q():

    dash()

    next_symbol_1()

    dash()

    next_symbol_1()

    dot()

    next_symbol_1()

    dash()



def r():

    dot()

    next_symbol_1()

    dash()

    next_symbol_1()

    dot()



def s():

    dot()

    next_symbol_1()

    dot()

    next_symbol_1()

    dot()



def t():

    dash()



def u():

    dot()

    next_symbol_1()

    dot()

    next_symbol_1()

    dash()



def v():

    dot()

    next_symbol_1()

    dot()

    next_symbol_1()

    dot()

    next_symbol_1()

    dash()



def w():

    dot()

    next_symbol_1()

    dash()

    next_symbol_1()

    dash()



def x():

    dash()

    next_symbol_1()

    dot()

    next_symbol_1()

    dot()

    next_symbol_1()

    dash()



def y():

    dash()

    next_symbol_1()

    dot()

    next_symbol_1()

    dash()

    next_symbol_1()

    dash()



def z():

    dash()

    next_symbol_1()

    dash()

    next_symbol_1()

    dot()

    next_symbol_1()

    dot()



text.pack()

textbox.pack()

button.pack()



window.mainloop()

