# U03_Ex11_natural_numbers.py.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: 30 Sept 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
# Introduction: This program will find the sum N natural numbers, find a sum, and cube them,
# where n is a user generated value
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   Get repetition number, define as rep
#   Get starting number, define as startnum
#   Make while loop
#       If rep is greater than two:
#       num1 = startnum + rep
#       print num1**3
#   if rep is less than 2:
#       print startnum**3
#   if rep is equal to two:
#   num2 = startnum + 2
#   print startnum**3


def main():
    # Introduce program
    print("This program will find the sum N natural numbers, where n is a user generated value")
    # Get repetition number, define as rep
    rep = eval(input("How many times would you like to repeat?   "))
    num = 0
    nxtnum = 0
    startnum = eval(input("What is the starting number?      "))
    while rep >= 2:
        num1 = startnum**rep-startnum
        print(num1**3)
        break
    if rep <= 2:
        print(startnum**3)
    if rep == 2:
        num2 = 0
        num2 = startnum + 2
        print(num2**3)


main()
