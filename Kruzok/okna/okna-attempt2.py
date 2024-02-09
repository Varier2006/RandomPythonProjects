from tkinter import *

ww = 800
wh = 480
root = Tk()
root.geometry(f"{ww}x{wh}")
canvas = Canvas(root, width=ww, height=wh)
canvas.pack()

x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 2, 3, 4]
lit = []
contains = False
width = 50
size = 75
wo = ww / 4
ho = wh / 5

for i in x:
    for ii in y:
        canvas.create_rectangle(wo + i * size, ho + ii * size, wo + i * size + width, ho + ii * size + width, fill="white")


def klik(pos):
    print(f"{pos.x}x{pos.y}")
    print(f"{x}x{y}")
    for i in x:
        for ii in y:
            if wo + i * size < pos.x < wo + i * size + width and ho + ii * size < pos.y < ho + ii * size + width:
                print(f"{i}x{ii}")
                if f"{i}x{ii}" in lit:
                    lit.remove(f"{i}x{ii}")
                    canvas.create_rectangle(wo + i * size, ho + ii * size, wo + i * size + width,
                                            ho + ii * size + width, fill="white")
                else:
                    lit.append(f"{i}x{ii}")
                    canvas.create_rectangle(wo + i * size, ho + ii * size, wo + i * size + width,
                                            ho + ii * size + width, fill="pink")
                print(lit)


root.bind("<Button-1>", klik)

canvas.mainloop()
