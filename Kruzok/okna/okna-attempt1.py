from tkinter import *
from random import *

# je to funkcne ale nastal problem s coordinates, nejak to vymysliet treba

ww = 1280
wh = 720
root = Tk()
root.geometry(f"{ww}x{wh}")
canvas = Canvas(root, width=ww, height=wh)
canvas.pack()

x = [10, 20, 30, 40, 50, 60]
y = [10, 20, 30, 40]
width = 50
size = 75
wo = ww / 4
ho = wh / 5

for i in x:
    for ii in y:
        print(int(str(i)[0]))
        canvas.create_rectangle(wo + int(str(i)[0]) * size, ho + int(str(ii)[0]) * size,
                                wo + int(str(i)[0]) * size + width, ho + int(str(ii)[0]) * size + width)


def klik(pos):
    print(f"{pos.x}x{pos.y}")
    print(f"{x}x{y}")
    for i in x:
        for ii in y:
            if wo + int(str(i)[0]) * size < pos.x < wo + int(str(i)[0]) * size + width and ho + int(str(ii)[0]) * size < pos.y < ho + int(str(ii)[0]) * size + width:
                print(f"{i}x{ii}")
                print(f"{int(str(i)[1])}s{int(str(ii)[1])}")
                if int(str(i)[1]) == 1 or int(str(ii)[1]) == 1:
                    canvas.create_rectangle(wo + int(str(i)[0]) * size, ho + int(str(ii)[0]) * size,
                                wo + int(str(i)[0]) * size + width, ho + int(str(ii)[0]) * size + width)
                    for a in range(len(x)):
                        if i == x[a]:
                            x[a] = x[a] - 1
                    for a in range(len(y)):
                        if ii == y[a]:
                            y[a] = y[a] - 1
                if int(str(i)[1]) == 0 or int(str(ii)[1]) == 0:
                    canvas.create_rectangle(wo + int(str(i)[0]) * size, ho + int(str(ii)[0]) * size,
                                wo + int(str(i)[0]) * size + width, ho + int(str(ii)[0]) * size + width,
                                            fill="pink")
                    for a in range(len(x)):
                        if i == x[a]:
                            x[a] = x[a] + 1
                    for a in range(len(y)):
                        if ii == y[a]:
                            y[a] = y[a] + 1
                print(f"{x}x{y}")


root.bind("<Button-1>", klik)

canvas.mainloop()
