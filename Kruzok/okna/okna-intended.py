import tkinter, random

canvas = tkinter.Canvas(width=30, height=255, bg='white')
canvas.pack()

sirka = 40
medz = 10
M = 4
N = 6
canvas['width'] = sirka / 2 + N * (sirka + medz)
canvas['height'] = sirka + 15 + M * (sirka + medz)

obr = []
for i in range(2):
    obr.append(tkinter.PhotoImage(file='okno' + str(i) + '.png'))

poz = []


def generuj():
    for rr in range(M):
        poz.append([])
        for ss in range(N):
            xx = medz + ss * (sirka + medz) + random.randrange(7)
            yy = medz + rr * (sirka + medz) + random.randrange(7)
            poz[-1].append([xx, yy])


def kresli():
    for rr in range(M):
        for ss in range(N):
            canvas.create_image(poz[rr][ss][0], poz[rr][ss][1], image=obr[0], anchor='nw')
    for ss in range(N):
        canvas.create_text(sirka - 10 + ss * (sirka + medz), M * (sirka + medz) + 5, text=str(ss), font='arial 15',
                           anchor='nw')


done = []


def randg():
    global vchod, posch
    vchod = random.randrange(N)
    posch = random.randrange(M)
    for a in range(len(done)):
        if done[a][1] == vchod and done[a][0] == posch:
            if len(done) == M*N:
                print("konec")
                canvas.create_text(10, M/5*2 * (sirka + medz) + 30, text='WIN',
                           font='arial 15', anchor='nw')
                return
            else:
                randg()


def klik(event):
    rrkto = -1
    sskto = -1
    global vchod, posch, done
    x = event.x
    y = event.y
    for rr in range(M):
        for ss in range(N):
            if poz[rr][ss][0] < x < poz[rr][ss][0] + sirka and poz[rr][ss][1] < y < poz[rr][ss][1] + sirka:
                rrkto = rr
                sskto = ss
    if rrkto == posch and sskto == vchod:
        canvas.create_image(poz[rrkto][sskto][0], poz[rrkto][sskto][1], image=obr[1], anchor='nw')
        done.append([rrkto, sskto])
        randg()
        canvas.itemconfig(idtxt, text='vchod: ' + str(vchod) + ' poschodie: ' + str(M - posch))


generuj()
vchod = random.randrange(N)
posch = random.randrange(M)
idtxt = canvas.create_text(10, M * (sirka + medz) + 30, text='vchod: ' + str(vchod) + ' poschodie: ' + str(M - posch),
                           font='arial 15', anchor='nw')
kresli()
canvas.bind('<Button-1>', klik)
canvas.mainloop()

[
    [
        [13, 16],
        [64, 16],
        [113, 15],
        [162, 10],
        [212, 14],
        [260, 15]
    ],
    [
        [13, 61],
        [61, 63],
        [112, 63],
        [160, 63],
        [214, 65],
        [263, 61]
    ],
    [
        [10, 110],
        [65, 116],
        [111, 111],
        [165, 112],
        [210, 113],
        [265, 114]
    ],
    [
        [11, 166],
        [63, 162],
        [111, 162],
        [160, 166],
        [216, 160],
        [264, 165]
    ]
]
