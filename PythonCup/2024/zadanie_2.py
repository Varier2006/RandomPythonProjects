from tkinter import *
from random import *
"""
Poradie machúľ
Po štarte programu sa v ľavej časti zobrazia 4 machule uložené na sebe v náhodnom poradí. Úlohou hráča je klikať na farebné štvorce v dolnej časti v rovnakom poradí v akom program uložil machule na seba od najspodnejšej (1.) po najvrchnejšiu (4.) machuľu. V pravej časti sa postupne skladajú machule na seba podľa toho, v akom poradí hráč kliká na farebné štvorce.
Keď hráč klikne na farebný štvorec v dolnej časti, štvorec sa presunie k najmenšiemu ešte neurčenému poradiu. Teda po prvom kliknutí k číslici 1, po druhom kliknutí k číslici 2 atď. Zároveň sa v pravej časti zobrazí machuľa príslušnej farby a umiestni sa ako vrchná machuľa. Týmto spôsobom reagujú na kliknutie len štvorce v dolnej časti, štvorce pri čísliciach sa nedajú odstraňovať ani premiestňovať.
Na našom obrázku vidíme situáciu, v ktorej hráč už určil poradie pre dve farby. Ako na prvý v poradí klikol na modrý štvorec. Tento štvorec sa po kliknutí presunul k číslici 1 a vpravo sa zobrazila ako prvá modrá machuľa. Potom hráč klikol na oranžový štvorec. Tento štvorec sa presunul k číslici 2 a vpravo sa na modrú machuľu umiestnila oranžová. Teraz hráč zrejme klikne na červený a nakoniec na zelený štvorec. Tým sa umiestnia aj zvyšné dve machule a program už ďalej nereaguje. Hráč si môže porovnaním ľavého a pravého obrázka vizuálne skontrolovať, či určil správne poradie ukladania machúľ. Program poradie nekontroluje.
Obrázky machúľ sú pripravené v súboroch machula0.png až machula3.png. Aby bolo dobre vidieť prekrývanie, umiestni machule na začiatku na súradnice (v poradí machúľ): [260,90], [200,110], [260,60], [160,70], použi umiestenie anchor='nw'. Machuliam vpravo zväčši x-ovú súradnicu napr. o 350.
Farebné štvorce sú v súboroch stvorec0.png až stvorec3.png. Číslice pre poradie machúľ vypíš programom.
"""
canvas = Canvas(width=1280, height=720, background="lightgrey")
canvas.pack()

machule = []
machule1 = []
for i in range(4):
    machule.append(PhotoImage(file='machula' + str(i) + '.png'))
    machule1.append(PhotoImage(file='machula' + str(i) + '.png'))
stvorce = []
for i in range(4):
    stvorce.append(PhotoImage(file='stvorec' + str(i) + '.png'))
shuffle(machule)
canvas.create_image(260, 90, image=machule[0], anchor='nw')
canvas.create_image(200, 110, image=machule[1], anchor='nw')
canvas.create_image(260, 60, image=machule[2], anchor='nw')
canvas.create_image(160, 70, image=machule[3], anchor='nw')
for i in range(4):
    canvas.create_text(20, 60 * (i + 1), text=f"{i}.", font="Arial 20")
for i in range(4):
    canvas.create_image(100 + 60 * (i + 1), 400, image=stvorce[i])
done = []


def klik(arg):
    print(done)
    for i in range(4):
        if 100 + 60 * (i + 1) - 25 <= arg.x <= 100 + 60 * (
                i + 1) + 25 and 400 - 25 <= arg.y <= 400 + 25 and i not in done:
            canvas.create_image(80, 60 * (len(done) + 1), image=stvorce[i])
            canvas.create_rectangle(100 + 60 * (i + 1) - 25, 400 - 25, 100 + 60 * (i + 1) + 25, 400 + 25,
                                    fill="lightgrey",
                                    outline="lightgrey")
            done.append(i)
            if len(done) == 1:
                canvas.create_image(560, 90, image=machule1[i], anchor='nw')
            if len(done) == 2:
                canvas.create_image(500, 110, image=machule1[i], anchor='nw')
            if len(done) == 3:
                canvas.create_image(560, 60, image=machule1[i], anchor='nw')
            if len(done) == 4:
                canvas.create_image(460, 70, image=machule1[i], anchor='nw')


canvas.bind("<Button-1>", klik)
mainloop()
