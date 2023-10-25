from art import *
from colorama import *
Art=text2art("BELIEVE AND ACHEIVE",font='block',chr_ignore=True) # Return ASCII text with block font
print(Art)
Artt=text2art("HELLO",font='sub-zero',chr_ignore=True) # Return ASCII text with block font
print(Artt)

print(Fore.RED + Artt)
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')