# U06_Ex11_SquareNums.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 18 Jan 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Square Numbers 11
#     Source: Python Programming
#    Chapter: #06
#
# Program Description
#   This program will square numbers inputted in a list form by the user
#
#
#
# Algorithm (pseudocode)
#   Func Input():
#       get input, def variable nums
#       return nums
#
#   func Calc():
#       make variable called numlist = Input()
#       print 'Your numbers are:'
#       initialize sel as 0
#       make rep = to numlist.count(',') + 1
#       make loop for <rep> times
#           make numsplit = numlist.split(',')
#           make num = int(numsplit[sel])
#           make numSqr = num**2
#           make sel = sel + 1
#           print numSqr



def Input():
    nums = str(input('What are the numbers you would like to square? (Please seperate each number by a comma)    '))
    return nums


def Calc():
    numlist = Input()
    print("Your numbers are:")
    sel = 0
    rep = numlist.count(',') + 1
    for i in range(rep):
        numsplit = numlist.split(',')
        num = int(numsplit[sel])
        numSqr = num**2
        sel = sel + 1
        print(numSqr)

Calc()
