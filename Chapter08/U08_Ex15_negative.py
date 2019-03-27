# U08_Ex15_negative.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 27 Mar 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Negative 15
#     Source: Python Programming
#    Chapter: #08
#
# Program Description
#   This program will convert an image to negative
#
#
#
# Algorithm (pseudocode)
#   main():
#       introduce program
#       get filename
#       use GrpConv
#       display new image


#   GrpConv():
#       make graphics window (400x400)
#       make image using anchor point 200, 200 (center) and filename
#       get width and length of image
#       for i in range (width)
#           for j in range (length)
#               change colors to negative
#      once done give option to save image
#       user can change name of file
#       save(filename)


from graphics import *


def GrpConv(filename):
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
            colorSel0 = colorSel[0]
            colorSel1 = colorSel[1]
            colorSel2 = colorSel[2]
            img.setPixel(w, h, color_rgb(255-colorSel0, 255-colorSel1, 255-colorSel2))
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
    print("This program will change an image to negative")
    fileInput = str(input("Please enter the name of a file that you want to change:   "))
    NewIMG = GrpConv(fileInput)

main()