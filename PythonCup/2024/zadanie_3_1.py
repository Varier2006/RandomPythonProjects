from tkinter import *
from random import *

"""
Navrhni projekt, ktorý pripraví hraciu plochu MxN štvorcov s náhodnými číslami. Program na začiatku hry vyberie náhodné číslo od 2 po 9 a zobrazí ho v hornej časti. Úlohou hráča je klikaním na čísla v hracej ploche označiť všetky čísla, ktoré sú násobkom vybraného čísla.
V programe priprav premenné M a N, ich hodnoty nastav náhodne tak, aby: 3<=M<=5, 3<=N<=10.
Program po štarte podľa aktuálnych hodnôt premenných M a N vygeneruje hraciu plochu náhodných čísel od 1 do 50 tak, že M určuje počet riadkov, N počet stĺpcov v každom riadku. Čísla nakresli ako zelené ('limegreen') kartičky veľkosti 50x50 s fontom 'arial 25'.
Potom program umožní hráčovi klikať na kartičky v hracej ploche. Ak hráč klikne na kartičku, na ktorej je násobok vybraného čísla, kartička sa prefarbí na hnedo ('peru'). Ak hráč klikne na číslo, ktoré nie je násobkom hľadaného čísla, kartička sa na chvíľu prefarbí na červeno ('tomato'), potom sa znovu prefarbí na zeleno.
Ak hráč označí v hracej ploche všetky násobky vybraného čísla, zobrazí sa v hornej časti, vpravo od kartičky s vybraným číslom, text: „Nájdené všetky násobky.“
"""
canvas = Canvas(width=1280, height=720, background="lightgrey")
canvas.pack()

M = randint(3, 5)
N = randint(3, 10)
cislo = randint(2, 9)

canvas.create_text(150, 50, text="Hadaj nasobky cisla:", font="Arial 20")


def square(x, y, t, c):
    canvas.create_rectangle(x - 25, y - 25, x + 25, y + 25, fill=c)
    canvas.create_text(x, y, text=t, font="Arial 25")


square(300, 50, cislo, "limegreen")

cisla = []
for m in range(M):
    cisla.append([])
    for n in range(N):
        cisla[m].append([])
        cisla[m][n].append(randint(1, 50))
        cisla[m][n].append(0)

print(cisla)
print(cisla[1])
win = 0
for i in range(len(cisla)):
    for ii in range(len(cisla[i])):
        if int(cisla[i][ii][0]) % cislo == 0:
            cisla[i][ii][1] = 1
            win = win + 1

print(cisla)
for m in range(len(cisla)):
    for n in range(len(cisla[0])):
        square(40 + m * 60, 120 + n * 60, cisla[m][n][0], "limegreen")

temp = ["1"]
print(temp)
checkwin = 0

def klik(arg):
    global temp, win, checkwin
    if temp[0] != "1":
        square(40 + temp[0] * 60, 120 + temp[1] * 60, temp[2], "limegreen")
    for m in range(len(cisla)):
        for n in range(len(cisla[0])):
            if 40 + 60 * m - 25 <= arg.x <= 40 + 60 * m + 25 and 120 + n * 60 - 25 <= arg.y <= 120 + n * 60 + 25:
                if cisla[m][n][1] == 1:
                    square(40 + m * 60, 120 + n * 60, cisla[m][n][0], "peru")
                    checkwin = checkwin + 1
                else:
                    square(40 + m * 60, 120 + n * 60, cisla[m][n][0], "tomato")
                    temp = [m, n, cisla[m][n][0]]
                    # square(40 + m * 60, 120 + n * 60, cisla[m][n][0], "limegreen")

                    # timeout 2sec a spet na zelene
                print(f"{cisla[m][n][0]}")
                if checkwin == win:
                    canvas.create_text(len(cisla)*30 +20, len(cisla[0]) *30 + 100, text="W", font="Arial 100",fill="magenta")


canvas.bind("<Button-1>", klik)
mainloop()
