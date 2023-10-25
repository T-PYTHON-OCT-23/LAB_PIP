from art import *
from colorama import Fore, Back, Style


text1 = text2art("BELIEVE AND ACHIEVE", "block")
print(Fore.LIGHTMAGENTA_EX , text1)

print(Style.RESET_ALL)
text2 = text2art("HELLO", "sub-zero")
print(Back.MAGENTA, text2 )
print(Style.RESET_ALL)




