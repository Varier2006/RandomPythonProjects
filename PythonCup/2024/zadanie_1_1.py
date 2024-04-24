from turtle import *
from random import *

"""
Čiary symetricky
Navrhni projekt, ktorý nakreslí symetricky podľa y-ovej osi rovnako dlhé čiary, medzi ktorými sú stále väčšie medzery tak, ako vidíš na obrázku.
Na našom obrázku je 12 čiar: 6 čiar zľava a ku nim 6 čiar symetricky. 
Medzi prvou a druhou čiarou zľava je vždy medzera veľkosti 5. Medzi každou nasledujúcou čiarou je medzera, ktorá je väčšia náhodne o 1 až 3. Uvedom si, že medzery medzi čiarami, ktoré sú nakreslené symetricky, musia byť rovnako veľké.
Prázdne miesto vznikne tým, že čiara sa nenakreslí, ak by sa mala nakresliť bližšie k osi y, ako je aktuálna veľkosť medzery.
Po štarte vygeneruj náhodnú vzdialenosť začiatku kreslenia čiar od y-ovej osi (100 až 200) a dĺžku čiar (80 až 200). Čiary nakresli tak, aby bol stred celej kresby v bode (0, 0).
"""
# rework with while loop until it's good, for the generation part
dlzka = randint(80, 200)
zaciatok = randint(100, 200)
odstupy = []
x = 5
for i in range(5):
    x = x + randint(1, 3)
    odstupy.append(x)
penup()
lt(90)
fd(dlzka / 2)
lt(90)
fd(zaciatok)
rt(180)
pendown()
for o in odstupy:
    pendown()
    rt(90)
    fd(dlzka)
    lt(90)
    penup()
    fd(o)
    lt(90)
    fd(dlzka)
    rt(90)
pendown()
rt(90)
fd(dlzka)
lt(90)
penup()
setpos(0, 0)
lt(90)
fd(dlzka / 2)
rt(90)
fd(zaciatok)
rt(180)
pendown()
for o in odstupy:
    pendown()
    lt(90)
    fd(dlzka)
    rt(90)
    penup()
    fd(o)
    rt(90)
    fd(dlzka)
    lt(90)
pendown()
lt(90)
fd(dlzka)
rt(90)
mainloop()
