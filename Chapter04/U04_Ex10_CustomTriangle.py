# U04_Ex10_CustomTriangle.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: 01 Nov 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: #
#
# Program Description
#   This program will create a Triangle with mouse clicks on the graphics window
#
#
#
# Algorithm (pseudocode)
#   Introduce Program
#   Create 450p by 450p graphics window named "Custom Triangle"
#   get a mouse click, variable name is click 1
#   Make variables X1 and Y1 based off of mouse click (click1)
#   check for mouse movement before getting mouse click (click2) and points X2 and Y2
#   check for mouse movement
#   get final mouse click, use as click3 and get point X3 and Y3
#   make a polygon named Tri based off of click1, click2, and click3
#   make outline of Tri black, make fill of Tri blue
#   Get lengths of each side Ex. L1 = abs(X1 - X2)
#   Find perimeter by adding all sides together
#   Define s Ex. s = (L1 + L2 + L3)/2
#   Find area Ex. math.sqrt(s * (s-L1) * (s-L2) * (s-L3))
#   Print both area and perimeter on new lines


from graphics import *

import math


def main():
    print("This program will create a Triangle with mouse clicks on the graphics window")
    print("Please click in three different places you would like the three points of the triangle to be")
    win = GraphWin("Custom Triangle", 450, 450)
    click1 = win.getMouse()
    X1 = click1.getX()
    Y1 = click1.getY()
    win.checkMouse()
    click2 = win.getMouse()
    X2 = click2.getX()
    Y2 = click2.getY()
    click3 = win.getMouse()
    X3 = click3.getX()
    Y3 = click3.getY()
    Tri = Polygon(Point(X1, Y1), Point(X2, Y2,), Point(X3, Y3))
    Tri.setOutline("black")
    Tri.setFill("blue")
    Tri.draw(win)
    XL1 = abs(X2 - X1)
    YL1 = abs(Y2 - Y1)
    L1 = XL1 + YL1
    print("The first side is", L1)
    XL2 = abs(X3 - X2)
    YL2 = abs(Y3 - Y2)
    L2 = XL2 + YL2
    print("The second side is", L2)
    XL3 = abs(X1 - X3)
    YL3 = abs(Y1 - Y3)
    L3 = XL3 + YL3
    print("The third side is", L3)
    TriPerim = abs(L1 + L2 + L3)
    print("The perimeter of the triangle is", TriPerim)
    s = (L1 + L2 + L3)/2
    TriArea = math.sqrt(s * (s-L1) * (s-L2) * (s-L3))
    print("The area of the triangle is", TriArea)
    input("\nPress ENTER to continue:   ")
    win.close()


main()
