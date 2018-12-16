# U05_Ex09_WordCount.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 05 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Word Count 09
#     Source: Python Programming
#    Chapter: #05
#
# Program Description
#   This program will count the amount of words in a phrase inputted by the user
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   Make input variable called phr
#   make a variable called phrSplit
#   initialize wordCount to 0
#   Make for loop (for word in phrSplit)
#       wordCount = wordCount + 1
#   print "There are", wordCount, "words in the phrase"


def main():
    print("This program will count the amount of words in a phrase inputted by the user")
    phr = input("What is the phrase? (Please separate each word with a space and do not use punctuation   ")
    phrSplit = phr.split(" ")
    wordCount = 0
    for word in phrSplit:
        wordCount = wordCount + 1
    print("There are {0:^} words in the phrase".format(wordCount))


main()
