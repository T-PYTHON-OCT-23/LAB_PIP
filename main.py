from art import *
from colorama import Back
phrase = "BELIEVE"
tprint(phrase,font='block')
phrase = "AND"
tprint(phrase,font='block')
phrase = "ACHEIVE"
tprint(phrase,font='block')
phrase = "HELLO"
tprint(phrase,font='sub-zero')

phrase = "BADER"
phrase=text2art(phrase,font='sub-zero')
print(Back.GREEN + phrase + Back.BLACK)