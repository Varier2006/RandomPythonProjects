import tkinter
from random import *
#kyvadlo
canvas = tkinter.Canvas(width=750, height=750, bg="black")
canvas.pack()
global x, color


def drawPendelum():
    canvas.create_line(375, 375, x, 400, fill=color)
    canvas.create_oval()
