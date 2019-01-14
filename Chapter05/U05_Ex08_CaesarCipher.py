# U05_Ex08_CaesarCipher.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 06 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Caesar Cipher 08
#     Source: Python Programming
#    Chapter: #05
#
# Program Description
#   This program will encode a phrase given a user inputted key
#
#
#
# Algorithm (pseudocode)
# Main Function:
# Introduce Program
# Get input for phrase
# Split phrase by spaces
# Initialize wordsel (word selector) and lensel (len selector) to -1
# Make a loop to count words
# Make a loop to get letters in those words
# Assign a number to a letter using list with math
# Make 'If' statement to ensure that the cipher is circular (the program will cipher z to the beginning of the alphabet,
# will not stop if it hits the end of the alphabet list)
# Find new letter in list starting with 'a'
# add all letters together
# return final cipher
#   Print Function:
#   Define cipherFin as " "
#   Define printFin as main(cipherFin)
#   print printFin


def main(cipherFin):
    # Introduce program
    print("This program will encode phrases into a caesar cipher")

    # Input
    phr = input("What would you like to encode?  ")

    # Input
    key = int(input("What is the key for this program?   "))

    # Split input
    phrSplit = phr.split(" ")

    # Initialize
    wordsel = -1
    lensel = -1
    cipher2 = " "

    # Loop for words
    for word in phrSplit:
        wordsel = wordsel + 1
        phrWordSel = phrSplit[wordsel]
        Wordlen = len(phrWordSel)

        # Loop for letters
        for letter in range(Wordlen):
            lensel = lensel + 1
            Wordlensel = phrWordSel[lensel]

            # Get number from letter
            ciphersel = [(Wordlensel.count('a') * 1) + (Wordlensel.count('b') * 2) + (Wordlensel.count('c') * 3)
                         + (Wordlensel.count('d') * 4)
                         + (Wordlensel.count('e') * 5) + (Wordlensel.count('f') * 6) + (Wordlensel.count('g') * 7)
                         + (Wordlensel.count('h') * 8)
                         + (Wordlensel.count('i') * 9) + (Wordlensel.count('j') * 10) + (Wordlensel.count('k') * 11)
                         + (Wordlensel.count('l') * 12)
                         + (Wordlensel.count('m') * 13) + (Wordlensel.count('n') * 14) + (Wordlensel.count('o') * 15)
                         + (Wordlensel.count('p') * 16)
                         + (Wordlensel.count('q') * 17) + (Wordlensel.count('r') * 18) + (Wordlensel.count('s') * 19)
                         + (Wordlensel.count('t') * 20)
                         + (Wordlensel.count('u') * 21) + (Wordlensel.count('v') * 22) + (Wordlensel.count('w') * 23)
                         + (Wordlensel.count('y') * 24)
                         + (Wordlensel.count('x') * 25) + (Wordlensel.count('z') * 26) + (Wordlensel.count(" ") * 0)]
            cipherselFin = ciphersel[0]
            cipherselFinKey = cipherselFin + key

            # 'If' statement to make cipher circular
            if cipherselFin >= 26 - key:
                cipherselFinKey = (cipherselFin - 26) + key

            # Cipher finding letter using number assigned with key
            cipherlist = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                          's', 't', 'u', 'v', 'w', 'y', 'x', 'z']

            # Add all letters together
            cipher1 = cipherlist[cipherselFinKey]
            cipherFin = cipher2 + cipher1
            cipher2 = cipherFin
    return cipherFin


def print1():
    # define cipherFin
    cipherFin = " "

    # define printFin
    printFin = main(cipherFin)

    # Print Output
    print(printFin)


print1()
