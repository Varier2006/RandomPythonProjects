from tkinter import *
from random import *

ww = 1280
wh = 720
root = Tk()
root.geometry(f"{ww}x{wh}")
canvas = Canvas(root, width="1280", height="720")
canvas.pack()

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3]
width = 25

for i in x:
    for ii in y:
        canvas.create_rectangle()

canvas.create_line(1, 1, 100, 100)

canvas.mainloop()
