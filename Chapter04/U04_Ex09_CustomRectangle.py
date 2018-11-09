# U04_Ex09_CustomRectangle.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 29 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Custom Rectangle Ex09
#     Source: Python Programming
#    Chapter: #04
#
# Program Description
#   This program will draw a rectangle based off of user mouse input and display the area and perimeter of it
#
#
#
# Algorithm (pseudocode)
#   Introduce Program
#   make graphics window
#   set coords to 0, 0, 10, 10
#   Get first click and X and Y values of it
#   Get second click and X and Y values of it
#   Make Rectangle based off of both click's values
#   Set fill to red and outline to black
#   Rectangle Length = X2 - X1
#   Rectangle Width = Y1 - Y2
#   Area: Rect length * Rect width
#   Perimeter: length + width * 2
#   Print both area and perimeter
#   Ask for ENTER input
#   Close graphics window


from graphics import *


def main():
    print("This program will draw a rectangle based off of user mouse input and display the area and perimeter of it")
    win = GraphWin("Rectangle")
    win.setCoords(0, 0, 10, 10)
    click1 = win.getMouse()
    X1 = click1.getX()
    Y1 = click1.getY()
    win.checkMouse()
    click2 = win.getMouse()
    X2 = click2.getX()
    Y2 = click2.getY()
    Rect = Rectangle(Point(X1, Y1), (Point(X2, Y2)))
    Rect.setOutline("black")
    Rect.setFill("red")
    Rect.draw(win)
    RectLength = abs(X2 - X1)
    RectWidth = abs(Y2 - Y1)
    RectArea = RectLength * RectWidth
    RectPerim = (RectLength + RectWidth) * 2
    print("The width of the rectangle is", RectWidth, "and the length of the rectangle is", RectLength)
    print("The area of the rectangle is:", RectArea, "The perimeter of the rectangle is:", RectPerim)
    input("Press ENTER to close the window")
    win.close()


main()
