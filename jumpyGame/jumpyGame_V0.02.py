# vsetko sa hybe len player je vzdy centered, jeden global y podla ktoreho sa vsetko sprava iba s offsetom
# y nech je len jedno ako main pozicia a to druhe nech je len + daco aby to definovalo hrubku dosky
# cez slider nech sa urcuje rychlost a ine veci ako velkost dosiek a ich frekvencia
# Gravtacia a player nech je na neho relativita robit
# Centered na playera aj s cords, nech je on 0,0 vzdy vlastne takze no nevem
# ked stupne na nejaku platformu sa posunie minimal height co je vlastne podla coho sa to bude spravat

from tkinter import *
from random import *

width = 1280
height = 720
root = Tk()
root.geometry(f"{width}x{height}")
root.title("Magnificent Game")
canvas = Canvas(root, width=width, height=height)
canvas.pack()
canvas.configure(scrollregion=(-width / 2, -height / 2, width / 2, height / 2))

dosky = []
key = ""
keys = []
gravity = True
skip = 0


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.rectangle = canvas.create_rectangle(5, 5, 25, 25, fill="black", outline="red")
        canvas.pack()
        self.pos = canvas.coords(self.rectangle)

    def movement(self):
        canvas.move(self.rectangle, self.x, self.y)
        self.pos = canvas.coords(self.rectangle)

    def left(self):
        self.x = -5
        self.y = 0
        self.movement()

    def right(self):
        self.x = 5
        self.y = 0
        self.movement()

    def up(self):
        self.x = 0
        self.y = -5
        self.movement()

    def down(self):
        global skip
        print("down")
        skip = 1

    def keypressed(self,key):
        if key == 25 or key == 65:
            self.up()
        elif key == 38:
            self.left()
        elif key == 39:
            self.down()
        elif key == 40:
            self.right()
        else:
            print(key)

    def gravity(self):
        self.x = 0
        self.y = 1
        self.movement()


class Doska:
    def __init__(self):
        self.y = 0
        self.x = 0
        x = randrange(width) - (width / 2)
        self.rectangle = canvas.create_rectangle(x, 105, x + 100, 115, fill="black")
        self.pos = canvas.coords(self.rectangle)
        canvas.pack()

    def movement(self):
        canvas.move(self.rectangle, self.x, self.y)

    def up(self):
        self.x = 0
        self.y = -5
        self.movement()

    def down(self):
        self.x = 0
        self.y = 5
        self.movement()


player = Player()
doska0 = Doska()
dosky.append(doska0)
doska1 = Doska()
dosky.append(doska1)
doska2 = Doska()
dosky.append(doska2)
doska3 = Doska()
dosky.append(doska3)
doska4 = Doska()
dosky.append(doska4)
doska5 = Doska()
dosky.append(doska5)
doska6 = Doska()
dosky.append(doska6)
doska7 = Doska()
dosky.append(doska7)
doska8 = Doska()
dosky.append(doska8)
doska9 = Doska()
dosky.append(doska9)


def keyup(arg):
    global keys
    print("keyup")
    if arg.keycode in keys:
        keys.pop(keys.index(arg.keycode))
        print("pop")

        # var.set(str(history))


def keydown(arg):
    global keys
    print("keydown")
    if not arg.keycode in keys:
        keys.append(arg.keycode)
        print("append")
        # var.set(str(history))


def cycle():
    global gravity, dosky, skip, keys
    for i in keys:
        player.keypressed(i)
        print(keys)
    if skip > 0:
        skip = skip - 1
    else:
        for i in dosky:
            if i.pos[0] <= player.pos[2] and i.pos[2] >= player.pos[0] and i.pos[1] == player.pos[3] + 1:
                gravity = False
    if gravity:
        player.gravity()
    gravity = True
    canvas.after(25, cycle)


root.bind("<KeyPress>", keydown)
root.bind("<KeyRelease>", keyup)
cycle()
canvas.mainloop()
