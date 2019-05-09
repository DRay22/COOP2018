# GUIBlackJack.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: 07 May 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: #FINAL
#
# Program Description
#
#   This program will create a GUI for the BlackJack Project
#
#
# Algorithm (pseudocode)
#
#   def main():
#       call createGUI()
#
#
#   def CreateGUI():
#       create window using graphics
#       create Dialogue box
#       create PlayerCard area
#       create DealerCard area
#       create money area
#       create Interaction box

#   def InteractGUI():
#       create buttons in interaction box and money box
#       update Dialogue box appropriately
#       update cards appropriately
#       find clicks and do according actions


from graphics import *
from Chapter10.button import *
from BlackJackProject.TextCreator import *

def mainGUI():
    CreateGUI()


def CreateGUI():

    # Win
    win = GraphWin("Black Jack Simulator", 600, 600)
    win.setCoords(0, 9, 9, 0)
    win.setBackground("Dark Green")

    # Diag Box
    DiagBox = Rectangle(Point(0.5, 2), Point(6, 0.5))
    DiagBox.setFill("grey")
    DiagBox.setOutline("Black")
    DiagBox.draw(win)

    # Money Box
    MoneyBox = Rectangle(Point(6.5, 2), Point(8.5, 0.5))
    MoneyBox.setOutline("black")
    MoneyBox.setFill("grey")
    MoneyBox.draw(win)

    # Dealer Card Box
    DealerCardArea = Rectangle(Point(0.5, 2.5), Point(4.5, 4.5))
    DealerCardArea.setFill("Dark Green")
    DealerCardArea.setOutline("Black")
    DealerCardArea.draw(win)

    # Player Card
    PlayerCardArea = Rectangle(Point(0.5, 5), Point(8.5, 7.5))
    PlayerCardArea.setFill("Dark Green")
    PlayerCardArea.setOutline("Black")
    PlayerCardArea.draw(win)

    # Interaction Box
    InterBox = Rectangle(Point(0.5, 7.7), Point(8.5, 8.7))
    InterBox.setOutline("Black")
    InterBox.setFill("Grey")
    InterBox.draw(win)

    # Call Interactions
    InteractGUI(win)



def InteractGUI(win):
    makeButtons(win)


def makeButtons(win):
    # QUIT BUTTON
    QuitButton = Button(win, Point(1.1, 8.25), 1, 0.5, "Quit")
    QuitButton.activate()

    # BET BUTTON
    BetButton = Button(win, Point(2.6, 8.25), 1, 0.5, "Bet")
    BetButton.activate()

    # HIT BUTTON
    HitButton = Button(win, Point(4.1, 8.25), 1, 0.5, "Hit")
    HitButton.activate()

    # STAY BUTTON
    StayButton = Button(win, Point(5.6, 8.25), 1, 0.5, "Stay")
    StayButton.activate()

    # STARTING DIAG
    DiagOrig = MakeText(win, Point(2.5, 1), Point(4.75, 4), 14, "Black", "Black Jack Simulator")
    DiagOrig.Activate(win)

    # HIT MESSAGE
    HitText = MakeText(win, Point(2.5, 1), Point(4.75, 4), 14, "Black", "You have chosen to hit")
    HitText.Deactivate()

    # BET MESSAGE
    BetText = MakeText(win, Point(2.5, 1), Point(4.75, 4), 14, "Black", "You have chosen to bet")
    BetText.Deactivate()

    # STAY MESSAGE
    StayText = MakeText(win, Point(2.5, 1), Point(4.75, 4), 14, "Black", "You have chosen to stay")
    StayText.Deactivate()

    # MONEY MESSAGE
    MoneyAMTT = 300
    MoneyAMT = MakeText(win, Point(7.5, 1), Point(8.5, 4), 14, "Black", str(MoneyAMTT) + str("$"))
    MoneyAMT.Activate(win)

    # LOGIC
    click = Point(0, 0)
    while QuitButton.clicked(click) == False:
        HitText.Deactivate()
        BetText.Deactivate()
        StayText.Deactivate()
        click = win.getMouse()
        if HitButton.clicked(click) == True:
            # Logic behind this
            # Get another card
            DiagOrig.Deactivate()
            HitText.Activate(win)
        if BetButton.clicked(click) == True:
            # Logic behind this
            # Add set amount of money or ask user for bet
            DiagOrig.Deactivate()
            BetText.Activate(win)
            betAMT = BettingGUI(win, MoneyAMTT)
            NewAMT = MoneyAMTT - betAMT
            MoneyAMT.UpdateText(str(NewAMT) +str("$"))
        if StayButton.clicked(click) == True:
            # Logic behind this
            # End action time/get results
            DiagOrig.Deactivate()
            StayText.Activate(win)
        win.getMouse()
    if QuitButton.clicked(click) == True:
        win.close()


def BettingGUI(win, prevAMT):
    previous = prevAMT
    GUIBack = Rectangle(Point(2.25, 3.5), Point(6.75, 4.75))
    GUIBack.setFill("Grey")
    GUIBack.setOutline("Black")
    GUIBack.draw(win)
    GUIText = MakeText(win, Point(4.5, 3.7), Point(5.5, 4.5), 14, "Black", "How much would you like to bet?")
    GUIText.Activate(win)
    GUIInput = Entry(Point(4.5, 4.1), 7)
    GUIInput.setStyle("italic")
    GUIInput.draw(win)
    GUIConfirm = Button(win, Point(3.3, 4.5), 1, 0.5, "Bet")
    GUIConfirm.activate()
    GUIClose = Button(win, Point(5.7, 4.5), 1, 0.5, "Cancel")
    GUIClose.activate()
    clickcheck = win.getMouse()
    if GUIConfirm.clicked(clickcheck) == True:
        BetAmt = GUIInput.getText()
        GUIBack.undraw()
        GUIText.Deactivate()
        GUIInput.undraw()
        GUIConfirm.Unexist()
        GUIClose.Unexist()
        return int(BetAmt)
    if GUIClose.clicked(clickcheck) == True:
        GUIBack.undraw()
        GUIText.Deactivate()
        GUIInput.undraw()
        GUIConfirm.Unexist()
        GUIClose.Unexist()
        return previous





mainGUI()