from tkinter import *

# vsetko sa hybe len player je vzdy centered, jeden global y podla ktoreho sa vsetko sprava iba s offsetom
# y nech je len jedno ako main pozicia a to druhe nech je len + daco aby to definovalo hrubku dosky
# cez slider nech sa urcuje rychlost a ine veci ako velkost dosiek a ich frekvencia
# Gravtacia a player nech je na neho relativita robit
# Centered na playera aj s cords, nech je on 0,0 vzdy vlastne takze no nevem
"""
# imports every file form tkinter and tkinter.ttk
from tkinter import *
from tkinter.ttk import *

class GFG:
	def __init__(self, master = None):
		self.master = master
		
		# to take care movement in x direction
		self.x = 1
		# to take care movement in y direction
		self.y = 0

		# canvas object to create shape
		self.canvas = Canvas(master)
		# creating rectangle
		self.rectangle = self.canvas.create_rectangle(
						5, 5, 25, 25, fill = "black")
		self.canvas.pack()

		# calling class's movement method to
		# move the rectangle
		self.movement()
	
	def movement(self):

		# This is where the move() method is called
		# This moves the rectangle to x, y coordinates
		self.canvas.move(self.rectangle, self.x, self.y)

		self.canvas.after(100, self.movement)
	
	# for motion in negative x direction
	def left(self, event):
		print(event.keysym)
		self.x = -5
		self.y = 0
	
	# for motion in positive x direction
	def right(self, event):
		print(event.keysym)
		self.x = 5
		self.y = 0
	
	# for motion in positive y direction
	def up(self, event):
		print(event.keysym)
		self.x = 0
		self.y = -5
	
	# for motion in negative y direction
	def down(self, event):
		print(event.keysym)
		self.x = 0
		self.y = 5

if __name__ == "__main__":

	# object of class Tk, responsible for creating
	# a tkinter toplevel window
	master = Tk()
	gfg = GFG(master)

	# This will bind arrow keys to the tkinter
	# toplevel which will navigate the image or drawing
	master.bind("<KeyPress-Left>", lambda e: gfg.left(e))
	master.bind("<KeyPress-Right>", lambda e: gfg.right(e))
	master.bind("<KeyPress-Up>", lambda e: gfg.up(e))
	master.bind("<KeyPress-Down>", lambda e: gfg.down(e))
	
	# Infinite loop breaks only by interrupt
	mainloop()
"""
root = Tk()
root.geometry("1280x720")
root.title("Hmm")
canvas = Canvas(root, width="1280", height="720")
canvas.pack()

dosky = []


class Player:
    def __init__(self):
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


class Doska:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


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


def keypressed(arg):
    if arg.char == " ":
        print("jum")
        jumped()
    elif arg.char == "w":
        Player.up()
    elif arg.char == "a":
        Player.left()
    elif arg.char == "s":
        Player.down()
    elif arg.char == "d":
        Player.right()
    else:
        print()

root.bind("<Key>", keypressed)
canvas.mainloop()
