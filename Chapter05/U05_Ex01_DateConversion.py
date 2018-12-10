# U05_Ex01_DateConversion.py.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 26 Nov 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: #05
#
# Program Description
#   This program will convert a numerical date into a date displaying month in an abbreviated form
#
#
#
# Algorithm (pseudocode)
#   Introduce program
#   Make list for month
#   Make list for days
#   Get input as int in form of dd/mm/yy (seperate for input for each (day, month, year)
#   Make dateConv1, printing all the numbers in a list as strings
#   Find month from list using input of month as a position, make variable name monthConv(string)
#   make variable called yearConv, where it takes the last two numbers of the year input
#   make variable called dateConv2, where it lists all the Conv variables
#   Print dayConv1 and dayConv2


def main():
    #   Introduce program
    print("This program will convert a numerical date into a date displaying month in a word format and will display "
          "both")

    #   Make list for month
    monthlist = ["January", "February", "March", "April", "May", "June", "July", "August",
                 "September", "October", "November", "December"]

    #   Make list for days
    daylist = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth",
               "Eleventh", "Twelfth", "Thirteenth", "Fourteenth", "Fifteenth", "Sixteenth", "Seventeenth",
               "Eighteenth", "Nineteenth", "Twentieth", "Twenty First", "Twenty Second", "Twenty Third",
               "Twenty Fourth", "Twenty Fifth", "Twenty Sixth", "Twenty Seventh", "Twenty Eighth",
               "Twenty Ninth", "Thirtieth", "Thirty First"]
    month = int(input("What is the number of the month?   "))
    day = int(input("What is the number of the day?    "))
    year = input("What year is it?    ")
    DateConv1 = [str(month), str(day), str(year)]
    yearConv = year[2:4]
    monthConv = monthlist[month - 1]
    dayConv = daylist[day - 1]
    DateConv2 = [monthConv + ',' + dayConv+',' + yearConv]
    print("The date is:", DateConv1, "or", DateConv2)


main()

