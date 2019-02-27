# U07_Ex13_DayConv.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 14 Feb 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Day Conversion 13
#     Source: Python Programming
#    Chapter: #07
#
# Program Description
#   This program will convert a date to a number of days in a year.
#
#
#
# Algorithm (pseudocode)
#   Input():
#       get date from user (separate by "/")
#       return date
#
#   Conv(date):
#       use functions or code from Ex12 to check if it is a valid date
#       use functions or code from Ex11 to check if the date is a leap year:
#       if it is:
#           use code below to see if it after february
#           if it is:
#               add 1 to final date
#       if it is:
#           check to see if it is under february:
#               if it is:
#                   date = 31(month - 1) + day
#               if it is not:
#                   subtract (4(month) + 23)//10 from previous statement
#       return values after every "if" statement
#
#   Output():
#       Introduce program
#       call Input
#       define conv function with date
#       print output

from Chapter07 import U07_Ex12_ValidDate, U07_Ex11_LeapYear


def Input():
    dateIn = str(input("What is the date? Formatting Example: 5/5/2015   "))
    return dateIn

def dateConv(dateMon, dateDay, dateYear):
    year = "fill"
    print("Month:", dateMon)
    print("Day:", dateDay)
    print("Year:", dateYear)

    ValidCheck = U07_Ex12_ValidDate.dateCheck(dateMon, dateDay)
    LeapCheck = U07_Ex11_LeapYear.LeapTest(dateYear)
    if ValidCheck == 'valid':
        if LeapCheck == "The year {0}, is a leap year".format(year):
            if dateMon < 2:
                date = 31 * (dateMon - 1) + dateDay
                print("Date Final:", date)
                return date
            if dateMon >= 2:
                date = 31 * (dateMon - 1) + dateDay
                print("Date Final:", date)
                date = date + 1
                print("Date Final (With Feb Calc):", date)
                return date
        else:
            if dateMon < 2:
                date = 31 * (dateMon - 1) + dateDay
                print("Date Final:", date)
                return date
            if dateMon >= 2:
                date = 31 * (dateMon - 1) + dateDay
                print("Date Final:", date)
                date = date - (4 * (dateMon) + 23)//10
                print("Date Final (With Feb Calc):", date)
                return date
    else:
        return "ERROR: The date is not valid"

def Output():
    print("This program  will convert a date to see which day of the year that day is.")
    date = Input()
    dateSplt = date.split("/")
    dateMon = dateSplt[0]
    dateDay = dateSplt[1]
    dateYear = dateSplt[2]
    dateDay = int(dateDay)
    dateMon = int(dateMon)
    dateYear = int(dateYear)
    dateOut = dateConv(dateMon, dateDay, dateYear)
    if dateOut == "ERROR: Date is not valid":
        print("The date is not valid. The program will run again, please enter a valid date.")
        print("Running again:\n")
        Output()
    else:
        print("The number of days that the date is equivalent to is {0}".format(dateOut))


if __name__ == '__main__':
    Output()


"""
RESULTS:
========
dateConv(1,27,2004)   -->   27 |   27 | [ Pass ]
dateConv(1,22,2004)   -->   22 |   22 | [ Pass ]
dateConv(1,1,2004)    -->    1 |    1 | [ Pass ]
========
"""