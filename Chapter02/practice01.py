# practice01.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: 01 oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: #
#
# Program Description
#   This program will do a unit conversion for Joules to Calories
#
# Algorithm (pseudocode)
#   Introduction
#   Get input for Joules (0 to quit)
#   Test for exit condition (break if true)
#   Calculate conversion: 1J = 0.239006 (cal = J*0.0239006)
#   Print(cal)


def main():
    # Introduction

    print("\nThis program will do a unit conversion for Joules to Calories")

    while True:
        #   Get input for Joules (0 to quit)
        j = float(input("\nWhat is the number of Joules?   (0 to quit)  "))

        # Test for exit condition (break if true)
        if j == 0:
            break

        #   Calculate conversion: 1J = 0.239006 (cal = J*0.239006)
        cal = j * 0.239

        #   Print(cal)
        print("\nThe conversion is", cal, "Calories for", j, "Joules")


main()
