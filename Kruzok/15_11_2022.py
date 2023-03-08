import tkinter

canvas = tkinter.Canvas(width=750, height=750)
canvas.pack()
# auto
canvas.create_rectangle(100, 150, 200, 200, fill="lightblue", tags="auto")
canvas.create_oval(115, 200, 140, 225, fill="green", tags="auto")
canvas.create_oval(160, 200, 185, 225, fill="green", tags="auto")
# bicykel
canvas.create_oval(200, 100, 230, 130, fill="", width=5, tags="bicykel", outline="blue")
canvas.create_oval(250, 100, 280, 130, fill="", width=5, tags="bicykel", outline="blue")
canvas.create_line(215, 115, 230, 70, width=5, tags="bicykel")
canvas.create_line(225, 90, 240, 115, width=5, tags="bicykel")
canvas.create_line(265, 115, 270, 85, width=5, tags="bicykel")
canvas.create_line(265, 115, 240, 115, width=5, tags="bicykel")
canvas.moveto("auto", 20, 160)
canvas.moveto("bicykel", 40, 400)


def move():
    global x_auto
    global y_auto
    global x_bicykel
    global y_bicykel
    global x_auto_decrease
    global y_auto_decrease
    global x_bicykel_decrease
    global y_bicykel_decrease
    if x_auto_decrease == True:
        if 0 < x_auto < 250:
            canvas.move("auto", 1, 0)
            x_auto = x_auto + 1
        else:
            x_auto = x_auto - 1
            x_auto_decrease = False
    else:
        if 0 < x_auto < 250:
            canvas.move("auto", -1, 0)
            x_auto = x_auto - 1
        else:
            x_auto = x_auto + 1
            x_auto_decrease = True
    if y_auto_decrease == True:
        if 0 < y_auto < 250:
            canvas.move("auto", 0, 1)
            y_auto = y_auto + 1
        else:
            y_auto = y_auto - 1
            y_auto_decrease = False
    else:
        if 0 < y_auto < 250:
            canvas.move("auto", 0, -1)
            y_auto = y_auto - 1
        else:
            y_auto = y_auto + 1
            y_auto_decrease = True
    if x_bicykel_decrease == True:
        if 0 < x_bicykel < 750:
            canvas.move("bicykel", 1, 0)
            x_bicykel = + 1
        else:
            x_bicykel_decrease = False
    else:
        if 0 < x_bicykel < 750:
            canvas.move("bicykel", -1, 0)
            x_bicykel = - 1
        else:
            x_bicykel_decrease = True
    if y_bicykel_decrease == True:
        if 0 < y_bicykel < 750:
            canvas.move("bicykel", 0, 1)
            y_bicykel = + 1
        else:
            y_auto_decrease = False
    else:
        if 0 < y_bicykel < 750:
            canvas.move("bicykel", 0, -1)
            y_bicykel = - 1
        else:
            y_bicykel_decrease = True
    canvas.after(10, move)


x_auto = 20
y_auto = 160
x_bicykel = 40
y_bicykel = 400
x_auto_decrease = False
y_auto_decrease = False
x_bicykel_decrease = True
y_bicykel_decrease = True

move()
canvas.mainloop()
