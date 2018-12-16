# U05_Ex12_Futval.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 06 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Future Value 12
#     Source: Python Programming
#    Chapter: #05
#
# Program Description
#   This program will calculate the future value of an investment
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   get principal from user
#   get apr from user
#   get length (time period) from user
#   initialize year1 as 0 (used for accumulator)
#   for i in range(length):
#       divide apr by 100 to get it as a decimal
#       principal = principal * apr + 1
#       make variable called yeardisp (to display year) and make it equal to year1 + 1
#       make year 1 equal to yeardisp
#       print output with string formatting. (Year: {0} | Value: {1:.2f}".format(yeardisp, principal))


def main():
    print("This program calculates the future value")
    print("of a ten year investment")
    principal = eval(input("Enter the initial principal:  "))
    apr = eval(input("Enter the annual interest rate: (without percentage sign)  "))
    length = eval(input("Over how many years is this investment?  "))
    year1 = 0
    for i in range(length):
        apr1 = apr/100
        principal = principal * (1 + apr1)
        yeardisp = year1 + 1
        year1 = yeardisp
        print("Year: {0} | Value: {1:.2f}".format(yeardisp, principal))


main()
