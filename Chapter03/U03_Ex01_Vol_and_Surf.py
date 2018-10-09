# U03_Ex01_Vol_and_Surf.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 25 sept 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Volume and Surface Area Ex01
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#   This program can calculate Volume and Surface area of a sphere from its radius, which is a user generated value
#
#
#
# Algorithm (pseudocode)
#   Introduce program "This program will..."
#   Input r = input(eval("what is the radius of the sphere?     "))
#   Calculate using formula and input for both surface area and volume:
#       V = 4/3*3.14*r**3
#       A = 4*3.14*r**2
#   print output "The volume of the sphere is", V,"and the surface area is", A,

import math


def main():
    # Introduce program "This program will display the surface area and volume of a sphere based off of it's radius"
    print("This program will display the surface area and volume of a sphere based off of it's radius")
    # Input r = input(eval("what is the radius of the sphere?      ")
    r = eval(input("What is the radius of the sphere?     "))
    # Calculate using formula and input for both surface area and volume
    input("Press ENTER to continue")
    v = 4/3*math.pi*r**3
    a = 4*math.pi*r**2
    # print output "The volume of the sphere is", V,"and the surface area is", A,
    print("The volume of the sphere is", v, "and the surface area is", a,)


main()
