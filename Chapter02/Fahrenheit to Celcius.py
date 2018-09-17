
# File: Fahreheit to Celsius converter.py
# A program to convert Fahrenheit to Celsius
#
# Algorithim:
# Step 1: Ask for input (F)
# Step 2: Calculate based on input
#       C = (F - 32) x 5/9
# Step 3 Display output (C)


def main():
    f = eval(input("What is the temperature in Fahrenheit?   "))
    for i in range(1):
        c = (f-32) * 5/9
        print("Here is the temperature in celsius:")
        print(c)


main()
