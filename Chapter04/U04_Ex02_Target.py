# U04_Ex02_Target.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: 22  2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Target Ex02
#     Source: Python Programming
#    Chapter: #04
#
# Program Description
#   This program will print an archery target that has a yellow center surrounded by a red ring, a blue ring,
#   a black ring, and a white outer ring.
#
#
# Algorithm (pseudocode)
#   Introduce Program
#   Import graphics
#   Open Graphics Window
#   Draw white circle
#   Set to points 100, 100
#   Make width 60
#   Make Outline black
#   Make Fill white
#   Draw black circle
#   Set to points 100, 100
#   Make width 50
#   Make Outline white
#   Draw blue circle
#   Set to points 100, 100
#   Make width 40
#   Make Outline black
#   Make Fill blue
#   Draw red circle
#   Set to points 100, 100
#   Make width 30
#   Make Outline blue
#   Make Fill red
#   Draw yellow center circle
#   Set to points 100, 100
#   Make width 20
#   Make Outline red
#   Make Fill yellow
#   Ask for Input to close graphics window
#   Close the window


from graphics import *


def main():
    #   Introduce Program
    print("This program will print an archery target")
    #   Open Graphics Window
    win = GraphWin()
    #   Draw white circle
    #   Set to points 100, 100
    #   Make width 60
    shape = Circle(Point(100, 100), 60)
    #   Make Outline black
    shape.setOutline("black")
    #   Make Fill white
    shape.setFill("white")
    shape.draw(win)
    #   Draw black circle
    #   Set to points 100, 100
    #   Make width 50
    shape = Circle(Point(100, 100), 50)
    #   Make Outline white
    shape.setOutline("white")
    #   Make Fill black
    shape.setFill("black")
    shape.draw(win)
    #   Draw blue circle
    #   Set to points 100, 100
    #   Make Width 40
    shape = Circle(Point(100, 100), 40)
    #   Make Outline black
    shape.setOutline("black")
    #   Make Fill blue
    shape.setFill("blue")
    shape.draw(win)
    #   Draw red circle
    #   Set to points 100, 100
    #   Make width 30
    shape = Circle(Point(100, 100), 30)
    #   Make Outline blue
    shape.setOutline("blue")
    #   Make Fill red
    shape.setFill("red")
    shape.draw(win)
    #   Draw yellow center circle
    #   Set to points 100, 100
    #   Make width 20
    shape = Circle(Point(100, 100), 20)
    #   Make Outline red
    shape.setOutline("red")
    #   Make Fill yellow
    shape.setFill("yellow")
    shape.draw(win)
    input("Would you like to close the window? Press ENTER to continue:        ")
    # Close the window
    win.close()


main()
