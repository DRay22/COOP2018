# U03_Ex07_Distance.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 26 Sept 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Calculating Distance Ex07
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#   This program will calculate distance based on user generated data points
#
#
#
# Algorithm (pseudocode)
#   Introduce program: "This program will..."
#   Ask for input on data points, x1,x2,y1,y2 (separately)
#   Calculate distance by plugging data points into formula: d = square root of x2-x1**2 + y2-y1**2
#   print output (d)

import math


def main():
    # Introduce program: "This program will calculate distance based on user generated data points"
    print("This program will calculate distance based on user generated data points")
    # Ask for input on data points, x1,x2,y1,y2 (separately)
    x1 = int(input("What is the X1 value?    "))
    y1 = int(input("What is the Y1 value?    "))
    x2 = int(input("What is the X2 value?    "))
    y2 = int(input("What is the Y2 value?    "))
    # Calculate distance by plugging data points into formula: d = square root of x2-x1**2 + y2-y1**2
    x = (x2 - x1)**2
    y = (y2 - y1)**2
    d = math.sqrt(x-y)
    # print output (d)
    print(d)


main()