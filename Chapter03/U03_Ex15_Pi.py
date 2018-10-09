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
    # Receive input (n)
    n = int(input("How many terms are in the sequence?   "))
    AppPi = 0
    # Make a for loop with n
    for amt in range(1, n+1):
        AppPi = 4 / 2*n - 1
        if n % 2:
            AppPi + 4 / 2*n - 1
        else:
            AppPi - 4 / 2*n - 1
        AppPi = 4/1 - 4/3 + 4/5 - 4/7 + 4/(2*n - 1) * (-1)**(n-1)
        piabs = math.fabs(math.pi)
        Appabs = math.fabs(AppPi)
        sub = piabs - Appabs
        print(sub)


main()
