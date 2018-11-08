# U04_Ex04_Winter.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 24 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: #
#
# Program Description
#   This program will draw a winter scene
#
#
#
# Algorithm (pseudocode)
#   make a graphics window and define as Win
#       Make window 400x400
#   make a circle
#       Set to points (100, 100) with width of 40
#       Set outline as black
#       Set fill as white
#   Draw circle
#   Make another circle, define as circ2
#       Set to same x value but higher y value (by about 45) make width 30
#       Set outline as black
#       Set fill as white
#   Draw circle
#   Make a third circle, circ3
#       Set points to same x value but higher y value (by 30 points) make width 20
#       Set outline as black
#       Set fill as white
#   Draw circle
#   Make a circle, eye1
#       Set points to 90, 20 with a width of 3
#       Set outline to black
#       Set fill to black
#       Draw eye1
#   Make a circle, eye2
#       Set points to 110, 20 with a width of 3
#       Set outline and fill to black
#       Draw eye2
#   Make a rectangle, call it nose
#       Set points to 100, 27 and 120, 32
#       Make outline and fill orange
#   Draw rectangle

from graphics import *


def main():
    win = GraphWin("Winter", 600, 600)
    win.setCoords(0, 0, 5, 5)
    # set window to 400x400
    arms = Rectangle(Point(0.5, 1.7), (Point(1.5, 1.7)))
    arms.setFill("brown")
    arms.setOutline("brown")
    arms.draw(win)
    circ = Circle(Point(1, 1), 0.4)
    circ.setOutline("black")
    circ.setFill("white")
    circ.draw(win)
    circ2 = Circle(Point(1, 1.55), 0.3)
    circ2.setOutline("black")
    circ2.setFill("white")
    circ2.draw(win)
    circ3 = Circle(Point(1, 1.9), 0.2)
    circ3.setOutline("black")
    circ3.setFill("white")
    circ3.draw(win)
    eye1 = Circle(Point(0.9, 2), 0.03)
    eye1.setOutline("black")
    eye1.setFill("black")
    eye1.draw(win)
    eye2 = Circle(Point(1.1, 2), 0.03)
    eye2.setOutline("black")
    eye2.setFill("black")
    eye2.draw(win)
    nose = Rectangle(Point(1, 1.95), Point(1.2, 1.92))
    nose.setOutline("orange")
    nose.setFill("orange")
    nose.draw(win)
    treeT = Rectangle(Point(3, 0.66), (Point(3.2, 1.2)))
    treeT.setOutline("brown")
    treeT.setFill("brown")
    treeT.draw(win)
    Leav1 = Oval(Point(2.66, 1.44), (Point(3.5, 1)))
    Leav1.setOutline("green")
    Leav1.setFill("green")
    Leav1.draw(win)
    Leav2 = Oval(Point(2.7, 1.65), (Point(3.45, 1.21)))
    Leav2.setOutline("green")
    Leav2.setFill("green")
    Leav2.draw(win)
    Leav3 = Oval(Point(2.8, 1.86), Point(3.35, 1.42))
    Leav3.setOutline("green")
    Leav3.setFill("green")
    Leav3.draw(win)
    Leav4 = Oval(Point(2.9, 2), Point(3.25, 1.63))
    Leav4.setFill("green")
    Leav4.setOutline("green")
    Leav4.draw(win)
    input("Press ENTER to continue")
    win.close()


main()
