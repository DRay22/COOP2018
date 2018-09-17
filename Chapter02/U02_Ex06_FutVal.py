# U02_Ex06_FutVal.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A3
#     Date: ${29}  ${2018}
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Future Value
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
#   Require three inputs
#   Calculate using formula
#   print output
#


def main():

    print("This program calculates the future value")
    print("of a ten year investment")

    principal = eval(input("Enter the initial principal:  "))
    apr = eval(input("Enter the annual interest rate: (without percentage sign)  "))
    length = eval(input("Over how many years is this investment?  "))

    for i in range(length):
        apr1 = apr/100
        principal = principal * (1 + apr1)

    print("Than value in", length, "years is:", principal)


main()
