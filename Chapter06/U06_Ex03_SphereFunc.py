# U06_Ex03_SphereFunc.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 13 Jan 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Sphere 03
#     Source: Python Programming
#    Chapter: #06
#
# Program Description
#   This program will calculate the surface area and volume of a sphere, given the radius
#
#
#
# Algorithm (pseudocode)
#   Get input through func Input()
#       get input
#       return value of input
#
#   Calculate vol and area through func Calc()
#       radius = Input()
#       area = 4*math.pi*radius**2
#       vol = 4/3*math.pi*radius**3
#       return radius, vol, area
#
#   Print values using func Print()
#   ans = Calc()
#   print values using formatting ans[0], ans[1], ans[2]


import math


def Input():
    radius = eval(input("What is the radius of the sphere?   "))
    return radius


def Calc():
    radius = Input()
    area = 4*math.pi*radius**2
    vol = 4/3*math.pi*radius**3
    return radius, vol, area


def Print():
    ans = Calc()
    print("The sphere, with a radius of {0}, has a volume of {1}, and a surface area of {2}"
          .format(ans[0], ans[1], ans[2]))

Print()
