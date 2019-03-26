# U08_Ex08_GCD.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 21 Mar 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: GCD 8
#     Source: Python Programming
#    Chapter: #08
#
# Program Description
# This program will find the greatest common divisor between two numbers, n and m
#
#
#
# Algorithm (pseudocode)
#   main():
#       print introduction
#       get n and m values
#       call calculating function
#       print GCD


#   CalcGCD():
#       while m != 0:
#           n, m = m, n%m
#       return n

global n
global m


def CalcGCD(Nput, Mput):
    # Define variables
    global n
    global m
    n = Nput
    m = Mput

    # Calculate GCD
    while m !=0:
        n, m = m, (n%m)

    # Return GCD
    return n

def main():
    # Introduce program
    print("This program will find the greatest common divisor between two numbers")

    # Get input
    Nput = int(input("Please enter the first value:   "))
    Mput = int(input("Please enter the second value:   "))

    # Call calculator function
    GCD = CalcGCD(Nput, Mput)

    # print output
    print("Your GCD is: {0}".format(GCD))

main()
