# U04_Ex06_FutValGraph.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 29 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: FutValGraph Ex06
#     Source: Python Programming
#    Chapter: #04
#
# Program Description
#   This program will make a graph of a future investment
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   Create a graphwin
#   Create a text box asking for the principle of the investment
#   Create an entry object for the principle
#   Get mouse
#   Ask for another click
#   make variable named principal, set to float and get text of inputPrinc
#   Get mouse and close graphics window
#   Do same process for apr of the investment
#   make a graph with labels increasing by 2.5k
#   Make a rectangle using points made by the investment
#   Make a for loop to make calculations for future years
#   Make rectangles using points from the calculation
#   Ask for input and close window


from graphics import *


def main():
    # Creates GraphWin and introduces program
    print("This program will make a graph of a future investment")
    win = GraphWin("Investment growth chart", 320, 240)
    win.setBackground("white")

    # First entry object for the principal of the investment and closes window when complete (after click)
    PrincTxt = Text(Point(160, 100), "What is the principal of the investment?")
    PrincTxt.setTextColor("black")
    PrincTxt.setSize(8)
    PrincTxt.setFace("times roman")
    PrincTxt.draw(win)
    inputPrinc = Entry(Point(160, 120), 10)
    inputPrinc.setText("10.0")
    inputPrinc.draw(win)
    win.getMouse()
    print("Please click again")
    principal = float(inputPrinc.getText())
    print(principal)
    win.getMouse()
    win.close()

    # Second entry object for APR of the investment (closes after final click)
    win = GraphWin("Investment growth chart", 320, 240)
    AprTxt = Text(Point(160, 100), "What is the APR of the investment?")
    AprTxt.setTextColor("black")
    AprTxt.setSize(8)
    AprTxt.setFace("times roman")
    AprTxt.draw(win)
    inputApr = Entry(Point(160, 120), 10)
    inputApr.setText("0.0")
    inputApr.draw(win)
    win.getMouse()
    apr = float(inputApr.getText())
    print(apr)
    win.close()

    # Makes graph using first and second entry objects and a new graphical window
    win = GraphWin("Investment growth chart", 320, 240)
    print("Click on graphics window to continue to your graph")
    win.getMouse()
    Text(Point(20, 230),  ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), ' 10.0K').draw(win)
    height = principal * 0.02
    print(principal)
    print(height)
    print(apr)
    bar = Rectangle(Point(40, 230), (Point(65, 230-height)))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    # Loop for calculation of the bars
    for year in range(1, 11):
        principal = principal * (1 + apr)
        x11 = year * 25 + 40
        height = principal # * 0.02
        bar = Rectangle(Point(x11, 230), Point(x11+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    input("Press ENTER to quit")
    win.close()


main()
