"""
- Import random
- Make list of card types and suits
- Loop randomizing both types and suits four times to get four different card values
- Assign values to CardP1, CardP2, CardD1, CardD2
- Check to see if any of the cards are the same
    If found the same, shuffle all four again until all four are different
- return CardP1, CardP2, CardD1, and CardD2
"""


from random import *

from graphics import *


class Deck:


    def __init__(self, amount):
        self.suits = {0: 'H', 1: 'D', 2: 'C', 3: 'S'}
        self.suitNames = {'H': 'Hearts', 'D': 'Diamonds', 'C': 'Clubs', 'S': 'Spades'}
        self.ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self.rankNames = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                  9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
        # global _cards
        _cards = ['Card_Images/Aces/ace_of_hearts.gif', 'Card_Images/2/2_of_hearts.gif',
                  'Card_Images/3/3_of_hearts.gif', 'Card_Images/4/4_of_hearts.gif',
                  'Card_Images/5/5_of_hearts.gif', 'Card_Images/6/6_of_hearts.gif',
                  'Card_Images/7/7_of_hearts.gif', 'Card_Images/8/8_of_hearts.gif',
                  'Card_Images/9/9_of_hearts.gif', 'Card_Images/10/10_of_hearts.gif',
                  'Card_Images/Jacks/jack_of_hearts2.gif', 'Card_Images/Queens/queen_of_hearts2.gif',
                  'Card_Images/Kings/king_of_hearts2.gif',

                  'Card_Images/Aces/ace_of_diamonds.gif', 'Card_Images/2/2_of_diamonds.gif',
                  'Card_Images/3/3_of_diamonds.gif', 'Card_Images/4/4_of_diamonds.gif',
                  'Card_Images/5/5_of_diamonds.gif', 'Card_Images/6/6_of_diamonds.gif',
                  'Card_Images/7/7_of_diamonds.gif', 'Card_Images/8/8_of_diamonds.gif',
                  'Card_Images/9/9_of_diamonds.gif', 'Card_Images/10/10_of_diamonds.gif',
                  'Card_Images/Jacks/jack_of_diamonds2.gif', 'Card_Images/Queens/queen_of_diamonds2.gif',
                  'Card_Images/Kings/king_of_diamonds2.gif',

                  'Card_Images/Aces/ace_of_clubs.gif', 'Card_Images/2/2_of_clubs.gif',
                  'Card_Images/3/3_of_clubs.gif', 'Card_Images/4/4_of_clubs.gif',
                  'Card_Images/5/5_of_clubs.gif', 'Card_Images/6/6_of_clubs.gif',
                  'Card_Images/7/7_of_clubs.gif', 'Card_Images/8/8_of_clubs.gif',
                  'Card_Images/9/9_of_clubs.gif', 'Card_Images/10/10_of_clubs.gif',
                  'Card_Images/Jacks/jack_of_clubs2.gif', 'Card_Images/Queens/queen_of_clubs2.gif',
                  'Card_Images/Kings/king_of_clubs2.gif',

                  'Card_Images/Aces/ace_of_spades.gif', 'Card_Images/2/2_of_spades.gif',
                  'Card_Images/3/3_of_spades.gif', 'Card_Images/4/4_of_spades.gif',
                  'Card_Images/5/5_of_spades.gif', 'Card_Images/6/6_of_spades.gif',
                  'Card_Images/7/7_of_spades.gif', 'Card_Images/8/8_of_spades.gif',
                  'Card_Images/9/9_of_spades.gif', 'Card_Images/10/10_of_spades.gif',
                  'Card_Images/Jacks/jack_of_spades2.gif', 'Card_Images/Queens/queen_of_spades2.gif',
                  'Card_Images/Kings/king_of_spades2.gif']
        self.cardSelect = []
        self.cardValueSelect = []
        self.cardImageSelect = []
        cardValueList = [1.11, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13,
                         2.11, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10, 2.11, 2.12, 2.13,
                         3.11, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13,
                         4.11, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10, 4.11, 4.12, 4.13]
        for i in range(52):
            self.cardSelect.append(i)
        # for card in _cards:
        #     print(card)
        Var = 52
        for i in range(amount):
            print("\nREP:", i)
            Selectsel = randrange(0, Var)    # make 52 a var
            Var -= 1
            print("CARD SELECT LIMIT:", Var)
            if Selectsel > 38:
                ImageSelect = Selectsel - 2
                ValueSelect = Selectsel - 2
            elif Selectsel > 25:
                ImageSelect = Selectsel - 2
                ValueSelect = Selectsel - 1
            elif Selectsel > 12:
                ImageSelect = Selectsel - 1
                ValueSelect = Selectsel - 1
            else:
                ImageSelect = Selectsel
                ValueSelect = Selectsel
            print("SELECTOR:", Selectsel)
            print("NEW IMAGE SELECT:", ImageSelect)
            cardSelected = self.cardSelect[Selectsel] - 1
            print("OLD IMAGE SELECTOR:", cardSelected)
            cardImage = _cards[ImageSelect]
            print(cardImage)
            self.cardImageSelect.append(cardImage)
            _cards.remove(cardImage)
            cardValueSel = ValueSelect
            print("OLD VALUE SELECTOR:", cardSelected)
            print("NEW VALUE SELECTOR:", ValueSelect)
            self.cardValueSelect.append(cardValueList[cardValueSel])
            print("cardValSel", self.cardValueSelect)

    def drawCard(self, whichcard, point, win):
        whichcard -= 1
        cardChosen = self.cardImageSelect[whichcard]
        drawCard = Image(point, cardChosen)
        drawCard.draw(win)

    def getCardValue(self, whichcard):
        whichcard -= 1
        getCardValue = self.cardValueSelect[whichcard]
        print(self.cardValueSelect)
        print(getCardValue)
        return getCardValue