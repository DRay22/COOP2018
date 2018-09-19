# U02_Ex09_FtoC.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A3
#     Date: ${19} ${Sept} ${2018}
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Fahrenheit to Celsius
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#   This program is used to convert Fahrenheit to Celsius.
#
#
#
# Algorithm (pseudocode)
#   Require input (f)
#   Calculate using conversion equation (c = (f-32) * 5/9)
#   Print output description ("Here is the temperature in celsius:")
#   Print output (c)


def main():
    # Require Input
    f = eval(input("What is the temperature in Fahrenheit?   "))
    # Calculate Input
    for i in range(1):
        c = (f-32) * 5/9
        # Produce Output
        # Print output description
        print("Here is the temperature in celsius:")
        # Print output
        print(c)


main()
