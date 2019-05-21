# BlackJackMath.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: 19 FINAL 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: #
#
# Program Description
#
#
#
#
# Algorithm (pseudocode)
#
#
#
#
#


from BlackJackProject import *

from graphics import *

class BlackJackMath:

    def __init__(self, PlayerCardVal1, PlayerCardVal2, PlayerCardVal3, DealerCardVal1,
                 DealerCardVal2, HitCheck):
        """
        SUBSTITUTE CARDVALUE1 WITH WHATEVER THE ACE IS

        Win2.5() refers to the player winning 2.5x the amount he put in.
        """
        global PlayerAce
        PlayerAce = 0
        if HitCheck == False:
            PlayerCardVal3 = 0
        self.DealerValue = DealerCardVal1 + DealerCardVal2
        self.PlayerValue = PlayerCardVal1 + PlayerCardVal2 + PlayerCardVal3
        # print(self.DealerValue)
        # print(self.PlayerValue)
        if PlayerCardVal1 == 11:
            PlayerAce = PlayerCardVal1
        elif PlayerCardVal2 == 11:
            PlayerAce = PlayerCardVal2
        elif PlayerCardVal3 == 11:
            PlayerAce = PlayerCardVal3
        #elif PlayerCardVal4 == 11:
        #    self.PlayerAce = PlayerCardVal4

    def winCheck(self, bet, PlayerCardVal1, PlayerCardVal2, PlayerCardVal3):
        if PlayerCardVal1 == 11:
            PlayerAce = PlayerCardVal1
        elif PlayerCardVal2 == 11:
            PlayerAce = PlayerCardVal2
        elif PlayerCardVal3 == 11:
            PlayerAce = PlayerCardVal3
        else:
            PlayerAce = 0
        if self.PlayerValue == 21:
            bet = bet * 2.5
            return int(bet)
        if self.PlayerValue > 21 and PlayerAce == 11:
            self.PlayerValue -= 10
        elif self.PlayerValue > 21:
            return False
        if self.PlayerValue == self.DealerValue:
            bet = bet * 1
            return int(bet)
        else:
            if self.PlayerValue > self.DealerValue:
                if self.PlayerValue <= 21 or self.DealerValue > 21:
                    bet = bet * 2
                    return int(bet)
            else:
                return False