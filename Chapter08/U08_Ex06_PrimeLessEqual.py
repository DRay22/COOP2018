# U08_Ex06_PrimeLessEqual.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: 21 Mar 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: #
#
# Program Description
#   This program will find prime numbers less or equal to n, a user inputted number
#
#
#
# Algorithm (pseudocode)
#   main():
#       introduce program
#       get user's number
#       call calculating function
#       print output


#   Calc():
#       if n > 2:
#           check if any numbers between 2 and math.sqrt(n) are evenly divisible by n (while)
#           if there is one:
#               add to list
#           if there is not:
#               run again
#       if n < 2:
#           add n to list
#           return list


from random import *
import math


global list
global x
global ModN

def main():
    global list
    global x
    global ModN
    list = ' '
    X = 1
    fakeN = 2
    print("fakeN", fakeN)
    print("X", X)
    N = int(input("What is the number that you would like to test?   "))
    while X <= math.sqrt(fakeN) and fakeN <= N:
        ModN = fakeN%X
        print(fakeN)
        print("Mod", ModN)
        if ModN != 0:
            list = str(fakeN) + ', '
            fakeN = fakeN + 1
            print("New fakeN", fakeN)
            X = 2
        if ModN == 0:
            X = X + 1
            print("New X", X)
    print("The numbers returned from this test are: {0}".format(list))


main()
