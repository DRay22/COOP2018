# U02_Ex06_FutVal.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A3
#     Date: ${19} ${Sept} ${2018}
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Future Value
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#   This program can calculate the future value of a ten year investment
#
#
#
# Algorithm (pseudocode)
#   Print the program description "This program calculates the future value of a ten year investment"
#   Define principle input
#   Define apr input
#   Define length input
#   Calculate using formula:
#       Define apr1 (apr1 = apr/100)
#       Use formula: principal = principal * (1 + apr1)
#   Print output, showing both length and the principal
#


def main():
    #   Print the program description "This program calculates the future value of a ten year investment"
    print("This program calculates the future value")
    print("of a ten year investment")
    #   Define principle input
    principal = eval(input("Enter the initial principal:  "))
    #   Define apr input
    apr = eval(input("Enter the annual interest rate: (without percentage sign)  "))
    #   Define length input
    length = eval(input("Over how many years is this investment?  "))
    #   Calculate using formula:
    for i in range(length):
        apr1 = apr/100
        principal = principal * (1 + apr1)
    #   Print output, showing both length and the principal
    print("Than value in", length, "years is:", principal)


main()
