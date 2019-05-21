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

#

#   def InteractGUI():
#       create buttons in interaction box and money box
#       update Dialogue box appropriately
#       update cards appropriately
#       find clicks/ check if buttons are clicked and do according actions
#       check to see who won using the MathFunction, and then display appropriate message and add winning to total

#   def makeCards():
#       make 5 cards using the card function

#   def hitFunction():
#       Activate the 5th card in the deck and change hit status to True


from graphics import *
from Chapter10.button import *
from BlackJackProject.TextCreator import *
from BlackJackProject.TestCardCreate import *
from BlackJackProject.ValueIDEA import *
from BlackJackProject.BlackJackMath import *


def mainGUI():
    StartGame()

def StartGame():
    global GameRep
    GameRep = 0
    GameRep += 1
    CreateGUI()

def CreateGUI():

    # Win
    win = GraphWin("Black Jack Simulator", 800, 800)
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

    # Money BetWin Box
    ChangeBox = Rectangle(Point(6.5, 3.6), Point(8.5, 2.1))
    ChangeBox.setOutline("Black")
    ChangeBox.setFill("Grey")
    ChangeBox.draw(win)

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
    DiagOrig = MakeText(win, Point(2.5, 1), Point(4.75, 4), 14, "Black", "Black Jack Simulator \nPlease Bet")
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
    global MoneyAMTT
    if GameRep > 1:
        MoneyAMTT = MoneyAMTT
    else:
        MoneyAMTT = 300
    MoneyAMT = MakeText(win, Point(7.5, 1.5), Point(8.5, 4), 14, "Black", str(MoneyAMTT) + str("$"))
    MoneyAMT.Activate(win)
    TotMessage = MakeText(win, Point(7.5, 1), Point(8.5, 3.5), 14, "Black", "Total:")
    TotMessage.Activate(win)

    # Bet Money
    BMoneyAMT = MakeText(win, Point(7.5, 3), Point(8.5, 4.5), 14, "Black",str("0$"))
    BMoneyAMT.Activate(win)
    BetMessage = MakeText(win, Point(7.5, 2.5), Point(8.5, 4), 14, "Black", "Bet:")
    BetMessage.Activate(win)

    # Win Message
    WinText = MakeText(win, Point(2.5, 1), Point(4.75, 4), 14, "Black", "You Won!")
    WinText.Deactivate()

    # Lose
    LoseText = MakeText(win, Point(2.5, 1), Point(4.75, 4), 14, "Black", "You Lost...")
    LoseText.Deactivate()


    makeCards(win)

    # LOGIC
    click = Point(0, 0)
    Play3Value = 0
    global HitCheck
    HitCheck = False
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
            Play3Value = cardHit(win)
            HitCheck = True
        if BetButton.clicked(click) == True:
            # Logic behind this
            # Add set amount of money or ask user for bet
            DiagOrig.Deactivate()
            BetText.Activate(win)
            global betAMT
            global NewAMT
            betAMT = BettingGUI(win, MoneyAMTT, MoneyAMT)
            # print(betAMT)
            NewAMT = MoneyAMTT - betAMT
            MoneyAMTT = NewAMT
            MoneyAMT.UpdateText(str("$") + str(NewAMT))
            BMoneyAMT.UpdateText(str("$") + str(betAMT))

        if StayButton.clicked(click) == True:
            # Logic behind this
            # End action time/get results
            DiagOrig.Deactivate()
            StayText.Activate(win)
            Math = BlackJackMath(Play1Value, Play2Value, Play3Value, Deal1Value, Deal2Value, HitCheck)
            Win = Math.winCheck(betAMT, Play1Value, Play2Value, Play3Value)
            if Win == False:
                Deal2Cover.undraw()
                StayText.Deactivate()
                DiagOrig.Deactivate()
                LoseText.Activate(win)
                BMoneyAMT.UpdateText("$0")
                win.getMouse()
                HitCover = Rectangle(Point(4.5, 5.5), Point(6.5, 7.43))
                HitCover.setFill('Dark Green')
                HitCover.setOutline("Dark Green")
                HitCover.draw(win)
                LoseText.Deactivate()
                makeCards(win)
                HitCheck = False
            else:
                Deal2Cover.undraw()
                StayText.Deactivate()
                DiagOrig.Deactivate()
                WinText.Activate(win)
                MoneyAMTT = Win + NewAMT
                MoneyAMT.UpdateText("$" + str(MoneyAMTT))
                BMoneyAMT.UpdateText("$0")
                win.getMouse()
                WinText.Deactivate()
                HitCover = Rectangle(Point(4.5, 5.5), Point(6.5, 7.43))
                HitCover.setFill('Dark Green')
                HitCover.setOutline("Dark Green")
                HitCover.draw(win)
                makeCards(win)
                HitCheck = False
            if MoneyAMTT == 0:
                EndGameText = MakeText(win, Point(2.5, 1.2), Point(4.75, 4.2), 14, "Black", "You are out of money")
                EndGameText.Activate(win)
                win.getMouse()
                quit()
        win.getMouse()
    if QuitButton.clicked(click) == True:
        quit()


def makeCards(win):
    global cards
    global Deal1Value, Deal2Value, Play1Value, Play2Value
    global Deal2Cover
    cards = Deck(5)
    cards.drawCard(1, Point(1.5, 3.5), win)
    Deal1Value = cards.getCardValue(1)
    cards.drawCard(2, Point(3.5, 3.5), win)
    Deal2Value = cards.getCardValue(2)
    cards.drawCard(3, Point(1.5, 6.5), win)
    Play1Value = cards.getCardValue(3)
    cards.drawCard(4, Point(3.5, 6.5), win)
    Play2Value = cards.getCardValue(4)
    Deal2Cover = Image(Point(3.5, 3.5), "Card_Images/Back_of_Card.ppm")
    Deal2Cover.draw(win)


def cardHit(win):
    global Play3Value
    cards.drawCard(5, Point(5.5, 6.5), win)
    Play3Value = cards.getCardValue(5)
    return Play3Value


def BettingGUI(win, prevAMT, MoneyAMT):
    previous = str(prevAMT)
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
        NewValue = int(previous) - int(BetAmt)
        MoneyAMT.UpdateText(str(NewValue))
        return int(BetAmt)
    if GUIClose.clicked(clickcheck) == True:
        GUIBack.undraw()
        GUIText.Deactivate()
        GUIInput.undraw()
        GUIConfirm.Unexist()
        GUIClose.Unexist()
        return 0





mainGUI()