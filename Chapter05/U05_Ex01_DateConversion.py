# U05_Ex01_DateConversion.py.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 26 Nov 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Date Conversion Exercise 1
#     Source: Python Programming
#    Chapter: #05
#
# Program Description
#   This program will convert a numerical date into a date displaying month as a string
#
# Algorithm
#   get the day, month, and year as numbers
#   Make first date using numbers
#   Make list of months, select moth with month number - 1
#   Make date2 using the month string
#   Print using string formatting

def main():
    # get the day month and year as numbers
    date = str(input("what is the date? please seperate with commas    "))
    dtsplit = date.split(',')
    day = dtsplit[1]
    month = dtsplit[0]
    year = dtsplit[2]

    # Get numerical date
    date1 = str(month)+"/"+str(day)+"/"+str(year)

    # Get string date
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    month = int(month)
    monthStr = months[month-1]
    date2 = monthStr+" " + str(day) + ", " + str(year)

    print("The date is {0} or {1}.".format(date1, date2))

main()
