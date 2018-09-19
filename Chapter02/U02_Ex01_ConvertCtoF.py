# U02_Ex01_ConvertCtoF.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: ${19} ${9} ${2018}
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Converting Celsius to Fahrenheit (Exercise 1)
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#   This program converts Celsius to Fahrenheit
#
# Algorithm (pseudocode)
# Input: Number of degrees Celsius
# Get C from user and assign to Celsius
# Calculate: (9/5) * C + 32 and assign to fahrenheit
# print fahrenheit

def main():
    # some code
    # Input: Number of degrees Celsius
    print("This program converts Celsius to Fahrenheit")
    # Get C from user and assign to Celsius
    celsius = eval(input("Enter Celsius to convert:"))

    # Calculate: (9/5) * C + 32 and assign to fahrenheit
    fahrenheit = (9/5) * celsius + 32
    # print fahrenheit
    print("Celsius is equivalent to", fahrenheit, "Fahrenheit")


main()
