# U05_Ex10_WordAverage.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 05 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Word Average 10
#     Source: Python Programming
#    Chapter: #05
#
# Program Description
#   This program will count the amount of words in a phrase inputted by the user and the average word length
#
#
#
# Algorithm (pseudocode)
#   introduce program
#   get phr as input for the phrase
#   Make Avg equal to wordAvg(phr)
#   split phr
#   make variable called wordCount equal to 0
#   make loop for word in phrSplit:
#      add one to wordCount
#   print output
#
#   wordAvg:
#       phrSplitAvg equal to phr.split(" ")
#       make variable wordlst equal to negative one
#       word 2 equal to 0
#       for word in phrSplitAvg:
#           wordlst = wordlst + 1
#           wordsel = phrSplitAvg[wordlst]
#           make word1 = len(wordsel)
#           wordlen = word1 + word2
#           word1 = word2
#           word2 = wordlen
#       return word2


def wordAvg(phr):
    phrSplitAvg = phr.split(" ")
    wordlst = -1
    word2 = 0
    for word in phrSplitAvg:
        wordlst = wordlst + 1
        wordsel = phrSplitAvg[wordlst]
        word1 = len(wordsel)
        wordlen = word1 + word2
        word1 = word2
        word2 = wordlen
    return word2



def main():
    print("This program will count the amount of words in a phrase inputted by the user and the average word length")
    phr = input("What is the phrase? (Please separate each word with a space and do not use punctuation   ")
    Avg = wordAvg(phr)
    phrSplit = phr.split(" ")
    wordCount = 0
    for word in phrSplit:
        wordCount = wordCount + 1
    print("There are {0} words in the phrase".format(wordCount))
    print("The average word length is {0} letters".format(Avg / wordCount))


main()
