import tkinter
import turtle

root = tkinter.Canvas(width=1366, height=768)
root.pack()
turtlescreen = turtle.TurtleScreen(root)
turtlescreen.tracer(1)
tutel = turtle.RawTurtle(turtlescreen)


def vlocka(n, d):
    # co sa tu deje???
    if n == 0:
        tutel.forward(d)
    else:
        vlocka(n - 1, d / 3)
        tutel.left(60)
        vlocka(n - 1, d / 3)
        tutel.left(120)
        vlocka(n - 1, d / 3)
        tutel.left(60)
        vlocka(n - 1, d / 3)


vlocka(4, 300)
"""
def strom(n, d):
    if n > 0:
        tutel.forward(d)
        tutel.left(45)
        strom(n - 1, d / 2)
        tutel.right(90)
        strom(n - 1, d / 2)
        tutel.left(45)
        tutel.forward(-d)


tutel.pensize(3)
tutel.pencolor("#FF00FF")
tutel.forward(-500)
strom(6, 500)
"""
turtlescreen.update()
