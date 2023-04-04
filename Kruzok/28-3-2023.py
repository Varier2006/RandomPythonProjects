import tkinter
import random

width = 1280
height = 720
root = tkinter.Tk()
root.geometry(f"{width}x{height}")
root.title("Magnificent Game")
canvas = tkinter.Canvas(root, width=width, height=height)
canvas.pack()
canvas.configure(scrollregion=(-width / 2, -height / 2, width / 2, height / 2))
