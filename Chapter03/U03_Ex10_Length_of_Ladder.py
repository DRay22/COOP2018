# U03_Ex10_Length_of_Ladder.py.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 30 sept 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Ex10 finding the length of a ladder
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#   This program will calculate the length of a ladder based off of user generated inputs
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   Get inputs Height and Degree
#   Define angle(Angle = math.pi/180*Degree)
#   Calculate using length = height/math.sin angle
#   print length

import math


def main():
    # Introduce program
    print("This program will calculate the length of a ladder based off of user generated inputs")
    #   Get inputs Height and Degree
    height = eval(input("How high is the ladder?   "))
    degree = eval(input("What degree is the ladder at?   "))
    #   Define angle(Angle = math.pi/180*Degree)
    angle = math.pi/180*degree
    #   Calculate using length = height/math.sin angle
    length = height/math.sin(angle)
    print("The length is", length,)


main()
