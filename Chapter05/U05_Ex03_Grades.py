# U05_Ex03_Grades.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 27 Nov 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Grades Exercise 3
#     Source: Python Programming
#    Chapter: #05
#
# Program Description
#   This program convert a user inputted grade to a letter grade
#
#
#
# Algorithm (pseudocode)
#   Introduce Program
#   Generate list [F, D, C, B, A]
#   Get an int value called grade
#   Chk = gradeChk(grade)
#   gradeChk(pos):
#       if pos >= 90, return 5
#       if pos >= 80, return 4
#       if pos >= 70, return 3
#       if pos >= 60, return 2
#       if pos < 60 return 1
#   GradeConv = GradeList[Chk - 1]
#   Print OYu letter grade is: GradeConv


def gradeChk(pos):
    if pos >= 90:
        return 5
    if pos >= 80:
        return 4
    if pos >= 70:
        return 3
    if pos >= 60:
        return 2
    if pos < 60:
        return 1


def grades():
    print("This program convert a user inputted grade to a letter grade")
    GradeList = ['F', 'D', 'C', 'B', 'A']
    grade = int(input("What grade would you like to convert  "))
    Chk = gradeChk(grade)
    GradeConv = GradeList[Chk - 1]
    print("Your letter grade is:", GradeConv)


grades()
