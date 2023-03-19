from tkinter import *
from math import *

width = 1920
height = 1080
root = Tk()
root.geometry("1920x1080")
canvas = Canvas(root, width=width, height=height)
canvas.pack()
canvas.configure(scrollregion=(-width / 2, -height / 2, width / 2, height / 2))
# Vykreslenie grid
for i in range(100):
    canvas.create_line(-width, i * 10, width, i * 10, fill="lightgray", width=1)
    canvas.create_line(-width, -i * 10, width, -i * 10, fill="lightgray", width=1)
    canvas.create_line(i * 10, -height, i * 10, height, fill="lightgray", width=1)
    canvas.create_line(-i * 10, -height, -i * 10, height, fill="lightgray", width=1)
canvas.create_line(-width, 0, width, 0, fill="gray", width=1)
canvas.create_line(0, -height, 0, height, fill="gray", width=1)

step = 3
lastx = 0
lasty = 0
offset = 297
for i in range(width * 2):
    telp = pow(sin(radians(i + 1)), -1)
    telp = telp * step * 1
    canvas.create_line(lastx - width + offset, lasty, lastx + step - width + offset, telp, fill="blue")
    lastx = lastx + step
    lasty = telp
lastx = 0
lasty = 0
for i in range(width * 2):
    telp = pow(cos(radians(i)), -1)
    telp = telp * step * 1
    canvas.create_line(lastx - width + offset, lasty, lastx + step - width + offset, telp, fill="red")
    lastx = lastx + step
    lasty = telp

mainloop()
