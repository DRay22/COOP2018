# U05_Ex04_Acronym.py
#
# Author: Donovan ray
# Course: Coding for OOP
# Section: A2
#     Date: 29 Nov 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Acronym Exercise 4
#     Source: Python Programming
#    Chapter: #05
#
# Program Description
#   This program will make an acronym for a phrase that contains three words
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   get input for the phrase
#   split phrase by spaces
#   initialize acronym as ""
#   make loop for word in list
#       acronym += word[0]
#   acronymFin equal to acronym.upper()
#   print output


def main():
    print("This program will make an acronym for a phrase that the user inputs")
    word = str(input("What is the phrase that you would like to make into an acronym      "))
    list = word.split(' ')
    acronym = ""
    for word in list:
        acronym += word[0]
    acronymFin = acronym.upper()
    print("Your acronym is", acronymFin)


main()
