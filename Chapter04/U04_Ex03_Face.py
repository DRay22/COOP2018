# U04_Ex03_Face.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 22 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Face Ex03
#     Source: Python Programming
#    Chapter: #04
#
# Program Description
#   This program will draw a face
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   Draw yellow circle
#   Set points to 100, 100
#   Make width 60
#   Make Outline black
#   Make Fill yellow
#   Draw circle
#   Draw black circle
#   Set points to x, y
#   Make width 20
#   Make Outline yellow
#   Make Fill black
#   Draw circle
#   Draw black circle
#   Set points to x, y
#   Make width 20
#   Make Outline yellow
#   Make Fill black
#   Draw circle
#   Draw a line
#   Set points to x, y
#   Make line Outline black
#   Make line Fill black
#   Ask for input
#   Close window

from graphics import *


def main():
    print("This program will draw a face")
    win = GraphWin()
    shape = Circle(Point(100, 100), 60)
    shape.setOutline("black")
    shape.setFill("yellow")
    shape.draw(win)
    eye1 = Circle(Point(80, 80), 10)
    eye1.setOutline("yellow")
    eye1.setFill("black")
    eye1.draw(win)
    eye2 = Circle(Point(120, 80), 10)
    eye2.setOutline("yellow")
    eye2.setFill("black")
    eye2.draw(win)
    line = Line(Point(75, 125), Point(125, 125))
    line.setOutline("black")
    line.setFill("black")
    line.draw(win)
    nose = Polygon(Point(100, 105), Point(100, 95), Point(120, 105))
    nose.setOutline("black")
    nose.setFill("yellow")
    nose.draw(win)
    input("press ENTER to close the window")
    win.close()


main()
