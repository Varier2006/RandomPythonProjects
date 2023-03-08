from tkinter import *
from random import *

root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, width="1920", height="1080")
canvas.pack()


def kresliLopticku(x, y):
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")


def kresliKurzor(x, y):
    canvas.create_line(x, y, x + 50, y, fill="blue", width=5)


def vypisBody(pocetBodov):
    canvas.create_text(100, 10, text="Body:")
    canvas.create_text(200, 10, text=pocetBodov)


def timerl():
    canvas.delete("all")
    global loptickaX, loptickaY, pocetBodov
    loptickaY = loptickaY + 5
    kresliLopticku(loptickaX, loptickaY)
    kresliKurzor(kurzorX, kurzorY)
    vypisBody(pocetBodov)
    if kurzorX < loptickaX < kurzorX + 50 and kurzorY - 10 < loptickaY < kurzorY:
        pocetBodov = pocetBodov + 1
        loptickaX = randrange(750)
        loptickaY = 20
    if loptickaY > 500:
        loptickaX = randrange(750)
        loptickaY = 20
    if pocetBodov == 10:
        root.quit()
    canvas.after(10, timerl)


def posunMysi(suradnice):
    global pocetBodov, kurzorX
    kurzorX = suradnice.x
    """
    canvas.delete("all")
    kresliLopticku(loptickaX, loptickaY)
    kresliKurzor(kurzorX, kurzorY)
    vypisBody(pocetBodov)
    """

pocetBodov = 0
loptickaX = randrange(750)
loptickaY = 20
kurzorX = 150
kurzorY = 450
timerl()
canvas.bind("<Motion>", posunMysi)
canvas.mainloop()
