from tkinter import *
from random import *

width = 1280
height = 720
root = Tk()
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()
canvas.configure(scrollregion=(-width / 2, -height / 2, width / 2, height / 2))
playerimg = PhotoImage(file="../img/dievcascaled50.png")
vajceimg = PhotoImage(file="../img/vajcescale50.png")
grid = 50
vajcia = []


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = canvas.create_image((randrange(7) - 3) * grid, (randrange(3) - 1) * grid, image=playerimg)
        canvas.pack()
        self.pos = canvas.coords(self.image)

    def movement(self):
        if width / 2 - grid >= self.pos[0] >= -width/2 + grid and height/2 - grid >= self.pos[1] >= -height/2 + grid:
            canvas.move(self.image, self.x * grid, self.y * grid)
        # broken
        # else:
        #     if self.x == 1:
        #         self.x = -1
        #         self.movement()
        #     elif self.x == -1:
        #         self.x = 1
        #         self.movement()
        #     elif self.y == 1:
        #         self.y = -1
        #         self.movement()
        #     elif self.y == -1:
        #         self.y = 1
        #         self.movement()

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

    def keypressed(self, key):
        if key == 25 or key == 65:
            self.up()
        elif key == 38:
            self.left()
        elif key == 39:
            self.down()
        elif key == 40:
            self.right()


class Vajce:
    def __init__(self):
        self.image = canvas.create_image((randrange(7) - 3) * grid, (randrange(3) - 1) * grid, image=vajceimg)
        canvas.pack()
        self.pos = canvas.coords(self.image)
        for i in range(len(vajcia)):
            if self.pos == vajcia[i].pos:
                self.pos[0] = (randrange(7) - 3) * grid
                self.pos[1] = (randrange(3) - 1) * grid

    def delimg(self):
        canvas.move(self.image, 9999, 9999)


player = Player()
vajce0 = Vajce()
vajcia.append(vajce0)
vajce1 = Vajce()
vajcia.append(vajce1)
vajce2 = Vajce()
vajcia.append(vajce2)
vajce3 = Vajce()
vajcia.append(vajce3)
vajce4 = Vajce()
vajcia.append(vajce4)
vajce5 = Vajce()
vajcia.append(vajce5)
vajce6 = Vajce()
vajcia.append(vajce6)


def keypress(arg):
    key = arg.keycode
    player.keypressed(key)
    for i in range(len(vajcia)):
        if player.pos == vajcia[i].pos:
            print(vajcia[i].pos)
            vajcia[i].delimg()


root.bind("<Key>", keypress)
mainloop()
