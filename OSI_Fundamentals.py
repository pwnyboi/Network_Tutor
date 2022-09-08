# The purpose of this file is to create the questions that will be asked during the OSI Fundamentals Module


from typing import ValuesView
import pyfiglet
import termcolor
from pyfiglet import Figlet
from termcolor import colored, cprint
import time
import random
import os

osi_fundamentals_menu = " "
osi_fundamentals_selection = " "
osi_fundamentals_continue = True
osi_correct = 0
osi_incorrect = 0

osi_fundamentals_banner = pyfiglet.figlet_format("OSI Fundamentals")

def start():
    print("Welcome to OSI Fundamentals Module!")
    print("Please Select from the following:")
    print("1. Take OSI Fundamentals Quiz")
    print("2. Get Help")
    print("3. Exit")
    osi_fundamentals_selection = input("Selection: ")
    if osi_fundamentals_selection == "1":
        os.system('cls')
        print("Taking TEST!")
        time.sleep(1)
        quiz()
        osi_fundamentals_selection == " "
    elif osi_fundamentals_selection == "3":
        os.system('cls')
        print("You selected Exit.")
        stop()
    else:
        os.system('cls')
        print("not a valid option at the moment")
        stop()
    return

def quiz():
    global osi_incorrect
    global osi_correct
    osi_correct = 0
    osi_incorrect = 0
    print("test")
    question1()
    os.system('cls')
    review()


def stop():
    print("Exiting Module....")
    time.sleep(2)


q1 = "a"
q2 = "a"
q3 = "a"
q4 = "a"
q5 = "a"
q6 = "a"
q7 = "a"
q8 = "a"
q9 = "a"
q10 = "a"
q11 = "a"
q12 = "a"
q13 = "a"
q14 = "a"
q15 = "a"
q16 = "a"
q17 = "a"
q18 = "a"
q19 = "a"
q20 = "a"


def question1():
    print("Question : ")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")
    q1_user_answer = input("Answer: ")
    if q1_user_answer == q1:
        print("congrats! your right")
        global osi_correct
        osi_correct+=1
        time.sleep(2)
        return osi_correct

    else:
        print("Wrong Answer! Study Harder!")
        global osi_incorrect
        osi_incorrect+=1
        time.sleep(2)
        return osi_incorrect


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


def review():
    print(f'you got {osi_correct} answers correct')
    time.sleep(2)
    print(f'you got {osi_incorrect} answers incorrect')
    time.sleep(2)
    print("Remember to practice as much as you can!")
    time.sleep(3)
    restart_quiz = input("Would you like to restart quiz? Y/N:   ")
    if restart_quiz == "y":
        quiz()
    else:
        print("Have a nice day!")
        time.sleep(.75)


def osi_fundamentals_module():
    print(osi_fundamentals_banner)
    start()

