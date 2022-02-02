'''
bounce some balls
'''
from tkinter import * # This imports all definitions from tkinter
from random import randint

def getRandomColor():
    color = '#'
    for j in range(6):
        color += toHexChar(randint(0, 15)) # Add random digit
    return color

def toHex
