from tkinter import *
from random import *

width = 1280
height = 720
root = Tk()
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()
canvas.configure(scrollregion=(-width / 2, -height / 2, width / 2, height / 2))

class Player:
    def __init__(self):
        self.pos = canvas.coords(self.image)