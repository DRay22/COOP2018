# U03_Ex06_Slope_of_Line.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 25 Sept 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Finding a Slope Ex06
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#   This program will calculate the slope of a line using user submitted data points
#
#
#
# Algorithm (pseudocode)
#   Introduce program "this program will..."
#   Ask for X1 and Y1 data points ("Enter X1 data point") ("Enter Y1 data point")
#   Ask for X2 and Y2 data points ("Enter X2 data point") ("Enter Y2 data point")
#   Calculate Slope using formula: Slope = (y2-y1)/(x2-x1)
#   print(slope)


def main():
    # Introduce program "This program will calculate the slope of a line using user generated data points"
    print("This program will calculate the slope of a line using user generated data points")
    # Ask for X1 data point
    x1 = eval(input("Enter the X1 data point"))
    # Ask for Y1 data point
    y1 = eval(input("Enter the Y1 data point"))
    # Ask for X2 data point
    x2 = eval(input("Enter the X2 data point"))
    # Ask for Y2 data point
    y2 = eval(input("Enter the Y2 data point"))
    # Calculate slope
    y = y2-y1
    x = x2-x1
    s = y/x
    # Print output
    print("The slope is", s,)


main()