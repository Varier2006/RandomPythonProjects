import tkinter
from random import *

canvas = tkinter.Canvas(width=750, height=750, bg="black")
canvas.pack()


def randomSquare():
    global x, y
    x = randrange(670)
    y = randrange(670)
    a = randint(20, 80)
    #canvas.delete("all")
    if a > 50:
        color = "red"
    else:
        color = "blue"
    canvas.create_rectangle(x, y, x + a, y + a, fill=color)
    canvas.create_text(x + 10, y + 10, text=a)
    canvas.after(150, randomSquare)

randomSquare()
canvas.mainloop()
