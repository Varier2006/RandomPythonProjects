import tkinter
import time
from random import *
import keyboard

canvas = tkinter.Canvas(width=750, height=750, background="white")
canvas.pack(side="left")
# _____________________________________________________________________________

# objekt1
novy_objekt1 = True
objekt_x1 = 0
objekt_y1 = -5
zmena_rychlosti1 = 0
objekt_y_ciel1 = 0
typ_hruska1 = False
typ_bomba1 = False
reset1 = False
# objekt2
novy_objekt2 = True
objekt_x2 = 0
objekt_y2 = -5
zmena_rychlosti2 = 0
objekt_y_ciel2 = 0
typ_hruska2 = False
typ_bomba2 = False
reset2 = False

# objekt3
novy_objekt3 = True
objekt_x3 = 0
objekt_y3 = -5
zmena_rychlosti3 = 0
objekt_y_ciel3 = 0
typ_hruska3 = False
typ_bomba3 = False
reset3 = False

# iné
medzernik_prestavka = 0
medzernik_prestavka_odpocitavadlo = 0
body = 0
kurzor_x = 0
kurzor_y = 0
game_over = True
pocet_zivotov = 5


# __________________________________________________________________________

def gameover():
    global game_over
    game_over = True
    canvas.delete("all")
    time.sleep(1)
    canvas.create_text(375, 375, text="KONIEC", font=("Times New Roman", 50))


def objekt1(x, y):
    # canvas.create_rectangle(x-25,y-25,x+25,y+25, fill = "Green")
    if typ_hruska1 == True:
        canvas.create_image(x - 50, y - 50, anchor=tkinter.NW, image=hruska)
    if typ_bomba1 == True:
        canvas.create_image(x - 50, y - 50, anchor=tkinter.NW, image=bomba)


def objekt2(x, y):
    # canvas.create_rectangle(x-25,y-25,x+25,y+25, fill = "Green")
    if typ_hruska2 == True:
        canvas.create_image(x - 50, y - 50, anchor=tkinter.NW, image=hruska)
    if typ_bomba2 == True:
        canvas.create_image(x - 50, y - 50, anchor=tkinter.NW, image=bomba)


def objekt3(x, y):
    # canvas.create_rectangle(x-25,y-25,x+25,y+25, fill = "Green")
    if typ_hruska3 == True:
        canvas.create_image(x - 50, y - 50, anchor=tkinter.NW, image=hruska)
    if typ_bomba3 == True:
        canvas.create_image(x - 50, y - 50, anchor=tkinter.NW, image=bomba)


def kurzor_vykreslenie(x, y):
    canvas.create_image(x, y, anchor=tkinter.NW, image=basket)


# ______________________________________________________________________________________________________________________________

