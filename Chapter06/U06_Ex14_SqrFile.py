# U06_Ex14_SqrFile.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: 18 Jan 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: #
#
# Program Description
#
#
#
#
# Algorithm (pseudocode)
#   Def Filename:
#       get file name from useer
#       return file name
#
#   def Open:
#       call Filename as file
#       open file, variable fileop
#       return fileop
#
#   def Calc():
#       call file open
#       read file lines
#       initialize rep as 4
#       print filenum
#       initialize sel as 0
#       make loop for rep
#           read file line
#           square contents of line
#           add to selector
#           make if statements to keep sel in range of file
#           get sum of lines
#           print output

def FileName():
    filen = str(input("What is the name of the file that you would like to read?   "))
    return filen

def Open():
    file = FileName()
    fileop = open(file, 'r')
    return fileop

def Calc():
    filenum = Open()
    filenum = filenum.readlines()
    rep = 4
    sel = 0
    linesum = 0
    for i in range(rep):
        fileread = int(filenum[sel])
        print(fileread)
        lineSqr = fileread**2
        line = lineSqr
        if sel < 4:
            sel = sel + 1
        if sel > 4:
            break
        linesum = linesum + line
    print("The square of the sum of the numbers is {0}".format(linesum))


Calc()
