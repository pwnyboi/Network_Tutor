# The purpose of this file is to create the questions that will be asked during the OSI Fundamentals Module


from typing import ValuesView
import pyfiglet
import termcolor
from pyfiglet import Figlet
from termcolor import colored, cprint
import time

osi_fundamentals_menu = " "
osi_fundamentals_selection = " "
osi_fundamentals_continue = True


def start():
    print("Welcome to OSI")
    print("Please Select from the following:")
    print("1. Take OSI Fundamentals Quiz")
    print("2. Help")
    print("3. Exit")
    osi_fundamentals_selection = input("Selection: ")
    if osi_fundamentals_selection == "1":
        print("Taking TEST!")
        osi_fundamentals_selection == " "
        osi_fundamentals_continue = False
        return osi_fundamentals_continue
    elif osi_fundamentals_selection == "3":
        print("You selected Exit.")
        stop()
    else:
        print("not a valid option at the moment")
        stop()


def stop():
    print("Exiting Module....")
    time.sleep(1)
    osi_fundamentals_selection = "Module Ended"


q1 = "d"
q2 = "1"
q3 = "1"
q4 = "1"
q5 = "1"
q6 = "1"
q7 = "1"
q8 = "1"
q9 = "1"
q10 = "1"
q11 = "1"
q12 = "1"
q13 = "1"
q14 = "1"
q15 = "1"
q16 = "1"
q17 = "1"
q18 = "1"
q19 = "1"
q20 = "1"


def question1():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question2():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question3():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question4():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question5():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question6():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question7():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question8():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question9():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question10():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question11():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question12():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question13():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question14():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question15():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question16():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question17():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question18():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question19():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def question20():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")


def osi_fundamentals_module():
    start()