def startgame():
    global img1, novy_objekt1, body, objekt_x1, objekt_y1, zmena_rychlosti1, objekt_y_ciel1, reset1, medzernik_prestavka, medzernik_prestavka_odpocitavadlo
    global typ_hruska1, typ_bomba1, pocet_zivotov, novy_objekt2, objekt_x2, objekt_y2, zmena_rychlosti2, objekt_y_ciel2, typ_hruska2, typ_bomba2
    global reset2, novy_objekt3, objekt_x3, objekt_y3, zmena_rychlosti3, objekt_y_ciel3, reset3, typ_hruska3, typ_bomba3, game_over
    # nový objekt1 a objekt2: smer hore/dole
    canvas.delete("all")
    game_over = False
    if novy_objekt1 == True:
        while True:
            zmena_rychlosti1 = randint(-20, 20)
            if zmena_rychlosti1 == 0:
                zmena_rychlosti1 = randint(-20, 20)
            else:
                zmena_rychlosti1 = int(zmena_rychlosti1)
                novy_objekt1 = False
                objekt_x1 = randint(50, 700)
                if zmena_rychlosti1 < 0:
                    objekt_y1 = 800
                    objekt_y_ciel1 = -50
                elif zmena_rychlosti1 > 0:
                    objekt_y1 = -50
                    objekt_y_ciel1 = 800
                k1 = randrange(4)
                if k1 == 3:
                    typ_bomba1 = True
                    typ_hruska1 = False
                else:
                    typ_hruska1 = True
                    typ_bomba1 = False
                break

    if novy_objekt2 == True:
        while True:
            zmena_rychlosti2 = randint(-20, 20)
            if zmena_rychlosti2 == 0:
                zmena_rychlosti2 = randint(-20, 20)
            else:
                zmena_rychlosti2 = int(zmena_rychlosti2)
                novy_objekt2 = False
                objekt_x2 = randint(50, 700)
                if zmena_rychlosti2 < 0:
                    objekt_y2 = 800
                    objekt_y_ciel2 = -50
                elif zmena_rychlosti2 > 0:
                    objekt_y2 = -50
                    objekt_y_ciel2 = 800
                k2 = randrange(4)
                if k2 == 3:
                    typ_bomba2 = True
                    typ_hruska2 = False
                else:
                    typ_hruska2 = True
                    typ_bomba2 = False
                break

    if novy_objekt3 == True:
        while True:
            zmena_rychlosti3 = randint(-20, 20)
            if zmena_rychlosti3 == 0:
                zmena_rychlosti3 = randint(-20, 20)
            else:
                zmena_rychlosti3 = int(zmena_rychlosti3)
                novy_objekt3 = False
                objekt_x3 = randint(50, 700)
                if zmena_rychlosti3 < 0:
                    objekt_y3 = 800
                    objekt_y_ciel3 = -50
                elif zmena_rychlosti3 > 0:
                    objekt_y3 = -50
                    objekt_y_ciel3 = 800
                k3 = randrange(4)
                if k3 == 3:
                    typ_bomba3 = True
                    typ_hruska3 = False
                else:
                    typ_hruska3 = True
                    typ_bomba3 = False
                break

    # rýchlost objektu1 a objektu2
    objekt_y1 = objekt_y1 + zmena_rychlosti1
    objekt_y2 = objekt_y2 + zmena_rychlosti2
    objekt_y3 = objekt_y3 + zmena_rychlosti3
    canvas.create_image(0, 0, anchor=tkinter.NW, image=img1)
    objekt1(objekt_x1, objekt_y1)
    objekt2(objekt_x2, objekt_y2)
    objekt3(objekt_x3, objekt_y3)
    canvas.create_text(40, 10, text="počet životov: " + str(pocet_zivotov))
    canvas.create_text(30, 20, text="body: " + str(body))
    kurzor_vykreslenie(kurzor_x, kurzor_y)

    if medzernik_prestavka_odpocitavadlo > 0:
        medzernik_prestavka_odpocitavadlo = medzernik_prestavka_odpocitavadlo - 1
        medzernik_prestavka = True
    elif medzernik_prestavka_odpocitavadlo == 0:
        medzernik_prestavka = False

    if (keyboard.is_pressed('space')) and (medzernik_prestavka == False):
        if (objekt_x1 - 50 < kurzor_x < objekt_x1 + 50) and (objekt_y1 - 50 < kurzor_y < objekt_y1 + 50):
            medzernik_prestavka_odpocitavadlo = 10
            reset1 = True
            if typ_hruska1 == True:
                body = body + 1
            if typ_bomba1 == True:
                pocet_zivotov = pocet_zivotov - 1

        if (objekt_x2 - 50 < kurzor_x < objekt_x2 + 50) and (objekt_y2 - 50 < kurzor_y < objekt_y2 + 50):
            medzernik_prestavka_odpocitavadlo = 20
            reset2 = True
            if typ_hruska2 == True:
                body = body + 1
            if typ_bomba2 == True:
                pocet_zivotov = pocet_zivotov - 1

        if (objekt_x3 - 50 < kurzor_x < objekt_x3 + 50) and (objekt_y3 - 50 < kurzor_y < objekt_y3 + 50):
            medzernik_prestavka_odpocitavadlo = 20
            reset3 = True
            if typ_hruska3 == True:
                body = body + 1
            if typ_bomba3 == True:
                pocet_zivotov = pocet_zivotov - 1

    # keď sa objekt dostane na druhú stranu --> starý objekt zmizne, nový sa objavý
    if (objekt_y1 >= objekt_y_ciel1) and (zmena_rychlosti1 > 0):
        reset1 = True
    elif (objekt_y1 <= objekt_y_ciel1) and (zmena_rychlosti1 < 0):
        reset1 = True
    if (objekt_y2 >= objekt_y_ciel2) and (zmena_rychlosti2 > 0):
        reset2 = True
    elif (objekt_y2 <= objekt_y_ciel2) and (zmena_rychlosti2 < 0):
        reset2 = True
    if (objekt_y3 >= objekt_y_ciel3) and (zmena_rychlosti3 > 0):
        reset3 = True
    elif (objekt_y3 <= objekt_y_ciel3) and (zmena_rychlosti3 < 0):
        reset3 = True
    if reset1 == True:
        objekt_x1 = 0
        objekt_y1 = 0
        zmena_rychlosti1 = 0
        objekt_y_ciel1 = 0
        reset1 = False
        typ_hruska1 = False
        typ_bomba1 = False
        novy_objekt1 = True
        if pocet_zivotov == 0:
            gameover()
            return
    if reset2 == True:
        objekt_x2 = 0
        objekt_y2 = 0
        zmena_rychlosti2 = 0
        objekt_y_ciel2 = 0
        typ_hruska2 = False
        typ_bomba2 = False
        novy_objekt2 = True
        reset2 = False
        if pocet_zivotov == 0:
            gameover()
            return
    if reset3 == True:
        objekt_x3 = 0
        objekt_y3 = 0
        zmena_rychlosti3 = 0
        objekt_y_ciel3 = 0
        typ_hruska3 = False
        typ_bomba3 = False
        novy_objekt3 = True
        reset3 = False
        if pocet_zivotov == 0:
            gameover()
            return
    canvas.update()
    canvas.after(10, startgame)


# ____________________________________________________________________________________

def posun_mysi(suradnice):
    global kurzor_x, kurzor_y, game_over
    if game_over == False:
        kurzor_x = suradnice.x
        kurzor_y = suradnice.y
        canvas.delete("all")
        canvas.create_image(0, 0, anchor=tkinter.NW, image=img1)
        objekt1(objekt_x1, objekt_y1)
        objekt2(objekt_x2, objekt_y2)
        objekt3(objekt_x3, objekt_y3)
        kurzor_vykreslenie(kurzor_x, kurzor_y)
        canvas.create_text(40, 10, text="počet životov: " + str(pocet_zivotov))
        canvas.create_text(30, 20, text="body: " + str(body))


# _________________________________________________________________________________________________________________________


img1 = tkinter.PhotoImage(file="img/planks.png")
basket = tkinter.PhotoImage(file="img/basket.png")
hruska = tkinter.PhotoImage(file="img/hruska.png")
bomba = tkinter.PhotoImage(file="img/bomba.png")
button = tkinter.Button(text="start", command=startgame)
button.pack()
canvas.bind("<Motion>", posun_mysi)

tkinter.mainloop()
