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
#   gradeChk(pos): (separate module)
#   Check if any of the grades fit these categories, then return 5-1 to select a letter grade from the list
#       if pos >= 90, return 5
#       if pos >= 80, return 4
#       if pos >= 70, return 3
#       if pos >= 60, return 2
#       if pos < 60 return 1
#   GradeConv = GradeList[Chk - 1]
#   Print "Your letter grade is {0}".format(GradeConv) for every returned value 1-5


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
    if GradeConv == 'F':
        GradeConv = 'an {0}'.format(GradeConv)
    if GradeConv == 'D':
        GradeConv = 'a {0}'.format(GradeConv)
    if GradeConv == 'C':
        GradeConv = 'a {0}'.format(GradeConv)
    if GradeConv == 'B':
        GradeConv = 'a {0}'.format(GradeConv)
    if GradeConv == 'A':
        GradeConv = 'an {0}'.format(GradeConv)
    print("Your letter grade is: {0}".format(GradeConv))


grades()
