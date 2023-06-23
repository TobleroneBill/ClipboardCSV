from faker import Faker
import pyperclip
import csv
import keyboard
import os
from playsound import playsound
import signal
import colorama

linecount = None
with open('Body.csv','r') as lines:
    linecount = len(lines.readlines())

generator = Faker()
csvFile = open('Body.csv','a',newline='')
writer = csv.writer(csvFile)


colorama.init(autoreset=True)

def addText():
    global linecount
    playsound('Copy.wav')
    print(linecount,pyperclip.paste())
    writer.writerow([linecount,pyperclip.paste()])
    linecount+=1
    print('----------------------------------------------------------------')

def quit():
    print('Quitting')
    playsound('Quit.wav')
    csvFile.close()
    os._exit(0) # think this is like exiting main from C (needs return code)

signal.signal(signal.SIGINT, signal.SIG_IGN)
keyboard.add_hotkey('ctrl+c',addText)
keyboard.add_hotkey('esc',quit)


print('CTRL+C as python interrupt is disabled')
print(colorama.Fore.CYAN + 'CTRL+C' + ' now saves text to CSV')
print(colorama.Fore.RED + 'ESC to quit')
print('----------------------------------------------------------------')

keyboard.wait()
