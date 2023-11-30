# obrazky vlozit do isteho priecinka ako kod,projekt bol vypracovany v linux tak obrazky mozno nebudu fungovat
from tkinter import *
from random import *

width = 1280
height = 720
root = Tk()
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()
canvas.configure(scrollregion=(-width / 2, -height / 2, width / 2, height / 2))
stopy0 = PhotoImage(file="./stopy0.png")
stopy1 = PhotoImage(file="./stopy1.png")
stopy2 = PhotoImage(file="./stopy2.png")
stopy3 = PhotoImage(file="./stopy3.png")
stopy4 = PhotoImage(file="./stopy4.png")
zviera0 = PhotoImage(file="./zviera0.png")
zviera1 = PhotoImage(file="./zviera1.png")
zviera2 = PhotoImage(file="./zviera2.png")
zviera3 = PhotoImage(file="./zviera3.png")
zviera4 = PhotoImage(file="./zviera4.png")
stopy = [stopy0, stopy1, stopy2, stopy3, stopy4]
zvierata = [zviera0, zviera1, zviera2, zviera3, zviera4]

for i in range(len(zvierata)):
    canvas.create_image(i * 150 - width / 2 + 300, -200, image=zvierata[i], tag=i)
cisloStopy = randrange(len(stopy))
canvas.create_image(-200, 0, image=stopy[cisloStopy])


def klik(arg):
    print(arg.x)
    print(cisloStopy)
    print(cisloStopy * 150 + 300)
    if cisloStopy * 150 + 250 <= arg.x <= cisloStopy * 150 + 350:
        canvas.moveto(cisloStopy + 1, -200, -75)
        for i in range(4):
            canvas.create_image(i * 150 - 50, 0, image=stopy[cisloStopy])
            canvas.move(cisloStopy + 1, 150, 0)
            canvas.update()
            canvas.after(1000)


root.bind("<Button-1>", klik)
mainloop()
