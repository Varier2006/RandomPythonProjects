import turtle
from random import *

tutel = turtle.Turtle()


def square(size, width, color):
    tutel.pensize(width)
    tutel.pencolor(color)
    wsize = size
    while wsize >= 25:
        for i in range(4):
            tutel.rt(90)
            tutel.forward(wsize)
        tutel.rt(90)
        tutel.forward(wsize/2)
        tutel.rt(90)
        tutel.forward(5)
        tutel.rt(270)
        tutel.forward((wsize-10)/2)
        wsize = wsize - 10


def pentagon(size, width, color):
    tutel.pensize(width)
    tutel.pencolor(color)
    for i in range(6):
        tutel.penup()
        tutel.forward(size/2)
        tutel.rt(90)
        tutel.forward(10)
        tutel.rt(270)
        tutel.pendown()
        for i in range(7):
            tutel.forward(size)
            tutel.rt(60)
        #size = size/100*90


tutel.speed(999)

for i in range(1000):
    tutel.penup()
    tutel.left(randrange(360))
    tutel.setposition(randint(-500, 500), randint(-200, 200))
    #tutel.setposition(0,0)
    #tutel.forward(randrange(500))
    color = "#{:06x}".format(randrange(256 ** 3))
    tutel.pendown()
    square(randint(25, 250), randint(1, 4), color)
    """
    ran = randint(1, 2)
    if ran == 1:
        square(randint(25, 250), randint(1, 4), color)
    elif ran == 2:
        pentagon(randint(25, 250), randint(1, 4), color)
    """