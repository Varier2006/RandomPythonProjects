from tkinter import *
from turtle import *
from random import *

root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, width="670", height="670")
canvas.pack(side="bottom")

ts = TurtleScreen(canvas)
ts.delay(0)
zoznam = []
k0 = RawTurtle(ts)
k0.penup()
k0.setpos(-300, 300)
k0.pendown()
for i in range(4):
    for j in range(20):
        k = RawTurtle(ts)
        k.penup()
        k.speed(0)
        k.setpos(k0.pos())
        k.setheading(k.towards(0, 0))
        k.pendown()
        zoznam.append(k)
        k0.forward(30)
    k0.right(90)
size = 0


def start():
    global size
    for i in range(20):
        size = size + 1
        for k in zoznam:
            k.pensize(size)
            col1 = randrange(255)
            col2 = randrange(255)
            col3 = randrange(255)
            colore = f"#{col1:02x}{col2:02x}{col3:02x}"
            k.pencolor(colore)
            k.fd(15)


canvas.moveto(0, 0)
button = Button(text="START", command=start)
button.pack(side="top")
canvas.mainloop()
