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
    Astring = str(input("What is the list of numbers that you would like to convert?  (Please seperate by commas)   "))
    return Astring

def Convert():
    string = Input()
    rep = string.count(',') + 1
    string = string.split(',')
    sel = -1
    Bstring = 'The list is: '
    for i in range(rep):
        sel = sel + 1
        print(sel)
        print(string[sel])
        if string[sel] == 'one' or 'One':
            string = '1'
        if string[sel] == 'two' or 'Two':
            string = '2'
        if string[sel] == 'three' or 'Three':
            string = '3'
        if string[sel] == 'four' or 'Four':
            string = '4'
        if string[sel] == 'five' or 'Five':
            string = '5'
        if string[sel] == 'six' or 'Six':
            string = '6'
        if string[sel] == 'seven' or 'Seven':
            string = '7'
        if string[sel] == 'eight' or 'Eight':
            string = '8'
        if string[sel] == 'nine' or 'Nine':
            string = '9'
        if string[sel] == 'ten' or 'Ten':
            string = '10'
        else:
            print("Number out of range or used with incorrect syntax")
        Bstring = Bstring + str(string) + ','
        print(Bstring)
    return Bstring


def Print():
    string = Convert()
    print(string)


Print()
