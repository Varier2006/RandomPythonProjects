from tkinter import *
from tkinter.ttk import *
import math

# samotny canvas nema moznost readovat keyboard input tak musim dat canvas do normalneho Tk window
root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, width="1280", height="720")
canvas.pack()
canvas.create_rectangle(-10, -10, 10, 10, tags="objecrt", fill="#FF0000")


def keypressed(event):
    znak = event.char
    print(znak)
    # root.move("objecrt", )


step = 1
zoznam = []
posunx = 200
posuny = 360
lastx = 0
lasty = posuny
canvas.create_line(0, posuny, 1280, posuny, fill="gray")
canvas.create_line(posunx, 0, posunx, 720, fill="gray")
for i in range(360):
    #telp = i * step / 20
    telp = math.sin(math.radians(i))
    telp = telp * step * 100
    canvas.create_line(posunx + lastx, posuny + lasty, posunx + lastx + step, posuny + telp)
    lastx = lastx + step
    lasty = telp


root.bind("<Key>", keypressed)
canvas.mainloop()
