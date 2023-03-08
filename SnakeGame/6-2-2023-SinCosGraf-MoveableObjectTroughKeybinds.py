from tkinter import *
from tkinter.ttk import *
import math

# samotny canvas nema moznost readovat keyboard input tak musim dat canvas do normalneho Tk window
root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, width="1280", height="720")
canvas.pack()

sirkaVykreslenia = 2
vyskaVykreslenia = 100
zoznam = []
posunx = 200
posuny = 360
poslednyX = 0
poslednyY = 1

# vykreslenie osi x a y
canvas.create_line(0, posuny, 1280, posuny, fill="gray")
canvas.create_line(posunx, 0, posunx, 720, fill="gray")


for i in range(361):
    vysledokSin = math.sin(math.radians(i))
    konecnyY = vysledokSin * sirkaVykreslenia * vyskaVykreslenia
    print(konecnyY)
    canvas.create_line(posunx + poslednyX, posuny + poslednyY, posunx + poslednyX + sirkaVykreslenia, posuny + konecnyY)
    poslednyX = poslednyX + sirkaVykreslenia
    poslednyY = konecnyY


canvas.mainloop()
