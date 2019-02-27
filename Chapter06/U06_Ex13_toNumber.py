# U06_Ex13_toNumber.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 18 Jan 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: To Number 13
#     Source: Python Programming
#    Chapter: #06
#
# Program Description
# This program will convert a string to a number
#
#
#
# Algorithm (pseudocode)
# Func Input():
#   Get input as Astring
#   return Astring
#
# Func convert():
#   split Atring by comma
#   set of if statements (ex: If Astring[sel] == 'one':)
#       return numerical number - 1
#   if else:
#       break
#   use returned number as a selector to a list of ints
#   add all together in a string (Bstring)
#   return Bstring
#
# Func print():
#   call Calc
#   print output of Calc


def Input():
    print("This program will convert a list of strings to a list of ints.")
    print("Please do not use capital letters, the list goes from 1 to 10.")
    Astring = str(input("What is the list of numbers that you would like to convert?  (Please seperate by commas)   "))
    return Astring.split(",")

def Convert(Astring):
    rep = Astring.count(',') + 1
    stringspl = Astring
    print(stringspl)
    # print("\nDebugging: \n \nstring split", string)
    sel = 0
    Bstring = 'The list is: '
    sel = -1
    print(stringspl)
    for i in range(len(stringspl)):
        stringspl[i] = eval(stringspl[i])
    return stringspl


def Print():
    Astring = Input()
    string = Convert(Astring)
    print('The new list is:', string)


Print()
