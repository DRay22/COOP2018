# U07_Ex16_ArcheryScore2.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 26 Feb 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Target 16
#     Source: Python Programming
#    Chapter: #07
#
# Program Description
#       This program will make an archery target that will respond to the user clicking, and score where they clicked
#       Once the user clicks, a hitmarker will be drawn, and Shot, Score, and Total score will be displayed
#
#
# Algorithm (pseudocode)
#
#   scoreTotal = 0 (Global Variable)
#
#
#   Draw target:
#       Draw 5 circles each less by 1 in radius
#
#   Get clicks:
#       Make text objects saying Shot, Score, and Total score (BEFORE LOOP)
#       Run user specified amount of times
#       Get clicks in the graphics window
#       get X and Y values for each
#
#   Draw Markers:
#       Make grey crossheirs on click position (Alter X and Y values (Dependant on line) by 0.5)
#
#   Score:
#       get score based off of click position and it's distance from the center of the target(0,0)
#       Scoring range:
#       < 2, 9 points
#       < 3, 7 points
#       < 4, 5 points
#       < 5, 3 points
#       < 6, 1 point
#       anything else: No points
#       print shot and score as well as displaying them on the screen after every if statement
#       draw hitmarker after every if statement
#       call TotalScore
#
#   TotalScore:
#       Access scoreTotal
#       add score from shot to scoreTotal
#
#
#   Main():
#
#   Get input for number of shots to take
#   Make a graphics window
#   set coords -9, -9, 9, 9 (Ensures that 0,0 is center of target)
#   make background grey
#   Call drawtarg
#   Call getclick
#   print "Click again to close window"
#   win.getMouse()
#   win.close()

from graphics import *

import math

scoreTotal = 0

def DrawTarg(win):

    # Draw Outer Circle
    Circ1 = Circle(Point(0, 0), 6)
    Circ1.setFill("White")
    Circ1.setOutline("White")
    Circ1.draw(win)

    # Draw Next Layer
    Circ3 = Circle(Point(0, 0), 5)
    Circ3.setFill("Black")
    Circ3.setOutline("White")
    Circ3.draw(win)

    # Draw Next Layer
    Circ5 = Circle(Point(0, 0), 4)
    Circ5.setFill("Blue")
    Circ5.setOutline("Black")
    Circ5.draw(win)

    # Draw Next Layer
    Circ7 = Circle(Point(0, 0), 3)
    Circ7.setFill("Red")
    Circ7.setOutline("Blue")
    Circ7.draw(win)

    # Draw Center
    Circ9 = Circle(Point(0, 0), 2)
    Circ9.setFill("Yellow")
    Circ9.setOutline("Red")
    Circ9.draw(win)

def GetClick(win, rep):

    # Initialize Shot Counter and Total Shot Calculator
    ShotRep = 0
    NextShot = 0

    # Set up text displays
    ScoreText = Text(Point(7, 6.5), Point(7.5, 7))
    ScoreText.setTextColor("Black")
    ScoreText.setText("Score: ")
    ScoreText.draw(win)
    ShotText = Text(Point(7, 7.5), Point(7.5, 8))
    ShotText.setTextColor("Black")
    ShotText.setText("Shot: ")
    ShotText.draw(win)
    TotalText = Text(Point(6.5, 8.5), Point(7.5, 9))
    TotalText.setTextColor("Black")
    TotalText.setText("Total Score: ")
    TotalText.draw(win)
    PrevScore = 0

    # Get Clicks
    for i in range(rep):
        ShotRep = ShotRep + 1
        ShotNUM = Text(Point(7.9, 7.5), Point(8.2, 8))
        ShotNUM.setTextColor("Black")
        ShotNUM.setText(ShotRep)
        ShotNUM.draw(win)
        Click = win.getMouse()
        ClickX = Click.getX()
        ClickY = Click.getY()
        print("X:", ClickX, "Y:", ClickY)
        Score(ClickX, ClickY, win, ShotRep, PrevScore, ShotNUM)

