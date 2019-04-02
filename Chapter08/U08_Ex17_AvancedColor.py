# U08_Ex17_AvancedColor.py
#
# Author:
# Course: Coding for OOP
# Section: A2
#     Date: 29 Mar 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: Name and Number
#     Source: Python Programming
#    Chapter: #
#
# Program Description
#   This program will manipulate an image
#
#
#
# Algorithm (pseudocode)
#   main():
#       Ask for image file
#       Call graphics function

#   GraphMain():
#       call graphics window(600, 600)
#       draw image from image file
#       create rectangle(s) for image manipulation options
#       wait for mouse click
#       if in rectangle range perform task

#   GreyScale():
#       (code from greyscale program)

#   Negative():
#       (code from negative program)

#   Back():
#       draw original image

#   CustomOne():
#       Make Blue value the red value
#       Make Red value the green value
#       Make Green value the blue value

#   CustomTwo():
#       randomize color values

from graphics import *

from random import *

global darken

global text2

def GraphMain(fileN):
    filename = fileN
    win = GraphWin("Image Manipulation", 600, 600)
    win.setCoords(0, 0, 600, 600)

    # Draw Image
    img = Image(Point(200, 300), fileN)
    img.draw(win)

    # Separating Rectangles:
    thelongone = Rectangle(Point(430, 0), Point(431, 600))
    thelongone.setOutline("Black")
    thelongone.setFill("Black")
    thelongone.draw(win)
    theflatone = Rectangle(Point(430, 515), Point(600, 516))
    theflatone.setOutline("Black")
    theflatone.setFill("Black")
    theflatone.draw(win)

    # Draw Buttons and Text:

# BUTTON NOTES:
#   Starting X value is 450
#   Starting Y value is 560 - 30 - (10 * amount of buttons)
#   Ending X value is 590
#   Ending Y value is 590 - 30 - (10 * amount of buttons)

# TEXT NOTES:
#   Starting X value is ALWAYS 490
#   Starting Y value is button Y1 + 13
#   Ending X value is button X2 - 10
#   Ending Y is button Y2 - 10


    # Data/ File/ Process Manipulation:

    QuitButton = QuitGraphic(win)
    # Points of Button: (450, 560) and (590, 590)
    # Points of Text: (490, 573) and (580, 580)

    SaveButton = SaveGraphic(win)
    # Points of Button: (450, 520) and (590, 550)
    # Points of Text: (490, 533) and (580, 540)




    # Image Manipulation:

    # BUTTON NOTES:
    #   Starting X value is 450
    #   Starting Y value is 560 - 30 - (10 * amount of buttons)
    #   Ending X value is 590
    #   Ending Y value is 590 - 30 - (10 * amount of buttons)

    # TEXT NOTES:
    #   Starting X value is ALWAYS 490
    #   Starting Y value is button Y1 + 13
    #   Ending X value is button X2 - 10
    #   Ending Y is button Y2 - 10

    GreyButton = GreyGraphic(win)

    NegButton = NegGraphic(win)

    RandButton = RandGraphic(win)

    SwitchButton = SwitchGraphic(win)

    IDKButton = IDKGraphic(win)

    # Wait for button click:
    Click = ClickTest(img, win, filename, QuitGraphic, SaveGraphic, GreyGraphic, NegGraphic, RandGraphic, SwitchGraphic,
              IDKGraphic)


# Button Graphics


def QuitGraphic(win):
    # Button:
    # Points of Button: (450, 560) and (590, 590)
    QuitButton = Rectangle(Point(450, 560), Point(590, 590))
    QuitButton.setFill("Light Grey")
    QuitButton.setOutline("Black")
    QuitButton.draw(win)

    # Text:
    # Points of Text: (490, 533) and (580, 540)
    QuitText = Text(Point(490, 573), Point(580, 580))
    QuitText.setText("Quit")
    QuitText.setTextColor("Black")
    QuitText.setSize(14)
    QuitText.draw(win)
    return QuitButton

def SaveGraphic(win):
    # Button:
    # Points of Button: (450, 520) and (590, 550)
    SaveButton = Rectangle(Point(450, 520), Point(590, 550))
    SaveButton.setFill("Light Grey")
    SaveButton.setOutline("Black")
    SaveButton.draw(win)

    # Text:
    # Points of Text: (490, 533) and (580, 540)
    SaveText = Text(Point(495, 533), Point(580, 540))
    SaveText.setText("Save Image")
    SaveText.setTextColor("Black")
    SaveText.setSize(12)
    SaveText.draw(win)
    return SaveButton

def GreyGraphic(win):
    # Button:
    # Points of Button: (450, 500) and (590, 530)
    GreyButton = Rectangle(Point(450, 480), Point(590, 510))
    GreyButton.setFill("Light Grey")
    GreyButton.setOutline("Black")
    GreyButton.draw(win)

    # Text:
    # Points of Text: (490, 493) and (590, 470)
    GreyText = Text(Point(495, 493), Point(580, 470))
    GreyText.setText("Greyscale")
    GreyText.setTextColor("Black")
    GreyText.setSize(12)
    GreyText.draw(win)
    return GreyButton

