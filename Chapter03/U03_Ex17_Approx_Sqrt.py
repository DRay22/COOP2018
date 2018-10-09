# U03_Ex17_Approx_Sqrt.py.py
#
# Author: Donovan Ray
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
#   This program will approximate the square root of a number (User generated) and display it
#
#
#
# Algorithm (pseudocode)
#   Introduce Program
#   Input: X for number to be squared, Y for repetition of guessing equation
#   Define guess as x/2
#   Define square root
#   print square root
#   First guess: (guess + x/guess)/2
#   Print first guess
#   Print distance between square root and first guess
#   Loop first guess algorithm Y amount of times
#   print looped guess and distance (in loop)


import math


def main():
    print("This program will approximate square root.  ")
    print(" ")
    x = eval(input("What is the number that you would like to square?   "))
    print(" ")
    y = eval(input("How many times would you like to repeat the guess?  "))
    print(" ")
    guess = x/2
    print("The guess is", guess)
    print(" ")
    square = math.sqrt(x)
    print("The square root is", square)
    print(" ")
    approx = (guess + x/guess)/2
    print("The approximation is", approx)
    print(" ")
    dist = approx - square
    print("The distance between the two is", dist)
    print(" ")
    for y in range(y):
        approx1 = ((guess + x/guess)/2)*y
        print(" ")
        print("The improved guess is", approx1)
        print(" ")
        print("The distance between the square root and the improved guess is", approx1 - square)


main()
