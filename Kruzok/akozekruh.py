import tkinter
import random
import time

canvas = tkinter.Canvas(width=750, height=750, background="black")
canvas.pack()
# hourglass
"""
x = 0
y = 520
z = 0
for i in range(1,26):
    canvas.create_line(x+z,y-z+10,x-z+510,y-z,fill="yellow")
    z = z + 20    
    canvas.update()
    canvas.after(100)
"""
x = 0
y = 0
y1 = 20
x1 = 520
cycle1 = False
cycle2 = True
cycle3 = True
cycle4 = True
end = False
while not end:
    if not cycle1:
        x = x + 20
        y = y + 20
        if x == 540 and y == 540:
            x = 520
            y = 520
            cycle1 = True
            cycle2 = False
    elif not cycle2:
        y1 = y1 + 20
        x1 = x1 - 20
        if x1 == 0 and y1 == 540:
            x1 = 20
            y1 = 520
            cycle2 = True
            cycle3 = False
    elif not cycle3:
        y = y - 20
        x = x - 20
        if x == 0 and y == 0:
            x = 20
            y = 20
            cycle3 = True
            cycle4 = False
    elif not cycle4:
        y1 = y1 - 20
        x1 = x1 + 20
        if x1 == 520 and y1 == 20:
            x1 = 520
            y1 = 0
            cycle4 = True
    else:
        end = True
    canvas.create_line(x, y1, x1, y, fill="yellow")
    canvas.update()
    canvas.after(50)
tkinter.mainloop()