def NegGraphic(win):

    # Button:
    # Points of Button: (450, 460) and (590, 490)
    NegButton = Rectangle(Point(450, 440), Point(590, 470))
    NegButton.setFill("Light Grey")
    NegButton.setOutline("Black")
    NegButton.draw(win)

    # Text:
    # Points of Text: (490, 473) and (590, 430)
    NegText = Text(Point(495, 453), Point(580, 430))
    NegText.setText("Negative")
    NegText.setTextColor("Black")
    NegText.setSize(12)
    NegText.draw(win)
    return NegButton

def RandGraphic(win):
    # Button:
    # Points of Button: (450, 400) and (590, 430)
    RandButton = Rectangle(Point(450, 400), Point(590, 430))
    RandButton.setFill("Light Grey")
    RandButton.setOutline("Black")
    RandButton.draw(win)

    # Text:
    # Points of Text: (490, 413) and (590, 425)
    RandText = Text(Point(495, 413), Point(580, 425))
    RandText.setText("TV Static")
    RandText.setTextColor("Black")
    RandText.setSize(12)
    RandText.draw(win)
    return RandButton

def SwitchGraphic(win):
    # Button:
    # Points of Button: (450, 373) and (590, 400)
    SwitchButton = Rectangle(Point(450, 360), Point(590, 390))
    SwitchButton.setFill("Light Grey")
    SwitchButton.setOutline("Black")
    SwitchButton.draw(win)

    # Text:
    # Points of Text: (490, 373) and (590, 385)
    SwitchText = Text(Point(495, 373), Point(580, 385))
    SwitchText.setText("Switch")
    SwitchText.setTextColor("Black")
    SwitchText.setSize(12)
    SwitchText.draw(win)
    return SwitchButton

def IDKGraphic(win):
    # Button:
    # Points of Button: (450, 373) and (590, 400)
    IDKButton = Rectangle(Point(450, 320), Point(590, 350))
    IDKButton.setFill("Light Grey")
    IDKButton.setOutline("Black")
    IDKButton.draw(win)

    # Text:
    # Points of Text: (490, 373) and (590, 385)
    IDKText = Text(Point(495, 333), Point(580, 345))
    IDKText.setText("Distort")
    IDKText.setTextColor("Black")
    IDKText.setSize(12)
    IDKText.draw(win)
    return IDKButton

# Click Test

def ClickTest(img, win, filename, QuitGraphic, SaveGraphic, GreyGraphic, NegGraphic, RandGraphic, SwitchGraphic,
              IDKGraphic):
    global darken
    global text2
    darken = Rectangle(Point(0, 0), Point(10, 10))
    darken.setFill("White")
    darken.draw(win)
    text2 = Rectangle(Point(0, 0), Point(10, 10))
    text2.setFill("White")
    text2.draw(win)
    while True:
        MouseCheck = win.checkMouse()
        if MouseCheck:
            MouseClickX = MouseCheck.getX()
            if MouseClickX >=450 and MouseClickX <= 590:
                MouseClickY = MouseCheck.getY()
                darken.undraw()
                text2.undraw()
                # Quit
                if MouseCheck and MouseClickY >= 560 and MouseClickY <= 590:
                    darken = Rectangle(Point(450, 560), Point(590, 590))
                    darken.setFill("Dark Grey")
                    darken.setOutline("Black")
                    darken.draw(win)
                    text2 = Text(Point(493, 560), Point(590, 590))
                    text2.setTextColor("Black")
                    text2.setSize(14)
                    text2.setText("Quit")
                    text2.draw(win)
                    QuitProgram(win)


                # Greyscale
                if MouseCheck and MouseClickY >= 480 and MouseClickY <= 510:
                    darken = Rectangle(Point(450, 480), Point(590, 510))
                    darken.setFill("Dark Grey")
                    darken.setOutline("Black")
                    darken.draw(win)
                    text2 = Text(Point(493, 493), Point(590, 510))
                    text2.setTextColor("Black")
                    text2.setSize(12)
                    text2.setText("Greyscale")
                    text2.draw(win)
                    Grey = GreyScale(img, win, filename)


                # Negative
                if MouseCheck and MouseClickY >= 440 and MouseClickY <= 470:
                    darken = Rectangle(Point(450, 440), Point(590, 470))
                    darken.setFill("Dark Grey")
                    darken.setOutline("Black")
                    darken.draw(win)
                    text2 = Text(Point(493, 453), Point(590, 465))
                    text2.setTextColor("Black")
                    text2.setSize(12)
                    text2.setText("Negative")
                    text2.draw(win)
                    Neg = Negative(img, win, filename)


                # Save
                if MouseCheck and MouseClickY >= 520 and MouseClickY <= 550:
                    darken = Rectangle(Point(450, 520), Point(590, 550))
                    darken.setFill("Dark Grey")
                    darken.setOutline("Black")
                    darken.draw(win)
                    text2 = Text(Point(493, 535), Point(590, 545))
                    text2.setTextColor("Black")
                    text2.setSize(12)
                    text2.setText("Save")
                    text2.draw(win)
                    Save = SaveImage(img)

                # Random
                if MouseCheck and MouseClickY >= 400 and MouseClickY <= 430:
                    darken = Rectangle(Point(450, 400), Point(590, 430))
                    darken.setFill("Dark Grey")
                    darken.setOutline("Black")
                    darken.draw(win)
                    text2 = Text(Point(493, 413), Point(590, 425))
                    text2.setTextColor("Black")
                    text2.setSize(12)
                    text2.setText("TV Static")
                    text2.draw(win)
                    Rand = Random(img, win, filename)


                # Switch
                if MouseCheck and MouseClickY >= 360 and MouseClickY <= 390:
                    darken = Rectangle(Point(450, 360), Point(590, 390))
                    darken.setFill("Dark Grey")
                    darken.setOutline("Black")
                    darken.draw(win)
                    text2 = Text(Point(493, 373), Point(590, 385))
                    text2.setTextColor("Black")
                    text2.setSize(12)
                    text2.setText("Switch")
                    text2.draw(win)
                    switch = Switch(img, win, filename)

                # IDK
                if MouseCheck and MouseClickY >= 320 and MouseClickY <= 350:
                    darken = Rectangle(Point(450, 320), Point(590, 350))
                    darken.setFill("Dark Grey")
                    darken.setOutline("Black")
                    darken.draw(win)
                    text2 = Text(Point(493, 333), Point(590, 345))
                    text2.setTextColor("Black")
                    text2.setSize(12)
                    text2.setText("Distort")
                    text2.draw(win)
                    idk = IDK(img, win, filename)






