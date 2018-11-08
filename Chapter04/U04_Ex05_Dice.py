# U04_Ex05_Dice.py
#
# Author:
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
#   This program will display six sides of dice
#
#
#
# Algorithm (pseudocode)
#   Make a rectangle (but its really a square) and name it dice1
#       Set points to 40, 80, and 80, 40
#       Set outline to black
#       Set fill to black
#   Draw rectangle
#   Make a circle name it one1
#       Set to points 60, 60 and have a width of 4
#       Set outline to black
#       Set fill to black
#   Draw circle
#   Make a rectangle, name it dice2
#       Set to points 100, 60 and 140, 100
#       Set outline to black
#       Set fill to white
#   Make a circle, name is one2
#       Set to points 130, 70, and have a width of 4
#       Set outline and fill to black
#       Draw circle
#   Make a circle, name is two2
#       Set to points 130, 90, and have a width of 4
#       Set outline and fill to black
#       Draw circle

from graphics import *


from graphics import *


def main():
    win = GraphWin("Dice.py", 300, 300)
    win.setCoords(0, 0, 11, 11)
    win.setBackground("green")
    dice1 = Rectangle(Point(1, 2), Point(2, 1))
    dice1.setOutline("black")
    dice1.setFill("white")
    dice1.draw(win)
    one1 = Circle(Point(1.5, 1.5), 0.075)
    one1.setFill("black")
    one1.draw(win)
    dice2 = Rectangle(Point(3, 4), Point(4, 3))
    dice2.setOutline("black")
    dice2.setFill("white")
    dice2.draw(win)
    one2 = Circle(Point(3.25, 3.75), 0.075)
    one2.setFill("black")
    one2.draw(win)
    two2 = Circle(Point(3.75, 3.25), 0.075)
    two2.setFill("black")
    two2.draw(win)
    dice3 = Rectangle(Point(5, 6), Point(6, 5))
    dice3.setOutline("black")
    dice3.setFill("white")
    dice3.draw(win)
    one3 = Circle(Point(5.5, 5.75), 0.075)
    one3.setFill("black")
    one3.draw(win)
    two3 = Circle(Point(5.25, 5.25), 0.075)
    two3.setFill("black")
    two3.draw(win)
    three3 = Circle(Point(5.75, 5.25), 0.075)
    three3.setFill("black")
    three3.draw(win)
    dice4 = Rectangle(Point(7, 8), (Point(8, 7)))
    dice4.setOutline("black")
    dice4.setFill("white")
    dice4.draw(win)
    one4 = Circle(Point(7.25, 7.75), 0.075)
    one4.setFill("black")
    one4.draw(win)
    two4 = Circle(Point(7.75, 7.75), 0.075)
    two4.setFill("black")
    two4.draw(win)
    three4 = Circle(Point(7.25, 7.25), 0.075)
    three4.setFill("black")
    three4.draw(win)
    four4 = Circle(Point(7.75, 7.25), 0.075)
    four4.setFill("black")
    four4.draw(win)
    dice5 = Rectangle(Point(9, 10), (Point(10, 9)))
    dice5.setOutline("black")
    dice5.setFill("white")
    dice5.draw(win)
    one5 = Circle(Point(9.5, 9.5), 0.075)
    one5.setFill("black")
    one5.draw(win)
    two5 = Circle(Point(9.75, 9.25), 0.075)
    two5.setFill("black")
    two5.draw(win)
    three5 = Circle(Point(9.75, 9.75), 0.075)
    three5.setFill("black")
    three5.draw(win)
    four5 = Circle(Point(9.25, 9.25), 0.075)
    four5.setFill("black")
    four5.draw(win)
    five5 = Circle(Point(9.25, 9.75), 0.075)
    five5.setFill("black")
    five5.draw(win)
    input("Press ENTER to continue")
    win.close()


main()