# U05_Ex14_FileWordCount.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 17 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Word Count 14
#     Source: Python Programming
#    Chapter: #05
#
# Program Description
#   This program will read a file and count the words in it
#
#
#
# Algorithm (pseudocode)
#   Get file name, make variable filename
#   Read file, make variable file
#   make variable called phr, equal to file.read
#   Split phr by every space (" ")
#   initialize wordcount as 0
#   make loop for word in phrSplit
#       make wordcount equal to wordcount + 1
#   print output


def main():
    print("This program will ocunt the amount of wirds in a file")
    filename = input("What is the file name?   ")
    file = open(filename, 'r')
    phr = file.read()
    phrSplit = phr.split(" ")
    phrSplit1 = phr.split("\n")
    wordCount = 0
    newCount = 0
    for word in phrSplit:
        wordCount = wordCount + 1
    for word in phrSplit1:
        newCount = newCount + 1
    print("There are {0:^} words in the file".format(wordCount + newCount))


main()
