# U06_Ex04_Cubes.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 14 Jan 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Cubes 04
#     Source: Python Programming
#    Chapter: #06
#
# Program Description
# This program will cube the sum of natural numbers
#
#
#
# Algorithm (pseudocode)
#   Func Input():
#       get nat for how many numbers the user wants to sum
#       return nat
#
#   Func SumNatural():
#       call Input as n
#       initialize sumnat as 0
#       make loop for range(1, n + 1)
#           sum nat = sumnat + i**3
#       print output of sumnat


def Input():
    nat = eval(input("How many numbers would you like to sum?     "))
    return nat

def SumNatural():
    n = Input()
    sumnat = 0
    for i in range(1, n + 1):
        sumnat = sumnat + i**3
    print("The sum of the natural numbers is {0}".format(sumnat))

SumNatural()
