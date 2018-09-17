# U02_Ex08_Compounding.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: ${29}  ${2018}
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Future Value with compounding
#     Source: Python Programming
#    Chapter: 2.2
#
# Program Description
#
#
#
#
# Algorithm (pseudocode)
#   Explain Program
#   Input for 3 values
#   calculate
#   Output


def main():

    print("This program calculates the future value")
    print("of a ten year investment")

    principal = eval(input("Enter the initial principal:  "))
    apr = eval(input("Enter the annual interest rate: (without percentage sign)  "))
    time_period = eval(input("What is the number of years that will be compounded:   "))

    for i in range(1):
        apr1 = apr/100
        principal = principal * (1 + apr1) ** time_period

    print("Than value is:", principal)


main()
