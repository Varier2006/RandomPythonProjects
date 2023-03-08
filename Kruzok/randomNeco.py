import tkinter
import random

canvas = tkinter.Canvas(width=750, height=750, background="black")
mesto = "Slovensko"
farby = ["blue", "red", "green", "white", "gray", "lightblue", "lightgreen", "yellow", "brown"]
x = 200
y = 0
for i in range(len(mesto)):
    canvas.create_text(x + y, 200, text=mesto[i], fill=random.choice(farby), font=('Helvetica 30 bold'))
    y = y + 20
canvas.pack()
canvas.mainloop()
