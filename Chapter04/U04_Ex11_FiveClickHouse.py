# U04_Ex11_FiveClickHouse.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 01 Nov 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Five Click House Ex11
#     Source: Python Programming
#    Chapter: #04
#
# Program Description
# This program will make a house using five user submitted clicks
#
#
#
# Algorithm (pseudocode)
#   Introduce program and give instructions
#   Ask for input(no data type) 'Press ENTER to continue'
#   Make graphics window
#   Get first click
#       find X and Y, define as X1 and Y1
#   Get second click
#       find X and Y, define as X2 and Y2
#   Make a rectangle using X1, Y1 and X2, Y2
#       Make outline black and fill white
#   Draw rectangle
#   Get third click
#   Make variable named X3_cen, (X value of click3 - X2*(1/10)
#   Make X3 the same value as X3_cen
#   Make Y3 the Y value of click 3
#   Make variable named X3_2, (X3_cen + X2 *(1/5)
#   Make Y3_2 the same value as Y2
#   Make a rectangle using these points, X3, Y3 and X3_2, Y3_2
#   Make rectangles Outline black and Fill white
#   Get click4
#   Make variable named X4 (x value of click4 - 25)
#   Make variable named Y4 (y value of click4 - 25)
#   Make X4_2 (X4 + 50)
#   Make Y4_2 (Y4 +50)
#   Make a rectangle using these points (X4, Y4), (X4_2, Y4_2)
#   Make outline black and fill white
#   Get a fifth click
#   Make variable X5 equal to click5 X value
#   Make variable Y5 equal to click5 Y value
#   Make a polygon named 'roof'
#   Make points of polygon X5, Y5,  X1, Y1,  X2, Y1
#   Make outline black and fill white
#   Draw polygon
#   Ask for input(no data type) 'Press ENTER to close the graphics window'
#   Close graphics window
#   Stop process

from graphics import *


def main():
    print("This program will allow ou to draw a house with 5 clicks:")
    print("\n The first click can be anywhere you want it to be, but it will be the top corner of the house")
    print("The second click should be the opposite corner of where you want you house to be")
    print("The third click will be the center of the top of the door")
    print("The fourth click will be the center of the window")
    print("The fifth and final click will be the highest point of the roof")
    input("\nPress ENTER to continue")
    win = GraphWin("Five Click House", 600, 600)
    click1 = win.getMouse()
    X1 = click1.getX()
    Y1 = click1.getY()
    click2 = win.getMouse()
    X2 = click2.getX()
    Y2 = click2.getY()
    Rect1 = Rectangle(Point(X1, Y1), (Point(X2, Y2)))
    Rect1.setOutline("black")
    Rect1.setFill("white")
    Rect1.draw(win)
    click3 = win.getMouse()
    X3_cen = click3.getX() - X2*(1/10)
    X3 = X3_cen
    Y3 = click3.getY()
    X3_2 = X3_cen + X2 * (1/5)
    Y3_2 = Y2
    Door = Rectangle(Point(X3, Y3,), Point(X3_2, Y3_2))
    Door.setOutline("black")
    Door.setFill("white")
    Door.draw(win)
    click4 = win.getMouse()
    X4 = click4.getX() - 25
    Y4 = click4.getY() - 25
    X4_2 = X4 + 50
    Y4_2 = Y4 + 50
    Window = Rectangle(Point(X4, Y4,), (Point(X4_2, Y4_2)))
    Window.setOutline("black")
    Window.setFill("white")
    Window.draw(win)
    click5 = win.getMouse()
    X5 = click5.getX()
    Y5 = click5.getY()
    Roof = Polygon(Point(X5, Y5), Point(X1, Y1), Point(X2, Y1))
    Roof.setOutline("black")
    Roof.setFill("white")
    Roof.draw(win)
    input("\nPress ENTER to close the graphics window")
    win.close()


main()
