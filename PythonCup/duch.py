from random import *
from tkinter import *

"""
Duch
Navrhni projekt, ktorý pripraví hraciu plochu z bielych a sivých štvorcov, po ktorých bude skákať duch. Úlohou hráča je kliknutím určiť štvorec, na ktorom uvidel ducha naposledy.
V programe sú premenné M a N, ich hodnoty sa na začiatku vygenerujú náhodne tak, že platí: 3<=M<=5, 3<=N<=7. Program po štarte podľa aktuálnych hodnôt týchto premenných vygeneruje hraciu plochu tak, že M určuje počet riadkov, N počet stĺpcov v každom riadku. Každý štvorec má veľkosť 50x50 a bielu alebo sivú farbu, pričom farby majú význam iba pre lepšiu orientáciu hráča na hracej ploche. Potom program zobrazí objavenie ducha náhodný počet krát (3 až 5) na niektorých náhodných štvorcoch. Na každom štvorci sa duch zobrazí na nejaký krátky čas, potom sa skryje. Potom, ako duch skončí svoje skákanie, program čaká na kliknutie hráča na niektorý štvorec. 
Ak hráč klikne na štvorec, na ktorom sa duch zobrazil pri skákaní ako na poslednom štvorci, duch sa na tomto štvorci ukáže, vedľa neho sa zobrazí správa SUPER a hra končí. Ak hráč neklikol správne, duch sa zobrazí na štvorci, na ktorom sa zobrazil ako na poslednom a vedľa neho sa zobrazí správa TU SOM a hra skončí. Na obrázku je situácia, keď hráč klikol na iný štvorec ako na ten, kde videl ducha naposledy.
 
Obrázok ducha nájdeš v súbore duch.png.
"""

width = 1280
height = 720
root = Tk()
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()
canvas.configure(scrollregion=(-width / 2, -height / 2, width / 2, height / 2))
color = ["white", "lightgrey"]
M = randrange(2) + 3
N = randrange(4) + 3
duchimg = PhotoImage(file="./duch.png")

for m in range(M):
    for n in range(N):
        if int(m / 2) * 2 == m and int(n / 2) * 2 == n:
            r = 0
        elif int(m / 2) * 2 != m and int(n / 2) * 2 == n or int(m / 2) * 2 == m and int(n / 2) * 2 != n:
            r = 1
        else:
            r = 0
        canvas.create_rectangle(50 * n - 25, 50 * m - 25, 50 * n + 25, 50 * m + 25, fill=color[r])
duch = canvas.create_image(randrange(N) * 50, randrange(M) * 50, image=duchimg)
print(canvas.coords(duch))
print(M, N)
for i in range(randrange(2) + 3):
    x = randrange(N) * 50 - 25
    y = randrange(M) * 50 - 25
    canvas.moveto(duch, randrange(N) * 50 - 25, randrange(M) * 50 - 25)
    canvas.update()
    canvas.after(500)
canvas.moveto(duch, 9999, 9999)


def klik(arg):
    if x - 25 <= arg.x - width <= x + 25 and y - 25 <= arg.y - height<= y + 25:
        print("E")
        canvas.moveto(duch, x, y)
        canvas.create_text(x + 20, y - 20, text="SUPER")


root.bind("<Button-1>", klik)
mainloop()
