# U03_Ex11_natural_numbers.py.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 30 Sept 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Ex12 cubes of natural number sums
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
# Introduction: This program will find the sum of cubed natural numbers
#
#
#
#
# Algorithm (pseudocode)
# Introduce program
# Get repetition number
# Define x as 0
# For loop in range 1, n + 1
# Equation for sumnat
# Print sumnat**3


def main():
    # Introduce program
    print("This program will find the sum of cubed natural numbers")
    # Get repetition number, define as rep
    n = eval(input("How many numbers would you like to sum?  "))
    # Define sumnat as 0
    sumnat = 0
    # For loop in range 1, n + 1
    for x in range(1, n + 1):
        # Equation for sumnat
        sumnat = sumnat + x**3
        # Print sumnat
    print("the sum of the natural numbers is", sumnat)

main()
