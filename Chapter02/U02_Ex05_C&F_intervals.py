# U02_Ex05_C&F_intervals.py
#
# Author:
# Course: Coding for OOP
# Section: A3
#     Date: ${29} 5 ${2018}
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Table of F and C Temps
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#   This program will convert 0C through 100C in increments of ten, and then convert it into fahrenheit and vise versa
#
#
#
# Algorithm (pseudocode)
#   Run program and Explain
#   Require Input
#   Run Calculation
#   Print Output


def main():
    # Run Program and Explain
    print("This program will calculate 0C to 100C in increments of ten ")
    print("and then it will convert it into Fahrenheit on the left side")
    print("Then it will do the same with 0F to 100F and convert it into celsius on the right side")

    # Require Input
    run = input("Click ENTER to continue:    ")
    # Run Calculation
    for i in range(1):
                    # Calculate C to F
                    fahrenheit0 = (9 / 5) * 0 + 32

                    fahrenheit1 = (9 / 5) * 10 + 32

                    fahrenheit2 = (9 / 5) * 20 + 32

                    fahrenheit3 = (9 / 5) * 30 + 32

                    fahrenheit4 = (9 / 5) * 40 + 32

                    fahrenheit5 = (9 / 5) * 50 + 32

                    fahrenheit6 = (9 / 5) * 60 + 32

                    fahrenheit7 = (9 / 5) * 70 + 32

                    fahrenheit8 = (9 / 5) * 80 + 32

                    fahrenheit9 = (9 / 5) * 90 + 32

                    fahrenheit10 = (9 / 5) * 100 + 32

                    # Calculate F to C (c = (f-32) * 5/9)

                    celsius0 = (0 - 32) * 5/9

                    celsius1 = (10 - 32) * 5/9

                    celsius2 = (20 - 32) * 5/9

                    celsius3 = (30 - 32) * 5/9

                    celsius4 = (40 - 32) * 5/9

                    celsius5 = (50 - 32) * 5/9

                    celsius6 = (60 - 32) * 5/9

                    celsius7 = (70 - 32) * 5/9

                    celsius8 = (80 - 32) * 5/9

                    celsius9 = (90 - 32) * 5/9

                    celsius10 = (100 - 32) * 5/9
# Print Output
                    print("Here are your temperatures")
                    run = input("Celsius will appear on the right, and Fahrenheit will appear on the left. Click ENTER")
                    print(fahrenheit0, "(0c) F ", celsius0, "(0f) C ")
                    print(" ")
                    print(fahrenheit1, "(10c) F ", celsius1, "(10f) C ")
                    print(" ")
                    print(fahrenheit2, "(20c) F ", celsius2, "(20f) C ")
                    print(" ")
                    print(fahrenheit3, "(30c) F ", celsius3, "(30f) C ")
                    print(" ")
                    print(fahrenheit4, "(40c) F ", celsius4, "(40f) C ")
                    print(" ")
                    print(fahrenheit5, "(50c) F ", celsius5, "(50f) C ")
                    print(" ")
                    print(fahrenheit6, "(60c) F ", celsius6, "(60f) C ")
                    print(" ")
                    print(fahrenheit7, "(70c) F ", celsius7, "(70f) C ")
                    print(" ")
                    print(fahrenheit8, "(80c) F ", celsius8, "(80f) C ")
                    print(" ")
                    print(fahrenheit9, "(90c) F ", celsius9, "(90f) C ")
                    print(" ")
                    print(fahrenheit10, "(100c) F ", celsius10, "(100f) C ")
                    print(" ")


main()
