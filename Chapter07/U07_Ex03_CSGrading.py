# U07_Ex03_CSGrading.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 04 Feb 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: CS Grading 3
#     Source: Python Programming
#    Chapter: #07
#
# Program Description
#   This program will convert a number grade to a letter grade
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   Func Input():
#       get input for number of grades to convert
#       get input for each grade
#
#   Func Conv():
#       for i in range (rep)
#           if grade >= 90:
#               return 5
#           if grade >= 80 and <= 89:
#               return 4
#           if grade >= 70 and <= 79:
#               return 3
#           if grade >= 60 and >= 69:
#               return 2
#           if grade >= 60:
#               return 1
#
#   Func ConvP2():
#       call Conv
#       make list of 5 letters (F, D, C, B, A)
#       use Conv as selector for list
#       return letter grade in form of a string
#
#   Func Output():
#       call Conv
#       print Letter grade with formatting


def Input():
    grades = int(input("What are the grades you would like to convert?  "))
    return grades


def Conv(grade):
    if grade >= 90:
        return 4
    elif grade >= 80:
        return 3
    elif grade >= 70:
        return 2
    elif grade >= 60:
        return 1
    elif grade < 60:
        return 0
    else:
        return "ERROR, Grade is out of range"

def ConvP2():
    grade = Input()
    gradeConv = Conv(grade)
    if gradeConv == type(str):
        return "Grade is out of range, please run program again and enter a grade less than or equal to 100"
    GradeList = ["F", "D", "C", "B", "A"]
    GradeConvP2 = GradeList[gradeConv]
    return GradeConvP2

def Output():
    gradeFin = ConvP2()
    print("The converted grade is a(n) {0}".format(gradeFin))

if __name__ == '__main__':
    Output()


# Test Code Results

'''
RESULTS:
========
Conv(0)     -->   0 |   0 | [ Pass ]
Conv(59)    -->   0 |   0 | [ Pass ]
Conv(60)    -->   1 |   1 | [ Pass ]
Conv(69)    -->   1 |   1 | [ Pass ]
Conv(70)    -->   2 |   2 | [ Pass ]
Conv(79)    -->   2 |   2 | [ Pass ]
Conv(80)    -->   3 |   3 | [ Pass ]
Conv(89)    -->   3 |   3 | [ Pass ]
Conv(90)    -->   4 |   4 | [ Pass ]
Conv(99)    -->   4 |   4 | [ Pass ]
Conv(100)   -->   4 |   4 | [ Pass ]
Conv(110)   -->   4 |   4 | [ Pass ]
========
'''