# Color Functions

def GreyScale(img, win, filename):
    img = Image(Point(200, 300), filename)
    img.undraw()
    img.draw(win)
    Gimg = img
    GimgWide = Gimg.getWidth()
    GimgHigh = Gimg.getHeight()
    for w in range(GimgWide):
        for h in range(GimgHigh):
            colorSel = Gimg.getPixel(w, h)
            gray = int(round(0.21 * colorSel[0] + 0.72 * colorSel[1] + 0.07 * colorSel[2]))
            Gimg.setPixel(w, h, color_rgb(gray, gray, gray))
    img.undraw()
    Gimg.draw(win)

def Negative(img, win, filename):
    img = Image(Point(200, 300), filename)
    img.undraw()
    img.draw(win)
    Nimg = img
    NimgWide = img.getWidth()
    NimgHigh = img.getHeight()
    for w in range(NimgWide):
        for h in range(NimgHigh):
            colorSel = Nimg.getPixel(w, h)
            colorSel0 = colorSel[0]
            colorSel1 = colorSel[1]
            colorSel2 = colorSel[2]
            Nimg.setPixel(w, h, color_rgb(255-colorSel0, 255-colorSel1, 255-colorSel2))
    img.undraw()
    Nimg.draw(win)

def Random(img, win, filename):
    img = Image(Point(200, 300), filename)
    img.undraw()
    img.draw(win)
    Rimg = img
    RimgWide = img.getWidth()
    RimgHigh = img.getHeight()
    for w in range(RimgWide):
        for h in range(RimgHigh):
            colorSel = Rimg.getPixel(w, h)
            colorSel0 = colorSel[0]
            colorSel1 = colorSel[1]
            colorSel2 = colorSel[2]
            Rimg.setPixel(w, h, color_rgb(randrange(1, 255), randrange(1, 255), randrange(1, 255)))
    img.undraw()
    Rimg.draw(win)

def Switch(img, win, filename):
    img = Image(Point(200, 300), filename)
    img.undraw()
    img.draw(win)
    Simg = img
    SimgWide = img.getWidth()
    SimgHigh = img.getHeight()
    for w in range(SimgWide):
        for h in range(SimgHigh):
            colorSel = Simg.getPixel(w, h)
            colorSel0 = colorSel[0]
            colorSel1 = colorSel[1]
            colorSel2 = colorSel[2]
            Simg.setPixel(w, h, color_rgb(colorSel2, colorSel1, colorSel0))
    img.undraw()
    Simg.draw(win)

def IDK(img, win, filename):
    img = Image(Point(200, 300), filename)
    img.undraw()
    img.draw(win)
    Iimg = img
    IimgWide = img.getWidth()
    IimgHigh = img.getHeight()
    for w in range(IimgWide):
        for h in range(IimgHigh):
            colorSel = Iimg.getPixel(w, h)
            colorSel0 = colorSel[0]
            colorSel1 = colorSel[1]
            colorSel2 = colorSel[2]
            Iimg.setPixel(w, h, color_rgb(colorSel[(randrange(0,2))], colorSel[(randrange(0,2))], colorSel[(randrange(0,2))]))
    img.undraw()
    Iimg.draw(win)

def SaveImage(img):
    NewFileName = str(input("What would you like the file to be called?  (Automatically appends .ppm to any file)    "))
    img.save(NewFileName + '.ppm')


def QuitProgram(win):
    win.close()


# Main Function

def main():
    print('This program will manipulate an image')
    fileN = str(input("What is the file name of the image?     "))
    graph = GraphMain(fileN)

main()