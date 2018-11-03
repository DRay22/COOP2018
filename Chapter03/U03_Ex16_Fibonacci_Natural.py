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
#   This program will perform a fibonacci equation with natural numbers
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   define start and y as 0
#   Get input for start (will be used as starting number)
#   Get input for rep (used for repetition)
#   for amount in range(rep):
#           This will be used for calculating the sequence and how it increases.
#       start = start + y
#       y = start - y
#       print(start with description)


def main():
    #   Introduce program
    print("This program will calculate A Fibonacci Sequence with user generated starting points.  ")
    #   define x and y as 0
    start = 0
    y = 0
    #   Get input for x
    start = eval(input("What is the starting point?   "))
    #   Get input for rep
    rep = eval(input("How many numbers are there in this sequence?   "))
    #   for amount in range(rep):
    for amount in range(rep):
        #  x = x + y
        start = start + y
        #  y = x - y
        y = start - y
        #  print(x)
        print("The sequence is", start,)


main()
