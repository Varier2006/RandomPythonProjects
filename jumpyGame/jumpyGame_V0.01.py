from tkinter import *

# vsetko sa hybe len player je vzdy centered, jeden global y podla ktoreho sa vsetko sprava iba s offsetom
# y nech je len jedno ako main pozicia a to druhe nech je len + daco aby to definovalo hrubku dosky
# cez slider nech sa urcuje rychlost a ine veci ako velkost dosiek a ich frekvencia
# Gravtacia a player nech je na neho relativita robit
# Centered na playera aj s cords, nech je on 0,0 vzdy vlastne takze no nevem

root = Tk()
root.geometry("1280x720")
root.title("Hmm")
canvas = Canvas(root, width="1280", height="720")
canvas.pack()

dosky = []
key = ""

class Player:
    def __init__(self, master=None):
        self.x = 0
        self.y = 0

        self.rectangle = canvas.create_rectangle(5, 5, 25, 25, fill="black")
        canvas.pack()

    def movement(self):
        canvas.move(self.rectangle, self.x, self.y)

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
        self.x = 0
        self.y = 5
        self.movement()

    def keypressed(self):
        global key
        if key == " ":
            print("jum")
            jumped()
        elif key == "w":
            self.up()
        elif key == "a":
            self.left()
        elif key == "s":
            self.down()
        elif key == "d":
            self.right()
        else:
            print(key)


class Doska:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


player = Player()
doska0 = Doska(0, 0, 0, 0)
dosky.append(doska0)
doska1 = Doska(0, 0, 0, 0)
dosky.append(doska1)
doska2 = Doska(0, 0, 0, 0)
dosky.append(doska2)
doska3 = Doska(0, 0, 0, 0)
dosky.append(doska3)
doska4 = Doska(0, 0, 0, 0)
dosky.append(doska4)
doska5 = Doska(0, 0, 0, 0)
dosky.append(doska5)
doska6 = Doska(0, 0, 0, 0)
dosky.append(doska6)
doska7 = Doska(0, 0, 0, 0)
dosky.append(doska7)
doska8 = Doska(0, 0, 0, 0)
dosky.append(doska8)
doska9 = Doska(0, 0, 0, 0)
dosky.append(doska9)

for i in range(len(dosky)):
    print(f"i = {i}")
    canvas.create_rectangle(dosky[i].x1, dosky[i].y1, dosky[i].x2, dosky[i].y2)
    print("vykreslene")
    canvas.update()


def jumped():
    for i in range(len(dosky)):
        print(f"i = {i}")
        canvas.move(dosky[i])
        print("vykreslene")
        canvas.update()


def keypress(arg):
    global key
    pressed = True
    key = arg.char
    player.keypressed()


root.bind("<Key>", keypress)
canvas.mainloop()
