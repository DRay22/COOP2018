# U04_Ex08_CustomLine.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: 29 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: #
#
# Program Description
#
#
#
#
# Algorithm (pseudocode)
#   Describe program
#   Make graphics window
#   Ask for mouse input
#   Get x and y of click1
#   Ask for mouse input again
#   Get x and y of click2
#   Press ENTER to continue
#   Make a line based off of those points
#   Make midX and Y by X2 - X1 and Y2 - Y1
#   Make a cyan point with midX and midY
#   Ask for ENTER input
#   close graphics window

from graphics import *


def main():
    print("\nThis program will make a line with points based off of where you click and make a cyan midpoint")
    win = GraphWin()
    click1 = win.getMouse()
    X1 = click1.getX()
    Y1 = click1.getY()
    win.checkMouse()
    click2 = win.getMouse()
    X2 = click2.getX()
    Y2 = click2.getY()
    line = Line(Point(X1, Y1), (Point(X2, Y2)))
    line.setOutline("black")
    line.setFill("black")
    line.draw(win)
    midX = (X1 + X2) * 0.5
    midY = (Y1 + Y2) * 0.5
    mid = Circle(Point(midX, midY), 2)
    mid.setOutline("cyan")
    mid.setFill("cyan")
    mid.draw(win)
    input("\nPress ENTER to close graphics window")
    win.close()


main()

