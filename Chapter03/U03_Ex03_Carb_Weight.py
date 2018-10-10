# U03_Ex03_Carb_Weight.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 25 sept 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Calculating the Weight of a Carbohydrate Ex03
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
#   This program will calculate the molecular weight of a Carbohydrate based on the number of H, C and O inside
#
#
#
# Algorithm (pseudocode)
#   Introduce program "This program will..."
#   Input for H, C and O "Enter the number of Hydrogen atoms in the molecule   "
#   Calculate using formula (Hw=H*1.00794, Cw=C*12.0107, and  Ow=O*15.99940)
#   Calculate total weight Wtot=Hw+Cw+Ow
#   print output ("The total weight is", W,)
#   print ("The hydrogen weight is", Hw,)
#   print ("the carbon weight is", Cw,)
#   print ("The oxygen weight is", Ow,)


def main():
    # Introduce Program "This program will..."
    print("This program will calculate the weight of a carbohydrate molecule based off of the weight of")
    print("Hydrogen, Carbon, and Oxygen atoms inside of it")
    # Input for H, C, and O "Enter the number of Hydrogen atoms in the Molecule   "
    h = eval(input("Enter the number of Hydrogen atoms in the Molecule   "))
    # Input for H, C, and O "Enter the number of Carbon atoms in the Molecule   "
    c = eval(input("Enter the number of Carbon atoms in the Molecule    "))
    # Input for H, C, and O "Enter the number of Oxygen atoms in the Molecule   "
    o = eval(input("Enter the number of Oxygen atoms in the Molecule    "))
    hw = h*1.00794
    cw = c*12.0107
    ow = o*15.9994
    # Calculate Total Weight Wtot = Hw + Cw + Ow
    w = hw + cw + ow
    # Print output ("The total weight is", w,)
    print("The total weight is", w,)
    # print ("The hydrogen weight is", Hw,)
    print("The hydrogen weight is", hw,)
    # print ("the carbon weight is", Cw,)
    print("The Carbon weight is", cw,)
    # print ("the oxygen weight is", Ow,)
    print("The Oxygen weight is", ow,)


main()
