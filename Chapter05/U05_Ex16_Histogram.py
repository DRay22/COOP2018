# U05_Ex16_Histogram.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 09 Jan 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Histogram Ex16
#     Source: Python Programming
#    Chapter: #05
#
# Program Description
#   This program will make a histogram based off of a user selected file
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   Get File
#   open file
#   read lines
#   make a list for numbers 0-10
#   print list
#   make graphics window
#   set coords 0, 0, 12, 16
#   initialize select as 0
#   initialize pointX as 1
#   make loop (x12)
#       define name
#       make text box with point pointX, 1
#       set size 14
#       set Fill black
#       draw
#       make height equal to numlist[select]
#       make bar with points pointX, height and pointX, 1.5
#       set fill to black
#       set width to 12
#       draw
#       add one to select, pointX, and numsel
#   press ENTER to continue
#   close window

from graphics import *


def main():
    print("This program will make a histogram based off of a .txt file submitted by the user")
    file = input("What is the name of the file:      ")
    fileopen = open(file, 'r')
    fileread = fileopen.readlines()
    numlist = [fileread.count('0\n'), fileread.count('1\n'), fileread.count('2\n'), fileread.count('3\n'),
               fileread.count('4\n'), fileread.count('5\n'), fileread.count('6\n'), fileread.count('7\n'),
               fileread.count('8\n'), fileread.count('9\n'), fileread.count('10\n')]
    print(numlist[0:])
    win = GraphWin("Histogram", 500, 500)
    win.setCoords(0, 0, 12, 16)
    select = 0
    pointX = 1
    namelist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numsel = 0
    for i in range(11):
        name = namelist[numsel]
        text = Text(Point(pointX, 1), name)
        text.setSize(14)
        text.setFill('Black')
        text.draw(win)
        height = numlist[select]
        bar = Rectangle(Point(pointX, height), Point(pointX, 1.5))
        bar.setFill('Black')
        bar.setWidth(12)
        bar.draw(win)
        select = select + 1
        pointX = pointX + 1
        numsel = numsel + 1
    input("Press ENTER to continue")
    win.close()

main()
