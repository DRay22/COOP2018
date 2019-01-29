# U06_Ex12_NumSum.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 18 Jan 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Number Sum 12
#     Source: Python Programming
#    Chapter: #06
#
# Program Description
#   This program will sum numbers inputted in a list form by the user
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
#       initialize sel as 0
#       make rep = to numlist.count(',') + 1
#       make loop for <rep> times
#           make numsplit = numlist.split(',')
#           make num = int(numsplit[sel])
#           make sum = num + num
#           make sel = sel + 1
#       return sum
#
#   Func Print():
#       sum = Calc()
#       print 'the sum of the numbers is {0}".format(sum)



def Input():
    nums = str(input('What are the numbers you would like to sum? (Please seperate each number by a comma)    '))
    return nums


def Calc():
    numlist = Input()
    sel = 0
    rep = numlist.count(',') + 1
    for i in range(rep):
        numsplit = numlist.split(',')
        num = int(numsplit[sel])
        sum = num + num
        sel = sel + 1
    return(sum)


def Print():
    sum = Calc()
    print("The sum of the numbers is {0}".format(sum))


Print()
