# from BlackJackProject.CardClass.py import *

from BlackJackProject import *

from graphics import *

class CardCreate:

    def __init__(self, point):
        imagename = "ace_of_spades.gif"  #Whatever image name that matthew gives me
        self.CreateCard = Image(imagename, point)

    def Draw(self, win):
        self.CreateCard.draw(win)

    def Undraw(self):
        self.CreateCard.undraw()