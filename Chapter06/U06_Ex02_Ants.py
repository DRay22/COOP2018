# U06_Ex02_Ants.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: 13 Jan 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: #
#
# Program Description
#   This program will print the lyrics to the ants go marching
#
#
#
# Algorithm (pseudocode)
#   Each function with a string returns value, and Func Sign() prints them
#   March1:
#       'The ants go marching one by one, hurrah! hurrah!'
#
#   L1:
#       'the little one stops to'
#
#   L12:
#       'suck his thumb/tie his shoe'       # Split by '/'
#
#   rain:
#       'And they all go marching down...\nIn the ground...\nTo get out....\nOf the rain\nBoom! Boom! Boom!'
#
#   March2:
#       'The and go marching two by two, hurrah! hurrah!'
#
#   Sing:
#   L12 = L12()         #Define as func
#   L12 = L12.split('/')    #Split
#   print statement:
#   print ("{0}\n{0}\n{1} {2}\n{3}\n{4}\n{4}\n{1} {5}\n{3}".format(March1(), L1(), l12[1], rain(), March2(), l12[1]))


def March1():
    return 'The ants go marching one by one, hurrah! hurrah!'

def L1():
    return 'the little one stops to'

def L12():
    return 'suck his thumb/tie his shoe'

def rain():
    return 'And they all go marching down...\nIn the ground...\nTo get out....\nOf the rain\nBoom! Boom! Boom!'

def March2():
    return 'The and go marching two by two, hurrah! hurrah!'

def Sing():
    l12 = L12()
    l12 = l12.split('/')

    print("{0}\n{0}\n{1} {2}\n{3}\n{4}\n{4}\n{1} {5}\n{3}".format(March1(), L1(), l12[1], rain(), March2(), l12[1]))

Sing()
