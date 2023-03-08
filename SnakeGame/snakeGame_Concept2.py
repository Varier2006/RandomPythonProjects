"""
Bola pridana hracia kocka ktora ale sa neuspesne upravuje podla velkosti okna
"""

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, width="1920", height="1080")
canvas.pack()
previous = 1
snake = []


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y


snakeHead = Snake(8, 8)
snake.append(snakeHead)


def keypressed(arg):
    global snake
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
    canvas.create_rectangle(-9999, -9999, 9999, 9999, fill="white", outline="white")
    print(size)
    for i in range(17):
        x11 = 16 + i * size
        y11 = 16
        x12 = 16 + i * size
        y12 = 16 + size - 15
        canvas.create_line(x11, y11, x12, y12 * 16)
        x21 = 16
        y21 = 16 + i * size
        x22 = 16 + size - 15
        y22 = 16 + i * size
        canvas.create_line(x21, y21, x22 * 16, y22)
    canvas.create_rectangle(snake[0].x * size - 26, snake[0].y * size - 26,
                            snake[0].x * size + 16, snake[0].y * size + 16,
                            fill="green")


repaintGrid(720 / 16 - 3)
root.bind("<Key>", keypressed)
root.bind("<Configure>", configured)
canvas.mainloop()
