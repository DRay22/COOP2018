# U03_Ex16_Fibonacci_Natural.py.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 01 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#   This program will perform a fibonacci equation with natural numbers
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   define x and y as 0
#   Get input for x
#   Get input for rep
#   for amount in range(rep):
#       x = x + y
#       y = x - y
#       print(x)


def main():
    print("This program will calculate A Fibonacci Sequence with user generated starting points.  ")
    x = 0
    y = 0
    x = eval(input("What is the starting point?   "))
    rep = eval(input("How many numbers are there in this sequence?   "))
    for amount in range(rep):
        x = x + y
        y = x - y
        print(x)


main()
