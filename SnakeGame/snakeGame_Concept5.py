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

root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, width="1920", height="1080")
canvas.pack()
previous = 1
snake = []
gridOffset = 16
snakeLength = 1
size = 720 / 16 - 3
keypressede = "w"
keypressedi = ""


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
    global snake, snakeLength, size, keypressede, keypressedi
    if root.winfo_width() / root.winfo_height() >= 1:
        size = root.winfo_height() / 16 - 3
    else:
        size = root.winfo_width() / 16 - 3
    if arg.char == "w" or "a" or "s" or "d":
        keypressede = arg.char
    if arg.char == "q" or "e":
        keypressedi = arg.char


def configured(arg):
    global previous, size
    print(arg)
    if arg.width / arg.height >= 1:
        now = 1
    else:
        now = 0
    if previous != now:
        if arg.width > arg.height:
            size = arg.height / 16 - 3
        else:
            size = arg.width / 16 - 3


def repaintGrid():
    global gridOffset, snakeLength, keypressede, size, keypressedi
    canvas.create_rectangle(-9999, -9999, 9999, 9999, fill="white", outline="white")

    if keypressede == "w":
        print("UP")
        snake[0].y = snake[0].y - 1
    elif keypressede == "a":
        print("LEFT")
        snake[0].x = snake[0].x - 1
    elif keypressede == "s":
        print("DOWN")
        snake[0].y = snake[0].y + 1
    elif keypressede == "d":
        print("RIGHT")
        snake[0].x = snake[0].x + 1
    if keypressedi == "q":
        if not snakeLength <= 1:
            print("REMOVE")
            snakeLength = snakeLength - 1
    elif keypressedi == "e":
        if snakeLength <= len(snake) - 2:
            print("ADD")
            snakeLength = snakeLength + 1
    print(snake[0].x, snake[0].y)

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
        print(str(i) + " rev")
        snake[i + 1].x = snake[i].x
        snake[i + 1].y = snake[i].y

    canvas.after(1000, repaintGrid)


root.bind("<Key>", keypressed)
root.bind("<Configure>", configured)
repaintGrid()
canvas.mainloop()
