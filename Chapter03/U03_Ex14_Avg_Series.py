# U03_Ex14_Avg_Series.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 26 Sept 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Averaging a series of numbers Ex14
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#   This program will average a series of user generated numbers and user generated amounts of numbers
#
#
#
# Algorithm (pseudocode)
#  Introduce program: This program will average a series of user generated numbers and user generated amounts of numbers
#  Ask how many numbers are in the group: define as i
#  Make for loop with i
#  Ask for input (repeating based on i)
#  calculate by adding input values and divide by i, define as end
#  print output (end/i)


def main():
    # Introduce program: This program will average a series of user generated numbers and user generated amounts of...
    print("This program will average a series of user generated numbers with a user generated amounts of numbers")
    #  Ask how many numbers are in the group: define as i
    i = eval(input("How many numbers are in this group? (2 or above)   "))
    sum = 0
    #  Make for loop with i
    for amount in range(i):
        #  Ask for input (repeating based on i)
        n = eval(input("Please enter a value:   "))
        #  calculate by adding input values, define as end
        end = sum + n
    #  print output (end/i)
    print(end / i)


main()
