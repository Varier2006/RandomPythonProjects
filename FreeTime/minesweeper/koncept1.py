from tkinter import *
from random import *

ww = 1280
wh = 720
root = Tk()
root.geometry(f"{ww}x{wh}")

grid = []
boom = 0
tem = [-1, 1]


def show():
    global grid, boom
    grid = []
    boom = 0
    x = ""
    y = ""
    half = False

    for i in clicked.get():
        if i == "x":
            half = True
        elif half:
            y += str(i)
        else:
            x += str(i)
    x = int(x)
    y = int(y)
    for a in range(x):
        grid.append([])
        for b in range(y):
            if randint(0, int(x * y / 2)) < (x + y) / 3 * 2:  # tweak probability
                grid[-1].append(1)
                boom += 1
            else:
                grid[-1].append(0)
    if x * y / 2 > boom > (x + y) / 3 * 2:  # set happy conditions
        # pod tymto sa snazim urobit check preto aby v strede nebolo mozne 8, mal by som dat ze ked je check pozitivny tak deletne rovno dva, ten kde je a jeden random okolo neho.
        # tiez by sa hodil check pre edges nech to neni annoying ze musis tipovat
        for c in range(len(grid)):
            for d in range(len(grid[c])):
                # co tuto vycookujem bude moj peak
                boomcheck = 0
                edgecheck = ""  # r,tr,tl,l,bl,br; ze right, left, top left etc.
                if d + 1 > len(grid[c]):
                    edgecheck = "t"
                if d - 1 < 0:
                    edgecheck = "b"
                if c + 1 > len(grid):
                    edgecheck += "r"
                if c - 1 < 0:
                    edgecheck += "l"

                if edgecheck == "r":
                    if grid[c - 1][d] == 1:
                        boomcheck += 1
                    if grid[c - 1][d + 1] == 1:
                        boomcheck += 1
                    if grid[c - 1][d - 1] == 1:
                        boomcheck += 1
                    if grid[c][d + 1] == 1:
                        boomcheck += 1
                    if grid[c][d - 1] == 1:
                        boomcheck += 1
                    if boomcheck == 5:
                        grid[c][d] = 0
                        grid[c - randint(0, 1)][d + tem[randint(0, 1)]] = 0
                if edgecheck == "l":
                    if grid[c + 1][d] == 1:
                        boomcheck += 1
                    if grid[c + 1][d + 1] == 1:
                        boomcheck += 1
                    if grid[c + 1][d - 1] == 1:
                        boomcheck += 1
                    if grid[c][d + 1] == 1:
                        boomcheck += 1
                    if grid[c][d - 1] == 1:
                        boomcheck += 1
                    if boomcheck == 5:
                        grid[c][d] = 0
                        grid[c + randint(0, 1)][d + tem[randint(0, 1)]] = 0
                if edgecheck == "t":
                    if grid[c - 1][d] == 1:
                        boomcheck += 1
                    if grid[c + 1][d] == 1:
                        boomcheck += 1
                    if grid[c + 1][d - 1] == 1:
                        boomcheck += 1
                    if grid[c - 1][d - 1] == 1:
                        boomcheck += 1
                    if grid[c][d - 1] == 1:
                        boomcheck += 1
                    if boomcheck == 5:
                        grid[c][d] = 0
                        grid[c + tem[randint(0, 1)][d - randint(0, 1)]] = 0
                    # continue tomorrow, snad si budes pametat ako. b,bl,br,tl,tr. pametat ze c je Left-Right a d je Top-Down

        draw()
    else:
        show()


def draw():
    offset = 2
    size = 25
    canvas.config(width=len(grid) * size + offset, height=len(grid[0]) * size + offset)
    canvas.delete("all")
    for c in range(len(grid)):
        for d in range(len(grid[c])):
            if grid[c][d] == 0:
                canvas.create_rectangle(offset + c * size, offset + d * size, offset + c * size + size,
                                        offset + d * size + size, fill="white")
            elif grid[c][d] == 1:
                canvas.create_rectangle(offset + c * size, offset + d * size, offset + c * size + size,
                                        offset + d * size + size, fill="red")


options = [
    "10x10",
    "15x15",
    "20x20",
    "25x25"
]
clicked = StringVar()
clicked.set("10x10")
OptionMenu(root, clicked, *options).pack()
Button(root, text="Set size", command=show).pack()


def box(pos, occupation):
    # som sprostost vyrobil, neviem co je lepsie pri dynamic size gridu, ci list alebo iba string decode. Radsej to cez list urobit a cez loops ho generovat.
    x = ""
    y = ""
    half = False
    for i in pos:
        if i == "x":
            half = True
        elif half:
            y += str(i)
        else:
            x += str(i)
    y = int(y)
    x = int(x)


canvas = Canvas(root, width=ww, height=wh)
canvas.pack()

root.mainloop()
