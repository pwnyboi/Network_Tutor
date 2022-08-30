# This is a netowrking fundamentals helpful tool!
# Purpose of this tool is:
# 1. Train Fundamentals of Networking Concepts
# 2. Test those concepts
# 3. Provide feedback on learning progress


from tkinter import E
import pyfiglet
import termcolor
from pyfiglet import Figlet
from termcolor import colored, cprint
import time


menu_selection = "0"
menu_list = ["1", "2"]
network_tutor_banner = pyfiglet.figlet_format("NetworkTutor")
banner_line = "=============================================================="
menu = pyfiglet.figlet_format("Main Menu", font= "small")
print(banner_line)
print(colored(network_tutor_banner, 'red'))
print(banner_line)

# Displays menu options
def Menu_Display():
    time.sleep(1)
    print(menu)
    menu_list = ["1. OSI Fundamentals", "2. Network Tools", "3. Coming Soon", "4. Coming Soon"]
    time.sleep(.75)
    for menu_item in menu_list:
        print(colored(menu_item, 'green'))
    print(colored("EXIT", "red"))

    time.sleep(.69)


# Input for user to select from menu
def Menu_Select():
    Menu_Select = input("Select Item: ")
    if Menu_Select == "1":
        time.sleep(.69)
        print("you have selected 1")
    if Menu_Select == "2":
        time.sleep(.69)
        print("you have selected 2")
    if Menu_Select == "exit" or "EXIT":
        time.sleep(.69)
        quit()


Menu_Display()
Menu_Select()