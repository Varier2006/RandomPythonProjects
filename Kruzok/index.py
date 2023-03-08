import tkinter
import random
import time
canvas = tkinter.Canvas()
canvas.pack()
canvas.configure(width=750,height=750)
#trojuholnik
"""
canvas.create_line(110,10,10,210,fill="blue")
canvas.create_line(10,210,210,210,fill="blue")
canvas.create_line(210,210,110,10,fill="blue")
"""
#osnova
"""
x = 10
for i in range(6 canvas.create_line(x+250,x,x+250,x+50,fill="blue")
    x = x + 10
"""
#random square
"""
for i in range(400):
    y = random.randrange(700)
    x = random.randrange(700)
    size = random.randint(5,50)
    color = random.choice(("red","yellow","skyblue"))
    canvas.create_rectangle(x,y,x+size,y+size,fill=color)
    canvas.after(111)
"""
"""
canvas.create_oval(200,200,300,250,fill="gray")
canvas.create_rectangle(200,345,300,450,fill="blue")
canvas.create_oval(200,250,300,350,fill="lightgray")

#usmev
canvas.create_oval(225,300,275,340)
canvas.create_rectangle(225,300,275,320,outline="lightgray",fill="lightgray")

canvas.create_oval(180,290,320,310,fill="gray")
canvas.create_rectangle(200,225,300,300,fill="gray")

#oci
canvas.create_oval(230,310,240,320,fill="lightblue")
canvas.create_oval(235,315,235,315)
canvas.create_oval(260,310,270,320,fill="lightblue")
canvas.create_oval(265,315,265,315)
"""

