# U03_Ex09_Area_of_Tri.py.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 30 Sept 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Ex09 finding the area of a triangle
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
# This program will calculate the area of a triangle with user generated measurements
#
#
#
# Algorithm (pseudocode)
#   Introduce Program
#   Get input for all three sides (a, b, c)
#   Calculate using s = (a + b + c)/2
#   Find area using area = math.sqrt(s(s - a)*(s - b)*(s - c))
#   Print "the area of the triangle is:", area,

import math


def main():
    # Introduce Program
    print("This program will calculate the area of a triangle with user generated measurements")
    #   Get input for all three sides (a, b, c)
    a = eval(input("What is the length of the first side of the triangle?  "))
    b = eval(input("What is the length of the second side of the triangle?  "))
    c = eval(input("What is the length of the third side of the triangle?  "))
    #   Calculate using s = (a + b + c)/2
    s = (a + b + c)/2
    #   Find area using area = math.sqrt(s(s - a)*(s - b)*(s - c))
    area = math.sqrt(s(s - a)*(s - b)*(s - c))
    #   Print area
    print("the area of the triangle is", area,)


main()
