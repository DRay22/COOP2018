# U02_Ex04_MultipleTemps.py
#
# Author:
# Course: Coding for OOP
# Section: A3
#     Date: ${19} ${Sept} ${2018}
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Converting multiple temperatures
#     Source: Python Programming
#    Chapter: 2.2
#
# Program Description
#   This program will convert five temperatures and display a table containing both celsius(left) and fahrenheit(right)
#
#
#
# Algorithm (pseudocode)
#   Explain program
#   Require input 1 through 5 for each temperature (In fahrenheit)
#   Calculate using formula:
#       for i in range(1):
#         a1 = (a - 32) * 5/9
#         b1 = (b - 32) * 5/9
#         c1 = (c - 32) * 5/9
#         d1 = (d - 32) * 5/9
#         e1 = (e - 32) * 5/9
#   Display Output for each variable, and tell whether it is in celsius or fahrenheit
#         print(a1, "Celsius", a, "Fahrenheit")
#         print(b1, "Celsius", b, "Fahrenheit")
#         print(c1, "Celsius", c, "Fahrenheit")
#         print(d1, "Celsius", d, "Fahrenheit")
#         print(e1, "Celsius", e, "Fahrenheit")


def main():
    # Explain Program
    print("this program will convert five temperatures and display a table containing both celsius and fahrenheit")
    # Require input 1 through 5 for each temperature (In fahrenheit)
    a = eval(input("Enter the first temperature in fahrenheit  "))
    b = eval(input("Enter the second temperature in fahrenheit  "))
    c = eval(input("Enter the third temperature in fahrenheit  "))
    d = eval(input("Enter the fourth temperature in fahrenheit  "))
    e = eval(input("Enter the fifth temperature in fahrenheit  "))
    run = input("Press ENTER to continue    ")
    # Calculate
    for i in range(1):
        a1 = (a - 32) * 5/9
        b1 = (b - 32) * 5/9
        c1 = (c - 32) * 5/9
        d1 = (d - 32) * 5/9
        e1 = (e - 32) * 5/9
    # Output
        print(a1, "Celsius", a, "Fahrenheit")
        print(b1, "Celsius", b, "Fahrenheit")
        print(c1, "Celsius", c, "Fahrenheit")
        print(d1, "Celsius", d, "Fahrenheit")
        print(e1, "Celsius", e, "Fahrenheit")


main()
