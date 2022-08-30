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

network_tutor_banner = pyfiglet.figlet_format("NetworkTutor")
print(colored(network_tutor_banner, 'blue'))

menu_selection = input("Select from menu: ")


def menu_select(menu_selection):
    if menu_selection == true:
        print(str(menu_selection))
    else:
        print("oops error!")
