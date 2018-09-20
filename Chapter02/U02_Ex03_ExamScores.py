# U02_Ex03_ExamScores.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A3
#     Date: ${19} ${Sept} ${2018}
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Exam Scores
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#   This program will take three exam scores and average them.
#
#
#
# Algorithm (pseudocode)
#   Describe program "This program will average three exam scores"
#   Require three inputs a,b, and c (exam scores)
#   Calculate using equation: z = (a + b + c)/3
#   Print output (z)


def main():
    print("This program will average three exam scores")
    a = eval(input("enter the first exam score:   "))
    b = eval(input("enter the second exam score:   "))
    c = eval(input("enter the third exam score:   "))
    for i in range(1):
        z = (a + b + c)/3
        print("The average is", z)


main()
