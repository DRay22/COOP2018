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
#   Func Input():
#       get input for term
#       return term
#
#   Func Fibonacci
#       call Input
#       initialize term1 and term2 as 1
#       if Input >= 3:
#           loop for 3, term+1
#               thisTerm = term1 + term2
#               term1 = term2
#               term2 = thisTerm
#           return value
#       else:
#           return term1
#
#   Func Print():
#       call fibonacci
#       print output
#


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

