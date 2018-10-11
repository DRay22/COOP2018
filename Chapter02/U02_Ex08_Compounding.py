# U02_Ex08_Compounding.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: ${19} ${Sept} ${2018}
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Ex08 Future Value with compounding
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
# This program calculates the future value with a interest rate quarterly, over a specified amount of time
#
#
#
# Algorithm (pseudocode)
#   Print the program description "This program calculates the future value with a interest rate quarterly"
#   "Over a specified amount of time"
#   Define principle input
#   Define rate input
#   Define periods input
#   Calculate using formula:
#       Define apr1 (apr1 = apr/100)
#       Divide rate/periods and add to principal
#   Print output, showing only the principle


def main():
    #   Print the program description "This program calculates the future value with a interest rate quarterly"
    print("This program calculates the future value with a interest rate quarterly")
    #   "Over a specified amount of time"
    print("Over a specified amount of time")

    #   Define principle input
    principal = eval(input("Enter the initial principal:  "))
    #   Define apr input
    rate = eval(input("Enter the annual interest rate: (without percentage sign)  "))
    #   Define time_period input (compounding)
    periods = eval(input("How many times will the interest be compounded in one year?   "))
    #   Calculate using formula:
    for i in range(10 * periods):
        apr1 = rate/100
        # Divide rate/periods and add to principal
        principal1 = (rate/periods) + principal
    #   Print output, showing only the principle

    print("The value is:", principal1, "after 10 years")


main()
