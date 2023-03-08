"""
Experimentuje sa s predlzenim hracej kocky na hadika

Treba pridat:
    - moznost ked sa pojde do steny nech sa objavis na opacnej strane a pokracujes
    - aby vsetko bolo na cyklus, nech sa hybe podla predurceneho delay a nie podla inputu,
    input nech je iba suggestion ktorym smerom
    - nieco urobit s tym blbym zoznamom na telo
    - samozrejme dodad randomly generovane cervene policko co zvecsuje hadika a aj nejaky score counter
"""

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, width="1920", height="1080")
canvas.pack()
previous = 1
snake = []
gridOffset = 16
snakeLength = 1


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y


snakeHead = Snake(8, 8)
snake.append(snakeHead)
snake1 = Snake(8, 8)
snake.append(snake1)
snake2 = Snake(8, 8)
snake.append(snake2)
snake3 = Snake(8, 8)
snake.append(snake3)
snake4 = Snake(8, 8)
snake.append(snake4)
snake5 = Snake(8, 8)
snake.append(snake5)
snake6 = Snake(8, 8)
snake.append(snake6)
snake7 = Snake(8, 8)
snake.append(snake7)
snake8 = Snake(8, 8)
snake.append(snake8)
snake9 = Snake(8, 8)
snake.append(snake9)


def keypressed(arg):
    global snake, snakeLength
    if root.winfo_width() / root.winfo_height() >= 1:
        size = root.winfo_height() / 16 - 3
    else:
        size = root.winfo_width() / 16 - 3
    print(arg)
    print(arg.char)
    print(snake[0].x, snake[0].y)
    if arg.char == "w":
        print("UP")
        snake[0].y = snake[0].y - 1
    elif arg.char == "a":
        print("LEFT")
        snake[0].x = snake[0].x - 1
    elif arg.char == "s":
        print("DOWN")
        snake[0].y = snake[0].y + 1
    elif arg.char == "d":
        print("RIGHT")
        snake[0].x = snake[0].x + 1
    elif arg.char == "q":
        if not snakeLength <= 1:
            print("REMOVE")
            snakeLength = snakeLength - 1
    elif arg.char == "e":
        if snakeLength <= len(snake) - 2:
            print("ADD")
            snakeLength = snakeLength + 1
    print(snake[0].x, snake[0].y)
    repaintGrid(size)


def configured(arg):
    global previous
    print(arg)
    if arg.width / arg.height >= 1:
        now = 1
    else:
        now = 0
    if previous != now:
        if arg.width > arg.height:
            size = arg.height / 16 - 3
            repaintGrid(size)
        else:
            size = arg.width / 16 - 3
            repaintGrid(size)


def repaintGrid(size):
    global gridOffset, snakeLength
    canvas.create_rectangle(-9999, -9999, 9999, 9999, fill="white", outline="white")
    print(size)
    for row in range(16):
        for column in range(16):
            canvas.create_rectangle(gridOffset + column * size, gridOffset + row * size,
                                    gridOffset + column * size + size, gridOffset + row * size + size, fill="gray")
    for i in range(snakeLength):
        print(i)
        canvas.create_rectangle(gridOffset + snake[i].x * size - size, gridOffset + snake[i].y * size - size,
                                gridOffset + snake[i].x * size, gridOffset + snake[i].y * size,
                                fill="green")
    for i in reversed(range(snakeLength)):
        print(str(i)+" rev")
        snake[i+1].x = snake[i].x
        snake[i+1].y = snake[i].y


repaintGrid(720 / 16 - 3)
root.bind("<Key>", keypressed)
root.bind("<Configure>", configured)
canvas.mainloop()
