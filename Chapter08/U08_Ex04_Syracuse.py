# U08_Ex04_Syracuse.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 21 Mar 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Syracuse 04
#     Source: Python Programming
#    Chapter: #08
#
# Program Description
#   This program will print a syracuse function for a user-given natural number
#
#
#
# Algorithm (pseudocode)
#
#   Global Vars:
#       SyraList = ' '
#
#   Func Main():
#       Introduce program
#       Get user input
#       Call Syracuse Func (with input)
#       print results
#
#
#   Func Syracuse(input):
#       Get X as user input
#       Make while loop for until x = 1:
#           Check is X is even or odd (using mod x by 2)
#           Even:
#               Syr(X) = x/2
#               Add calculation results to SyraList
#           Odd:
#               Syr(X) = 3x + 1
#               Add calculation results to SyraList
#       When x is = 1:
#           return SyraList
List = ''

def Syracuse(Input):
    # Define Variables
    X = Input


    # Make List and return new list
    if X%2 != 0:
        X = (3*X) + 1
        X = int(X)
        return X
    if X%2 == 0:
        X = X/2
        X = int(X)
        return X
    if X == 1:
        return X

def main():
    global List
    # Introduce program
    print("This program will produce a Syracuse Sequence based off of a user-inputted number\n")

    # Get input
    Input = int(input("Please enter a natural number:   "))
    Sequence = Input

    # Call List-making Function
    while Sequence != 1:
        Sequence = Syracuse(Sequence)
        List = List + str(Sequence) + ', '
    Input = str(Input)

    # Print new list
    print("The sequence based off of the natural number is: \n{0}{1}".format(str(Input + ', '), List))

if __name__ == '__main__':
    main()

'''
RESULTS:
========
Syracuse(5)    -->   16 |   16 | [ Pass ]
Syracuse(16)   -->    8 |    8 | [ Pass ]
========
'''