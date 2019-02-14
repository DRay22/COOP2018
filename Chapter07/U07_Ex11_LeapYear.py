# U07_Ex11_LeapYear.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 08 Feb 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Ex11 Leap Year
#   Source: Python Programming
#   Chapter: #07
#
# Program Description
#   This program will see if a year is a leap year
#
#
#
# Algorithm (pseudocode)
#   Func Input():
#       get Input
#       return input
#
#   Func LeapTest()
#       call Input()
#       if the year is a century year:
#           divide the year by 400
#           if type is int:
#               return "The year (Input) is a leap year"
#           else:
#               return "The year (Input) is not a leap year"
#       else:
#          divide year by 4
#          if the type is int:
#              return the year, (yearInput), is a leap year
#
#   Func Output():
#       Call LeapTest()
#       print LeapTest


def Input():
    Year = int(input("What is the year that you would like to test?       "))
    return Year

def LeapTest(year):
    yearMod = year % 100
    if yearMod == 0:
        yearDiv = year/400
        yearDivstr = str(yearDiv)
        yearFltSplt = yearDivstr.split('.')
        if yearFltSplt[1] == '0':
            return "The year {0}, is a leap year".format(year)
        else:
            return "The year {0}, is not a leap year".format(year)
    else:
        yearDiv = year/4
        yearDivstr = str(yearDiv)
        yearFltSplt = yearDivstr.split('.')
        if yearFltSplt[1] == '0':
            return "The year {0}, is a leap year".format(year)
        else:
            return "The year {0}, is not a leap year".format(year)


def Output():
    print("This program will take a year from the user, and see if it is a leap year or not")
    year = Input()
    YearFin = LeapTest(year)
    print(YearFin)

if __name__ == '__main__':
    Output()


'''
RESULTS:
========
LeapTest(1600)   -->       The year 1600, is a leap year |       The year 1600, is a leap year | [ Pass ]
LeapTest(2000)   -->       The year 2000, is a leap year |       The year 2000, is a leap year | [ Pass ]
LeapTest(2146)   -->   The year 2146, is not a leap year |   The year 2146, is not a leap year | [ Pass ]
LeapTest(2033)   -->   The year 2033, is not a leap year |   The year 2033, is not a leap year | [ Pass ]
========
'''