# U05_Ex15_BarChart.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 17 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Bar Chart 15
#     Source: Python Programming
#    Chapter: #05
#
# Program Description
#   This program will make a bar chart based off of student's exam scores
#
#
#
# Algorithm (pseudocode)
#   introduce program
#   get input for amount of students
#   make loop based off of amount of students
#       get input student's name and scores
#   make graphics window
#   print student's name and bar
#   close window

from graphics import *


def main():
    print('this program will be an utter failure')
    fname = input("What is the name of the file?    ")
    fopen = open(fname, 'r')
    rep = fopen.readline()
    lines = fopen.readlines()
    sel = 0
    win = GraphWin('Bar Chart', 500, 500)
    win.setCoords(0, 0, 130, 9)
    lineY1 = 10
    for i in range(4):
        line = lines[sel]
        if sel <= 4:
            lineY1 = lineY1 - 2
            sel = sel + 1
            split = line.split(' ')
            name1 = split[0]
            number = split[1]
            number = number.split("\n")
            number = number[0]
            text = Text(Point(15, lineY1), name1)
            text.setFill('Black')
            text.setSize(14)
            text.draw(win)
            bar = Rectangle(Point(30, lineY1 + 0.2), Point(number, lineY1-0.2))
            bar.setFill('black')
            bar.draw(win)
            num = Text(Point(110, lineY1), number)
            num.setFill('Black')
            num.draw(win)
        else:
            break
    input("Press ENTER to close the window")
    win.close()


main()
