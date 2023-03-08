from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, width="1280", height="720")
canvas.pack()
size = 2
spaceBetweenx = 10
spaceBetweeny = 10
for i in range(17):
    print(i)
    x1 = 10 + i * spaceBetweenx * size
    canvas.create_line(x1, 10, 10 + i * size * spaceBetweenx, 10 + size * spaceBetweeny)

canvas.mainloop()