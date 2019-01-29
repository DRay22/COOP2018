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
    return Astring

def Convert():
    string = Input()
    rep = string.count(',') + 1
    string = string.split(', ')
    sel = 0
    Bstring = 'The list is: '
    for i in range(rep):
        string = string[sel]
        if string == 'ten':
            stringfin = '10'
        if string == 'nine':
            stringfin = '9'
        if string == 'eight':
            stringfin = '8'
        if string == 'seven':
            stringfin = '7'
        if string == 'six':
            stringfin = '6'
        if string == 'five':
            stringfin = '5'
        if string == 'four':
            stringfin = '4'
        if string == 'three':
            stringfin = '3'
        if string == 'two':
            stringfin = '2'
        if string == 'one':
            stringfin = '1'
        else:
            string = 'ERROR'
        Bstring = Bstring + (stringfin + ',')
        if sel < rep:
            sel = sel + 1
        if sel == rep:
            sel = sel + 0
        if sel > rep:
            break
    return Bstring


def Print():
    string = Convert()
    print(string)


Print()
