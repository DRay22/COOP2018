# U04_Ex07_CircleGraphics.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 29 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Circle Graphics Ex07
#     Source: Python Programming
#    Chapter: #04
#
# Program Description
#   This program will make a circle with a user specified radius and find where it intersects with a line on the y
#   intercept.
#
#
# Algorithm (pseudocode)
#   Import Graphics and the math library
#   Introduce program
#   Ask for input for radius, def as r
#   Ask for y intercept of line def as y
#   Set Coords -10, -10, 10, 10
#   Make a circle at (0, 0) with a width of 1
#       Make outline black
#       Make Fill blue
#   Draw circle
#   Draw a horizontal line across the screen with y intercept
#   LinX = +- math.sqrt(r**2 - y**2)
#   LinY = y
#   Draw two points of intersection in red
#       Give points LinX, Lin Y for one line, and -1 * LinX, 1 * LinY


from graphics import *

import math


def main():
    print("This program will draw a circle with a user specified radius and show where it will intercept with a line")
    print("running across the graph at the Y Intercept, which is also user specified")
    print("This graph will have the coordinates -10, -10 and 10, 10")
    r = (int(input("what is the radius of the circle?   ")))
    y = (int(input("\nwhat is the y intercept?   ")))
    if y > r:
        print("The circle will not intercept with the line")
    else:
        win = GraphWin("Circle Graphics.py", 400, 400)
        win.setCoords(-10, -10, 10, 10)
        Circ = Circle(Point(0, 0), r)
        Circ.setOutline("black")
        Circ.setFill("blue")
        Circ.draw(win)
        hline = Line(Point(-10, y), (Point(10, y)))
        hline.setOutline("black")
        hline.setFill("black")
        hline.draw(win)
        LinX = +- math.sqrt(r**2 - y**2)
        LinY = y
        Point1 = Point(LinX, LinY)
        Point1.setOutline("red")
        Point1.setFill("red")
        Point1.draw(win)
        Point2 = Point(-1 * LinX, 1 * LinY)
        Point2.setOutline("red")
        Point2.setFill("red")
        Point2.draw(win)
        P1X = Point1.getX()
        P2X = Point2.getX()
        print("The X value of the first intercept is", P1X)
        print("The X value of the second intercept is", P2X)
        input("\nPress ENTER to Continue")
        win.close()


main()
