# U02_Ex08_Compounding.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: ${19} ${Sept} ${2018}
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Future Value with compounding
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
# This program calculates the future value with a interest rate, over a specified amount of time
#
#
#
# Algorithm (pseudocode)
#   Print the program description "This program calculates the future value with a interest rate"
#   "Over a specified amount of time"
#   Define principle input
#   Define apr input
#   Define time_period input (compounding)
#   Calculate using formula:
#       Define apr1 (apr1 = apr/100)
#       Use formula: principal = principal * (1 + apr1) ** time_period
#   Print output, showing only the principle


def main():
    #   Print the program description "This program calculates the future value with a interest rate"
    print("This program calculates the future value with a interest rate")
    #   "Over a specified amount of time"
    print("Over a specified amount of time")

    #   Define principle input
    principal = eval(input("Enter the initial principal:  "))
    #   Define apr input
    apr = eval(input("Enter the annual interest rate: (without percentage sign)  "))
    #   Define time_period input (compounding)
    time_period = eval(input("What is the number of years that will be compounded:   "))
    #   Calculate using formula:
    for i in range(1):
        apr1 = apr/100
        principal = principal * (1 + apr1) ** time_period
    #   Print output, showing only the principle
    print("Than value is:", principal)


main()
