# U02_Ex10_Kilo_to_Mile.py
#
# Author:
# Course: Coding for OOP
# Section: A3
#     Date: ${19} ${Sept} ${2018}
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Kilometers to miles
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
# This program converts Kilometers to Miles
#
#
#
# Algorith (pseudocode)
#   Explain purpose
#   Require input to define x
#   Calculate y = x*0.621371
#   Produce Output (y)


def main():
    # Explain Purpose
    print("This program is used to convert kilometers to miles")
    # Require Input to define x
    x = eval(input("What is the number of kilometers?"))
    # Calculate Input
    for i in range(1):
        y = x*0.621371
        # Produce Output
        print("The result of the conversion is:")
        print(y)


main()