def Score(ClickX, ClickY, win, ShotRep, PrevScore, ShotNUM):

    # If the coords are less than 0, make them positive so that math function works
    if ClickX <= -0.000000000001:
        ClickXAlt = ClickX * (-1)
        print('ClickX Changed:', ClickXAlt)
    if ClickY <= -0.000000000001:
        ClickYAlt = ClickY * (-1)
        print('ClickY Changed:', ClickYAlt)
    if ClickX > 0:
        ClickXAlt = ClickX
    if ClickY > 0:
        ClickYAlt = ClickY
    Delta = math.sqrt((ClickXAlt)**2 + (ClickYAlt)**2)
    print(Delta)

    # Get and print score based off of distance from center
    if Delta < 2:
        score = 9
        print("Shot: ", ShotRep, "  |  Score:", score)
        ScoreDisp = Text(Point(8.2, 6.5), Point(8.5, 7))
        ScoreDisp.setText(score)
        ScoreDisp.setTextColor("Black")
        ScoreDisp.draw(win)
        ClickMarker(ClickX, ClickY, win, )
        PrevScore = TotalScore(score, PrevScore, win, ScoreDisp, ShotNUM)
    elif Delta < 3:
        if Delta > 2:
            score = 7
            print("Shot: ", ShotRep, "  |  Score:", score)
            ScoreDisp = Text(Point(8.2, 6.5), Point(8.5, 7))
            ScoreDisp.setText(score)
            ScoreDisp.setTextColor("Black")
            ScoreDisp.draw(win)
            ClickMarker(ClickX, ClickY, win, )
            PrevScore = TotalScore(score, PrevScore, win, ScoreDisp, ShotNUM)
    elif Delta < 4:
        if Delta > 3:
            score = 5
            print("Shot: ", ShotRep, "  |  Score:", score)
            ScoreDisp = Text(Point(8.2, 6.5), Point(8.5, 7))
            ScoreDisp.setText(score)
            ScoreDisp.setTextColor("Black")
            ScoreDisp.draw(win)
            ClickMarker(ClickX, ClickY, win, )
            PrevScore = TotalScore(score, PrevScore, win, ScoreDisp, ShotNUM)

    elif Delta < 5:
        if Delta > 4:
            score = 3
            print("Shot: ", ShotRep, "  |  Score:", score)
            ScoreDisp = Text(Point(8.2, 6.5), Point(8.5, 7))
            ScoreDisp.setText(score)
            ScoreDisp.setTextColor("Black")
            ScoreDisp.draw(win)
            ClickMarker(ClickX, ClickY, win, )
            PrevScore = TotalScore(score, PrevScore, win, ScoreDisp, ShotNUM)

    elif Delta < 6:
        if Delta > 5:
            score = 1
            print("Shot: ", ShotRep, "  |  Score:", score)
            ScoreDisp = Text(Point(8.2, 6.5), Point(8.5, 7))
            ScoreDisp.setText(score)
            ScoreDisp.setTextColor("Black")
            ScoreDisp.draw(win)
            ClickMarker(ClickX, ClickY, win, )
            PrevScore = TotalScore(score, PrevScore, win, ScoreDisp, ShotNUM)
    else:
        score = 0
        print("Shot: ", ShotRep, "  |  Score:", score)
        ScoreDisp = Text(Point(8.2, 6.5), Point(8.5, 7))
        ScoreDisp.setText(score)
        ScoreDisp.setTextColor("Black")
        ScoreDisp.draw(win)
        ClickMarker(ClickX, ClickY, win, )
        PrevScore = TotalScore(score, PrevScore, win, ScoreDisp, ShotNUM)




def ClickMarker(ClickX, ClickY, win,):

            LineX = Line(Point(ClickX - 0.5, ClickY), Point(ClickX + 0.5, ClickY))
            LineX.setFill("Grey")
            LineX.setWidth(2)
            LineX.draw(win)
            LineY = Line(Point(ClickX, ClickY - 0.5), Point(ClickX, ClickY + 0.5))
            LineY.setFill("Grey")
            LineY.setWidth(2)
            LineY.draw(win)



def TotalScore(score, PrevScore, win, ScoreDisp, ShotNUM):
    global scoreTotal
    scoreTotal += score
    PrevScore = scoreTotal
    TotScore = Text(Point(8.4, 8.5), Point(8.9, 9))
    TotScore.setText(scoreTotal)
    TotScore.setTextColor("Black")
    TotScore.draw(win)
    print("Click to shoot again:  ")
    win.getMouse()
    ScoreDisp.undraw()
    ShotNUM.undraw()
    TotScore.undraw()
    return PrevScore

def main():

    # Get amount of shots
    rep = int(input("How many shots would you like to take?  "))

    # Make graphics window
    win = GraphWin("Target", 500, 500)
    win.setCoords(-9, -9, 9, 9)
    win.setBackground("Grey")

    # Call Functions
    DrawTarg(win)
    GetClick(win, rep)

    # Close window
    print("Click to close window")
    win.getMouse()
    win.close()


main()
