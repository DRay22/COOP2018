# U03_Ex16_Fibonacci_Natural.py.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 01 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Ex16 Fibonacci natural numbers
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#   Introduce: This program will find the value of a user selected term in a regular fibonacci sequence
#   Get input for which term to be found, make variable 'n'
#   Make term1 and term2 equal to 1
#   Make an if statement
#       If n is >= 3
#           Make a for loop in range(3, n+1)
#           make variable named thisTerm
#           make thisTerm equal to ter11 + term2
#           make term1 equal to term2
#           make term2 equal to thisTerm
#       print thisTerm
#       if else:
#           print term1
# Algorithm (pseudocode)
#


def main():
    print("This program will find the value of a user selected term in a regular fibonacci sequence")
    n = int(input("Which term would you like to display?   "))
    term1 = 1
    term2 = 1
    if n >= 3:
        for i in range(3, n+1):
            thisTerm = term1 + term2
            term1 = term2
            term2 = thisTerm
        print("The value is:", thisTerm)
    else:
        print("The value is:", term1)


main()
