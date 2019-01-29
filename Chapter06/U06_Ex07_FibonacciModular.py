# U06_Ex07_FibonacciModular.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 15 Jan 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Fibonacci Modular 07
#     Source: Python Programming
#    Chapter: #06
#
# Program Description
# This program will print a fibonacci sequence using modular coding
#
#
#
# Algorithm (pseudocode)
#
#
#
#
#


# Notes from previous code:
#    print("This program will find the value of a user selected term in a regular fibonacci sequence")
#    n = int(input("Which term would you like to display?   "))
#    term1 = 1
#    term2 = 1
#   if n >= 3:
#        for i in range(3, n+1):
#            thisTerm = term1 + term2
#            term1 = term2
#            term2 = thisTerm
#        print("The value is:", thisTerm)
#    else:
#        print("The value is:", term1)

def Input():
    term = int(input('What term would you like to select?  '))
    return term

def Fibonacci():
    term = Input()
    term1 = 1
    term2 = 1
    if term >= 3:
        for i in range(3, term+1):
            thisTerm = term1 + term2
            term1 = term2
            term2 = thisTerm
        return"The value is:", thisTerm
    else:
        return"The value is:", term1


def Print():
    FibonacciNum = Fibonacci()
    print(FibonacciNum)


Print()

