# U08_Ex14_color.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 26 Mar 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: GreyScale 14
#     Source: Python Programming
#    Chapter: #08
#
# Program Description
#   This program will change the color of an image to greyscale
#
#
#
# Algorithm (pseudocode)
#   main():
#       introduce program
#       get input for filename
#       run graphics and color change functions
#       save new image with user-inputted file name


#   GrpColor():
#       make graphics window (400x400)
#       make image using anchor point 200, 200 (center) and filename
#       get width and length of image
#       for i in range (width)
#           for j in range (length)
#               change colors to grey scale
#      once done give option to save image
#       user can change name of file
#       save(filename)
from graphics import *



def GrpColor(filename):
    win = GraphWin("Image Manipulator", 400, 400)
    img = Image(Point(200, 200), filename)
    img.draw(win)
    input("Display Image?  Press ENTER to continue")
    imgWide = img.getWidth()
    imgHigh = img.getHeight()
    for w in range(imgWide):
        for h in range(imgHigh):
            colorSel = img.getPixel(w, h)
            # print("\nOriginal:", colorSel)
            gray = int(round(0.21 * colorSel[0] + 0.72 * colorSel[1] + 0.07 * colorSel[2]))
            img.setPixel(w, h, color_rgb(gray, gray, gray))
            # print("Changed:", colorSel)
    img.undraw()
    img.draw(win)
    yesno = input("Do you want to save image?  (yes/no)   ")
    if yesno == "yes":
        NewFileName = str(input("What would you like the file to be called?   "))
        img.save(NewFileName+'.ppm')
    if yesno == "no":
        print("Stopping processes...")

def main():
    print("This program will change an image to greyscale")
    fileInput = str(input("Please enter the name of a file that you want to change:   "))
    NewIMG = GrpColor(fileInput)

main()
