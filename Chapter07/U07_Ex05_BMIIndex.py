# U07_Ex05_BMIIndex.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 06 Feb 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: BMI Index Ex05
#     Source: Python Programming
#    Chapter: #07
#
# Program Description
# This program will get the user's weight, and user's height (in inches) and then convert the amounts to a BMI,
# and then will tell if they are below, in, or above the healthy range
#
#
#
# Algorithm (pseudocode)
# Def Input():
#   get weight (in pounds)
#   get height (in inches)
#   return both values
#
# Def Calc():
#   call values from Input
#   Multiply weight by 720
#   Square height
#   divide weight by height
#   return value
#
# Def BMIConv():
#   call Calc Value
#   if Calc is less than 19
#       return number and status
#   if Calc is more than 19 and less than 25
#       return number and status
#   if Calc is more than 25:
#       return number and status
#
# Def Output():
#   call BMIConv()
#   split by "/" (for the and in the BMIConv return)
#   print output with formatting for number and status


def Input():
    # Get input for pounds and inches
    lbs = str(input("Weight: (In pounds)     "))
    inc = str(input("Height: (In inches)     "))

    # Return values
    return lbs, inc

def Calc(height, weight):
    height = float(height)
    weight = float(weight)
    # Multiply weight by 720
    weight720 = weight * 720

    # Square height
    heightSqr = height**2

    # Divide weight by height
    BMI = weight720/heightSqr
    return int(BMI)

def BMIConv():
    # Call Calculate Function
    CallInp = Input()
    height = CallInp[1]
    weight = CallInp[0]
    bmicall = Calc(height, weight)

    # Convert to float
    bmi = float(bmicall)

    # If statements for healthy range
    if bmi < 19.0:
        return int(bmi), "Below Healthy Range"
    if bmi >= 19.0:
        if bmi <= 25.0:
            return int(bmi), "In Healthy Range"
    else:
        if bmi > 25.0:
            return int(bmi), "Above Healthy Range"


def Output():
    # Introduce Program
    print("This program will get user input for weight and height, and then calculate the values into a BMI Chart. "
          "\nAfter calculating the values into a BMI Chart, the program will show the user the BMI Number, and if"
          "\nthe values are in the healthy range.")

    # Call/convert values to float
    BMIFin = BMIConv()
    if BMIFin == None:
        print("Input Error, please enter a valid weight and height")
    else:
        BMINum = BMIFin[0]
        BMINum = float(BMINum)
        BMIStat = BMIFin[1]
        print("BMI Number: {0:0.2f} | BMI Status:{1}".format(BMINum, BMIStat))



if __name__ == '__main__':
    Output()



'''
RESULTS:
========
Calc(72, 170)   -->   23 |   23 | [ Pass ]
Calc(72, 180)   -->   25 |   25 | [ Pass ]
Calc(72, 250)   -->   34 |   34 | [ Pass ]
========
'''
