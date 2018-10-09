# U03_Ex09_Area_of_Tri.py.py
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
# This program will calculate the area of a triangle with user generated measurements
#
#
#
# Algorithm (pseudocode)
#   Introduce Program
#   Get input (a,b,c)
#   Calculate using s = (a + b + c)/2
#   Calculate using area = math.sqrt s(s - a)(s - b)
#   Print area

import math


def main():
    # Introduce Program
    print("This program will calculate the area of a triangle with user generated measurements")
    #   Get input (b, h)
    b = int(input("What is the base of the triangle?   "))
    h = int(input("What is the height of the triangle?  "))
    area = math.sqrt((1/2*b)*h)
    print("the area of the triangle is", area,)


main()
