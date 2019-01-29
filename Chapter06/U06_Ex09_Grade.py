# U06_Ex09_Grade.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 17  2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Grade 09
#     Source: Python Programming
#    Chapter: #06
#
# Program Description
# This program will convert a numerical grade into a letter grade using modular coding
#
#
#
# Algorithm (pseudocode)
#   Func Input():
#       get input as varibal grade
#       return
#
#   Func gradeChk(): (Make if statements for selecting a letter from a list based off of grade range)
#       grade = Input()
#       if grade >= 90:
#           return 5
#       if grade >= 80:
#           return 4
#       if grade >= 70:
#           return 3
#       if grade >= 60:
#           return 2
#       if grade < 60:
#           return 1
#
#   Func list():
#       list of letter grades starting with F
#       call gradeChk
#       make variable for selecting grade from list
#       make print statements for every grade
#
#
#   Func Print():
#       call list
#       print output


def Input():
    grade = int(input("What is the grade that you would like to convert?   "))
    return grade



def gradeChk():
    grade = Input()
    if grade >= 90:
        return 5
    if grade >= 80:
        return 4
    if grade >= 70:
        return 3
    if grade >= 60:
        return 2
    if grade < 60:
        return 1


def list():
    GradeList = ['F', 'D', 'C', 'B', 'A']
    Chk = gradeChk()
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
    return GradeConv


def Print():
    grade = list()
    print("Your letter grade is {0}".format(grade))


Print()
