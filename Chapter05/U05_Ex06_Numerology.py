# U05_Ex06_Numerology.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 06 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Numerology 06
#     Source: Python Programming
#    Chapter: #05
#
# Program Description
#   This program will convert a phrase or name into a number based off of each letter's position in the alphabet
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   get str as nameinput
#   make nameinput lowercase
#   make list called nameNum:
#       make each property in list name.count<letter> * <letter's position in alphabet> for each letter and
#       add everything together
#   print nameNum


def main():
    print("This program will convert a phrase or name into a number based off of each letter's position "
          "in the alphabet")
    nameinput = input("What is the name or phrase you would like to convert?   ")
    name = nameinput.lower()
    nameNum = [(name.count('a') * 1) + (name.count('b') * 2) + (name.count('c') * 3) + (name.count('d') * 4)
        + (name.count('e') * 5) + (name.count('f') * 6) + (name.count('g') * 7) + (name.count('h') * 8)
        + (name.count('i') * 9) + (name.count('j') * 10) + (name.count('k') * 11) + (name.count('l') * 12)
        + (name.count('m') * 13) + (name.count('n') * 14) + (name.count('o') * 15) + (name.count('p') * 16)
        + (name.count('q') * 17) + (name.count('r') * 18) + (name.count('s') * 19) + (name.count('t') * 20)
        + (name.count('u') * 21) + (name.count('v') * 22) + (name.count('w') * 23) + (name.count('y') * 24)
        + (name.count('x') * 25) + (name.count('z') * 26) + (name.count(' ') * 0)]
    nameNum = nameNum[0]
    print("The sum of the numeric value(s) is {0}".format(nameNum))


main()
