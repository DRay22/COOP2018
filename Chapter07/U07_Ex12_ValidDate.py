# U07_Ex12_ValidDate.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 08 Feb 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Valid Date 12
#     Source: Python Programming
#    Chapter: #07
#
# Program Description
#   this program will check a date and see if it is valid
#
#
#
# Algorithm (pseudocode)
#   Func Input():
#       get input for date (str seperated by "/")
#       return value
#
#   Func Check(date1, date2, date3):
#       if date1 is 1:
#           if date2 > 31:
#               return false
#           else:
#               return true
#
#       if date1 is 2:
#           if date2 > 28:
#               return false
#           else:
#               return true
#
#       if date1 is 3:
#           if date2 > 31:
#               return false
#           else:
#               return true
#
#       if date is 4:
#           if date > 30:
#               return false
#           else:
#               return true
#
#       And so on...
#
#   Func Output():
#       Call input and split by /
#       def each split
#       call check(date1, date2, date3)
#       print output

from Chapter07.U07_Ex11_LeapYear import LeapTest


def Input():
    Dateinit = str(input("What is the date that you would like to check?   (please separate by slashes)   "))
    return Dateinit

def dateCheck(date1, date2, date3):
    date2 = int(date2)
    date1 = int(date1)
    date3 = int(date3)
    YearLeapTest = LeapTest(date3)


    if date1 == 1:
        if date2 > 31:
            return 'false'
        else:
            return 'valid'

    if date1 == 2:
        if YearLeapTest == "The year {0}, is a leap year".format(date3):
            if date2 > 29:
                return 'false'
            elif date2 <= 29:
                return 'valid'
        elif date2 > 28:
            return 'false'
        else:
            return 'valid'
        LeapTest(date3)



    if date1 == 3:
        if date2 > 31:
            return 'false'
        else:
            return 'valid'

    if date1 == 4:
        if date2 > 30:
            return 'false'
        else:
            return 'valid'

    if date1 == 5:
        if date2 > 31:
            return 'false'
        else:
            return 'valid'

    if date1 == 6:
        if date2 > 30:
            return 'false'
        else:
            return 'valid'

    if date1 == 7:
        if date2 > 31:
            return 'false'
        else:
            return 'valid'

    if date1 == 8:
        if date2 > 31:
            return 'false'
        else:
            return 'valid'

    if date1 == 9:
        if date2 > 30:
            return 'false'
        else:
            return 'valid'

    if date1 == 10:
        if date2 > 31:
            return 'false'
        else:
            return 'valid'

    if date1 == 11:
        if date2 > 30:
            return 'false'
        else:
            return 'valid'

    if date1 == 12:
        if date2 > 31:
            return 'false'
        elif date2 < 31:
            return 'valid'
    if date1 > 12:
        return 'false'

def Output():
    print("This program will check if a user submitted date is valid   ")
    date = Input()
    dateSpl = date.split("/")
    date1 = dateSpl[0]
    date2 = dateSpl[1]
    date3 = dateSpl[2]
    DateCheck = dateCheck(date1, date2, date3)
    print("\nThe date, {0}, is a {1} date".format(date, DateCheck))


if __name__ == '__main__':
    Output()


'''
RESULTS:
========
dateCheck(2, 15)    -->   valid |   valid | [ Pass ]
dateCheck(9, 31)    -->   false |   false | [ Pass ]
dateCheck(13, 31)   -->   false |   false | [ Pass ]
dateCheck(1, 27)    -->   valid |   valid | [ Pass ]
========
'''