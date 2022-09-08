# This is a netowrking fundamentals helpful tool!
# Purpose of this tool is:
# 1. Train Fundamentals of Networking Concepts
# 2. Test those concepts
# 3. Provide feedback on learning progress

import pyfiglet
import termcolor
from pyfiglet import Figlet
from termcolor import colored, cprint
import time
from OSI_Fundamentals import *
import random

menu_selection = "0"
menu_list = ["1", "2"]
network_tutor_banner = pyfiglet.figlet_format("NetworkTutor")
network_tutor_banner2 = pyfiglet.figlet_format("v 1.0", font="small")
banner_line = "=============================================================="
space = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]
menu = pyfiglet.figlet_format("Main Menu", font="small")
print(banner_line)
print(colored(network_tutor_banner, 'cyan'))
print(colored(network_tutor_banner2, 'magenta'))
print(banner_line)
time.sleep(.75)
print(*space, sep="\n")

# Displays menu options
def Menu_Display():
    print(*space, sep="\n")
    print(banner_line)
    print(menu)
    print("Select one of the following options:")
    print(banner_line)
    menu_list = ["1. OSI Fundamentals", "2. Network Tools",
                 "3. Coming Soon", "4. Coming Soon"]
    time.sleep(.1)
    for menu_item in menu_list:
        print(colored(menu_item, 'cyan'))
        time.sleep(.09)
    print(colored("EXIT", "red"))
    time.sleep(.1)


# Input for user to select from menu
def Menu_Select():
    Menu_Select = input("Select Item: ")
    if Menu_Select == "1":
        time.sleep(.69)
        print("you have selected OSI Fundamentals!")
        print(*space, sep="\n")
        osi_fundamentals_module()
        Menu_Select = "0"
        return Menu_Select
    if Menu_Select == "2":
        time.sleep(.69)
        print("you have selected 2")
        print(*space, sep="\n")
        Menu_Select = "0"
        return Menu_Select
    if Menu_Select == "exit" or "EXIT":
        time.sleep(.69)
        quit()


while True:
    Menu_Display()
    Menu_Select()
    continue