"""
Hracie pole sa vie vykreslit ale cez ciary jednotlive
Program vie upravit velkost pola podla velkosti okna
"""

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, width="1920", height="1080")
canvas.pack()
previous = 1


def keypressed(arg):
    print(arg)
    print(root.winfo_width(), root.winfo_height())


def configured(arg):
    global previous
    print(arg)
    print(arg.width / arg.height)
    if arg.width / arg.height >= 1:
        print("1 or more")
        now = 1
    else:
        print("less than 1")
        now = 0
    if previous != now:
        if arg.width > arg.height:
            repaintGrid(arg.height)
        else:
            repaintGrid(arg.width)


def repaintGrid(size):
    # zaokruhlit nadol lebo neviem ako na tom su floats
    canvas.create_rectangle(-9999, -9999, 9999, 9999, fill="white", outline="white")
    size = size / 16 - 3
    for i in range(17):
        print(i)
        x11 = 16 + i * size
        y11 = 16
        x12 = 16 + i * size
        y12 = 16 + size - 15
        canvas.create_line(x11, y11, x12, y12 * 16)
        x21 = 16
        y21 = 16 + i * size
        x22 = 16 + size - 15
        y22 = 16 + i * size
        canvas.create_line(x21, y21, x22 * 16, y22)


repaintGrid(720)
root.bind("<Key>", keypressed)
root.bind("<Configure>", configured)
canvas.mainloop()
