# U03_Ex15_Pi.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 26 Sept 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Approximating Pi Ex15
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#   This program will approximate pi
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   Define N to # of terms
#   Initialize ApproxPi to 0
#   Loop N times (i)
#   Add nextTerm to ApproxPI
#       nextTerm = If i%2 = 0 #even, else, subtract 4/2i-1 (use above AND below)
#   Find diff between math.pi and AppPi
#   Print results 

import math


def main():
    # Introduce program: "This program will approximate pi"
    print("This program will approximate pi")
    #   Define N to # of terms
    n = int(input("How many terms are in the sequence?   "))
    #   Initialize AppPi as 4 / 2 * n - 1
    AppPi = 0
    #   Loop N times (i)
    for amt in range(1, n+1):
        AppPi = AppPi + 4/(2*amt - 1) * (-1)**(amt-1)

    #   Find diff between math.pi and AppPi
    piabs = math.fabs(math.pi)
    Appabs = math.fabs(AppPi)
    sub = piabs - Appabs
    #   Print results
    print("Pi is:", piabs)
    print("The approximated pi is:", Appabs)
    print("The difference between in the approximation and Pi is:", sub)


main()
