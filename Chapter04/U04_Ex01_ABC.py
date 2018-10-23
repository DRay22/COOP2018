# U04_Ex01_ABC.py.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 19 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: ABC Ex01
#     Source: Python Programming
#    Chapter: #04


from graphics import *

# Program Description
# This program will print a square onto the graphics window
#
#
#
# Algorithm (pseudocode)
#   Make an overall main function
#   Ask for input, call variable run
#   If run is less than or equal to 3:
#       If run is equal to 1, launch main_a
#       If run is equal to 2, launch main_b
#       If run is equal to 3, launch main_c
#   If else:
#       say "Invalid input, please enter valid input
#       run process again
#       If else again:
#           say "invalid input, stopping program"


def main():
    run = eval(input("What would you like to run? 1 for 1A, 2 For 1B, 3 For 1C   "))
    if run <= 3:
        print("Valid input, running now")
    else:
        print("Invalid input, please enter valid input   ")
        run = eval(input("What would you like to run? 1 for 1A, 2 For 1B, 3 For 1C   "))
        if run <= 3:
            print("Valid input, running now")
        else:
            print("Invalid input, stopping program")
    # Program Description
    #   This program will print a square onto the graphics window, it will then give the user the option to close
    #   the window
    #
    #
    # Algorithm (pseudocode)
    #   Make GraphWin
    #   Make rectangle
    #       set points to 10, 50 and 30, 70
    #   Make fill and outline red
    #   Draw shape
    #   Ask for input (without assigning a variable)
    #   close the window and end process

    if run == 1:
        def main_a():
            print("This program will print a square onto the graphics window")
            print("it will then give the user the option to close the window")
            win = GraphWin()
            shape = Rectangle(Point(10, 50), Point(30, 70))
            shape.setOutline("red")
            shape.setFill("red")
            shape.draw(win)
            input("press ENTER to close graphics window")
            win.close()

        main_a()

# Program Description
#   This program will display a rectangle, and display more with 10 clicks.
#
#
#
# Algorithm (pseudocode)
#   Make graphics window
#   Make a rectangle
#       Set outline and fill to red
#   Draw rectangle
#   make a for loop:
#   Wait for mouse click
#   Define new x1-2 and y1-2 points by adding 5 to the original points
#   make new rectangle (rectangle2) with new points
#       set outline and fill to red
#   draw new rectangle
#   repeat and add 10 to x1-2 and y1-2
#   Ask for input (without variable)
#   close graphics window and stop process
    if run == 2:
        def main_b():
            print("This program will display a rectangle, and display more with 10 clicks.")
            win = GraphWin()
            shape = Rectangle(Point(10, 50), Point(30, 70))
            shape.setOutline("red")
            shape.setFill("red")
            shape.draw(win)
            for i in range(10):
                win.getMouse()
                x1 = 15
                x2 = 35
                y1 = 55
                y2 = 75
                shape2 = Rectangle(Point(x1, y1), Point(x2, y2))
                shape2.setOutline("red")
                shape2.setFill("red")
                shape2.draw(win)
                input("press ENTER to close graphics window")
                win.close()

        main_b()

# Program Description
#   This program will display a rectangle, and display more with 10 clicks. After the 10 clicks it will give the user
#   The option to click on the graphics window to close the window.
#
#
# Algorithm (pseudocode)
#   Make graphics window
#   Make a rectangle
#       Set outline and fill to red
#   Draw rectangle
#   make a for loop:
#   Wait for mouse click
#   Define new x1-2 and y1-2 points by adding 5 to the original points
#   make new rectangle (rectangle2) with new points
#       set outline and fill to red
#   draw new rectangle
#   repeat and add 10 to x1-2 and y1-2
#   After loop is complete:
#   Make text with points 10, 50 "Click on window to close it" assign to variable msg
#   Set color to black
#   Make size 36
#   Set font to times new roman
#   draw
#   Wait for click
#   close graphics window and stop process
    if run == 3:
        def main_c():
            print("This program will display a rectangle, and display more with 10 clicks.")
            print("After the 10 clicks it will give the user the option to click on the graphics window ")
            print("This will close the window")
            win = GraphWin()
            shape = Rectangle(Point(10, 50), Point(30, 70))
            shape.setOutline("red")
            shape.setFill("red")
            shape.draw(win)
            for i in range(10):
                win.getMouse()
                x1 = 15
                x2 = 35
                y1 = 55
                y2 = 75
                shape2 = Rectangle(Point(x1, y1), Point(x2, y2))
                shape2.setOutline("red")
                shape2.setFill("red")
                shape2.draw(win)
            msg = Text(Point(10, 50), "Click on window to close it")
            msg.setTextColor("black")
            msg.setSize(36)
            msg.setFace("times roman")
            msg.draw(win)
            win.getMouse()
            win.close()

        main_c()


main()
