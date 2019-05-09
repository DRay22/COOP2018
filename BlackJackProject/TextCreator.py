from graphics import *

class MakeText:

    def __init__(self, win, FirstPoint, SecondPoint, size, TextColor, text):
        p1 = FirstPoint
        p2 = SecondPoint
        self.Text = Text(p1, p2)
        self.Text.setText(text)
        self.Text.setSize(size)
        self.Text.setTextColor(TextColor)

    def Activate(self, win):
        self.Text.draw(win)

    def Deactivate(self):
        self.Text.undraw()

    def UpdateText(self, NewText):
        self.Text.setText(NewText)
