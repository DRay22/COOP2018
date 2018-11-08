# U04_Ex01_ABC.py
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
            win = GraphWin("Exercise 1A", 500, 500)
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
    #   Get x and y of click
    #   Make new points, x3 and y3 using the mouse's coordinates
    #   Make another set of coordinates, x4 and y4. These are just x3 + 20 and y3 + 20
    #   Make a square using these points
    #   Make outline and fill red
    #   Draw square
#   Loop repeats
#   Ask for input (without variable)
#   close graphics window and stop process
    if run == 2:
        def main_b():
            print("This program will display a rectangle, and display a user specified amount when clicked.")
            rep = int(input("How many extra squares would you like to draw?   "))
            win = GraphWin("Exercise 1B", 500, 500)
            shape = Rectangle(Point(50, 90), Point(70, 110))
            shape.setOutline("red")
            shape.setFill("red")
            shape.draw(win)
            for i in range(rep):
                click = win.getMouse()
                x3 = click.getX()
                y3 = click.getY()
                x4 = x3 + 20
                y4 = y3 + 20
                shape3 = Rectangle(Point(x3, y3), Point(x4, y4))
                shape3.setOutline("red")
                shape3.setFill("red")
                shape3.draw(win)
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
#   Get x and y of click
#   Make new points, x3 and y3 using the mouse's coordinates
#   Make another set of coordinates, x4 and y4. These are just x3 + 20 and y3 + 20
#   Make a square using these points
#   Make outline and fill red
#   Draw square
#   Loop repeats
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
            print("This program will display a rectangle, and display a user specified amount when clicked.")
            print("After the specified amount clicks it will give the user the option to click on the graphics window ")
            print("This will close the window")
            rep = int(input("How many extra squares would you like to draw?   "))
            win = GraphWin("Exercise 1C", 500, 500)
            shape = Rectangle(Point(50, 90), Point(70, 110))
            shape.setOutline("red")
            shape.setFill("red")
            shape.draw(win)
            for i in range(rep):
                click = win.getMouse()
                x3 = click.getX()
                y3 = click.getY()
                x4 = x3 + 20
                y4 = y3 + 20
                shape3 = Rectangle(Point(x3, y3), Point(x4, y4))
                shape3.setOutline("red")
                shape3.setFill("red")
                shape3.draw(win)
            msg = Text(Point(95, 90), "Click on window to close it")
            msg.setTextColor("black")
            msg.setSize(12)
            msg.setFace("times roman")
            msg.draw(win)
            win.getMouse()
            win.close()

        main_c()


main()
