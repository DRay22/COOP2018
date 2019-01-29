# U06_Ex06_Area_of_Tri_Modular.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 17 Jan 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Area of Triangle 06
#     Source: Python Programming
#    Chapter: #06
#
# Program Description
# This program will find the area of a triangle through modular coding
#
#
#
# Algorithm (pseudocode)
#   Func Input():
#       get input for three sides then return in a list
#
#   Func Calc():
#       call input
#       split three sides while assigning to variables
#       make variable called s (sum of the sides): (side1 + side2 + side3)/2
#       make variable called area (the area of the triangle): math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
#       return area
#
#   Func Print():
#       call Calc
#       print area of triangle
#

import math


def Input():
    s1 = int(input('What is the length of the first side?   '))
    s2 = int(input('What is the length of the second side?  '))
    s3 = int(input('What is the length of the third side?   '))
    return s1, s2, s3


def Calc():
    sides = Input()
    side1 = sides[0]
    side2 = sides[1]
    side3 = sides[2]
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area


def Print():
    area = Calc()
    print("The area is {0}".format(area))


Print()
