import turtle
from turtle import *
from random import *

tutel = Turtle()
tutel.penup()
tutel.setposition(randrange(650) - 300, randrange(120) + 100)
n = randrange(10) + 5
strana = randrange(10) + 10
luc = randrange(50) + 30
tutel.pendown()


def obdlznik(a, b):
    for i in range(2):
        tutel.forward(a)
        tutel.left(90)
        tutel.forward(b)
        tutel.left(90)


def slnko(n, strana, luc):
    uhol = 360 / n
    for i in range(n):
        tutel.forward(strana)
        tutel.right(uhol)
        obdlznik(strana, luc)


slnko(n, strana, luc)

mainloop()
