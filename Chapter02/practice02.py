# practice02.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: 01 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: #
#
# Program Description
#   This program is an interactive calculator that accepts mathematical expressions
#
#
#
# Algorithm (pseudocode)
#   Introduction program
#   Loop until exit requested
#   Get input (mathematical expression (0 to quit))
#   Test for exit
#   evaluate expression
#   print result


def main():
    # Introduction program
    print("This program is an interactive calculator that accepts mathematical expressions")
    #   Loop until exit requested
    while True:
        #   Get input (mathematical expression (0 to quit))
        expr = eval(input("Please enter a mathematical expression (0 to quit):   "))
        #   Test for exit
        if expr ==0:
            break
        #   evaluate expression

        #   print result
        print("Your solution is", expr)


main()