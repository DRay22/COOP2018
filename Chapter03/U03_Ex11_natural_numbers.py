# U03_Ex11_natural_numbers.py.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: 30 Sept 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Sum of Natural Numbers Ex11
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
# Introduction: This program will find the sum N natural numbers, where n is a user generated value
#
#
#
# Algorithm (pseudocode)
# Introduce program
# Get repetition number
# Define x as 0
# For loop in range 1, n + 1
# Equation for sumnat
# Print sumnat


def main():
    # Introduce program
    print("This program will find the sum N natural numbers, where n is a user generated value")
    # Get repetition number, define as rep
    n = eval(input("How many numbers would you like to sum?  "))
    # Define x as 0
    x = 0
    # Define sumnat as 0
    sumnat = 0
    # For loop in range 1, n + 1
    for x in range(1, n + 1):
        # Equation for sumnat
        sumnat = sumnat + x
        # Print sumnat
    print("the sum of the natural numbers is", sumnat)


main()
