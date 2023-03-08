"""
Button() Label() Entry() Scale()
https://www.tutorialspoint.com/python/python_gui_programming.htm
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
f"#{var:02x}"
"""

from tkinter import *

root = Tk()
root.geometry("1280x720")
canvas = Canvas(root, width="500", height="800")
canvas.pack(side="top")

press = False


def but():
    global press
    if not press:
        button.config(text="Z")
        press = True
    else:
        button.config(text="E")
        press = False


def square():
    global redScale, greenScale, blueScale
    col = f"#{redScale.get():02x}{greenScale.get():02x}{blueScale.get():02x}"
    canvas.config(background=col)


button = Button(canvas, text="E", command=but, activebackground="#206080", cursor="pencil")
button.pack()

redScale = Scale(canvas, to=255, label="Red", orient="horizontal")
greenScale = Scale(canvas, to=255, label="Green", orient="horizontal")
blueScale = Scale(canvas, to=255, label="Blue", orient="horizontal")
redScale.pack()
greenScale.pack()
blueScale.pack()
button2 = Button(canvas, text="Comm", command=square, activebackground="#206080", cursor="pencil")
button2.pack()

canvas.mainloop()
