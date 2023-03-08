import tkinter

canvas = tkinter.Canvas(width=750, height=750, background="black")
canvas.pack()
x = 0
y = 0
neco = False
necot = False
lisx = []
lisy = []


def robot(x, y):
    canvas.delete("all")
    canvas.create_line(x + 50, y + 110, x + 10, y + 175, fill="gray", width=20)
    canvas.create_line(x + 100, y + 110, x + 140, y + 175, fill="gray", width=20)
    canvas.create_rectangle(x + 50, y + 50, x + 100, y + 100, fill="white")
    canvas.create_rectangle(x + 40, y + 100, x + 110, y + 200, fill="green")
    canvas.create_rectangle(x + 40, y + 200, x + 70, y + 275, fill="red")
    canvas.create_rectangle(x + 80, y + 200, x + 110, y + 275, fill="blue")


def callback(e):
    if neco:
        # canvas.after(200)
        x = e.x
        y = e.y
        print("Pointer is currently at %d, %d" % (x, y))
        robot(x - 75, y - 75)
    elif necot:
        lisx.append(e.x)
        lisy.append(e.y)
    elif not necot:
        #postupne nech sa hibe z listu x y a potom ich removeovat
        x = e.x
        y = e.y
        print("Pointer is currently at %d, %d" % (x, y))
        robot(x - 75, y - 75)


def Button1Pressed(olo):
    olo = 0
    global neco
    neco = True


def Button1Released(olo):
    olo = 0
    global neco
    neco = False


def Button3Pressed(olo):
    olo = 0
    print("button 2 press")
    global necot
    necot = True


def Button3Released(olo):
    olo = 0
    print("button 2 release")
    global necot
    necot = False


canvas.bind('<Motion>', callback)
canvas.bind("<ButtonPress-1>", Button1Pressed)
canvas.bind("<ButtonRelease-1>", Button1Released)
canvas.bind("<Double-Button-3>", quit)
canvas.bind("<ButtonPress-3>", Button3Pressed)
canvas.bind("<ButtonRelease-3>", Button3Released)
canvas.mainloop()
