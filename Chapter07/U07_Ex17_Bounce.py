# U07_Ex17_Bounce.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 21 Feb 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Bouncing 17
#     Source: Python Programming
#    Chapter: #07
#
# Program Description
#   This program will make a ball that bounces around the graphics window
#
#
#
# Algorithm (pseudocode)
#   Func StartQues()
#       get input from user (do you want to start program? yes/no0
#       return value as str
#
#   Func Bounce()
#       make graphics window
#       for i in range(10000)
#           update(30) (to slow it down)
#           randomize dx and dy in range 50, 200
#           draw circle using points dx, dy
#           if statements for borders of window(200, 200)
#               too high:
#                   dx = -1
#               too low:
#                   dx = 1
#               y too far left:
#                   dy = 1
#               y too far right:
#                   dy = -1
#
#   Func main():
#       call input
#       if input = yes:
#           Bounce()
#       else:
#           print("Closing program")

from graphics import *

from random import *

def StartQues():
    yesno = str(input("Start program? (yes/no)    "))
    return yesno

def Bounce(win):
    dx = 0
    dy = 0
    Boundary = 0
    for i in range(10000):
            circle = Circle(Point(dx, dy), 20)
            circle.setFill("Blue")
            circle.setOutline("Black")
            circle.draw(win)
            dx = randrange(50, 200)
            dy = randrange(50, 200)
            if dx < Boundary:
                dx = 1
            if dy < Boundary:
                dy = 1
            update(6)
            circle.undraw()

def main():
    In = StartQues()
    if In == "yes":
        win = GraphWin("Bouncing Ball", 700, 700)
        win.setCoords(0, 0, 200, 200)
        Bounce(win)
    else:
        print("Closing program...")



main()
