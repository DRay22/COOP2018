from graphics import *

from BlackJackProject import *

class TestCardCreate:


    def __init__(self, point):
        imagename = "ace_of_spades.gif"
        self.TestCard = Image(point, imagename)

    def Activate(self, win):
        self.TestCard.draw(win)

    def Unexist(self):
        self.TestCard.undraw()