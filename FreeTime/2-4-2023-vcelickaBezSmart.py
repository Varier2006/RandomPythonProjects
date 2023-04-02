import time
from tkinter import *
from random import *

width = 1280
height = 720
root = Tk()
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()
canvas.configure(scrollregion=(-width / 2, -height / 2, width / 2, height / 2))
kvetimg = PhotoImage(file="../img/kvetsmol.png")
vcelickaimg = PhotoImage(file="../img/vcelickasmol.png")
kvety = []


class Kvet:
    def __init__(self):
        self.done = True
        self.image = canvas.create_image(randrange(width - 100) - width / 2 + 100,
                                         randrange(height - 100) - height / 2 + 100, image=kvetimg)
        canvas.pack()
        self.pos = canvas.coords(self.image)


class Vcelicka:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = canvas.create_image(randrange(width - 100) - width / 2 + 100,
                                         randrange(height - 100) - height / 2 + 100, image=vcelickaimg)
        canvas.pack()
        self.pos = canvas.coords(self.image)

    def movement(self):
        canvas.move(self.image, self.x, self.y)
        self.pos = canvas.coords(self.image)

    def left(self):
        self.x = -1
        self.y = 0
        self.movement()

    def right(self):
        self.x = 1
        self.y = 0
        self.movement()

    def up(self):
        self.x = 0
        self.y = -1
        self.movement()

    def down(self):
        self.x = 0
        self.y = 1
        self.movement()


kvet0 = Kvet()
kvet0.done = False
kvety.append(kvet0)
kvet1 = Kvet()
kvety.append(kvet1)
kvet2 = Kvet()
kvety.append(kvet2)
vcelicka = Vcelicka()


def cycle():
    for i in reversed(range(len(kvety))):
        if not kvety[i].done:
            if kvety[i].pos[0] > vcelicka.pos[0]:
                vcelicka.right()
            elif kvety[i].pos[0] < vcelicka.pos[0]:
                vcelicka.left()
            if kvety[i].pos[1] > vcelicka.pos[1]:
                vcelicka.down()
            elif kvety[i].pos[1] < vcelicka.pos[1]:
                vcelicka.up()
            if kvety[i].pos[0] == vcelicka.pos[0] and kvety[i].pos[1] == vcelicka.pos[1]:
                kvety[i].done = True
                if len(kvety) > i + 1:
                    kvety[i + 1].done = False
                    time.sleep(2)
    canvas.after(10, cycle)


cycle()
mainloop()
