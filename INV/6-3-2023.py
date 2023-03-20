from tkinter import *
from random import *

root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, width="1280", height="695", background="#000000")
canvas.pack(side="bottom")


def cycle():
    global red, redGoal, green, greenGoal, blue, blueGoal, rand
    if rand == 0:
        if blue <= blueGoal:
            blue = blue + 1
            print(f"blue{blue}")
        elif red <= redGoal:
            red = red + 1
            print(f"red{red}")
        elif green <= greenGoal:
            green = green + 1
            print(f"green{green}")
        col = f"#{red:02x}{green:02x}{blue:02x}"
    elif rand == 1:
        if red <= redGoal:
            red = red + 1
            print(f"red{red}")
        elif blue <= blueGoal:
            blue = blue + 1
            print(f"blue{blue}")
        elif green <= greenGoal:
            green = green + 1
            print(f"green{green}")
        col = f"#{red:02x}{green:02x}{blue:02x}"
    elif rand == 2:
        if green <= greenGoal:
            green = green + 1
            print(f"green{green}")
        elif blue <= blueGoal:
            blue = blue + 1
            print(f"blue{blue}")
        elif red <= redGoal:
            red = red + 1
            print(f"red{red}")
        col = f"#{red:02x}{green:02x}{blue:02x}"

    if blue >= blueGoal and red >= redGoal and green >= greenGoal:
        print("konec")
        colorChange()
        return
    canvas.config(background=col)
    canvas.after(5, cycle)


def colorChange(d=""):
    global red, redGoal, green, greenGoal, blue, blueGoal, rand
    print("colorChangeINIT")
    red = 0
    blue = 0
    green = 0
    redGoal = randrange(50, 255)
    greenGoal = randrange(50, 255)
    blueGoal = randrange(50, 255)
    rand = randrange(3)
    print(rand)
    if rand == 0:
        redGoal = 0
    elif rand == 1:
        greenGoal = 0
    elif rand == 2:
        blueGoal = 0
    print(redGoal)
    print(greenGoal)
    print(blueGoal)
    cycle()
    print(f"random{rand}")


button = Button(root, text="Initiate Color Change", command=colorChange)
button.pack(side="bottom")
root.bind("<Key>", colorChange)
canvas.mainloop()
