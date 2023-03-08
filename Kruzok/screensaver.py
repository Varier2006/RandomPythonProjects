import tkinter
import random
import time

# canvas = tkinter.Canvas(width=750,height=750,bg="black")
root = tkinter.Tk()
# canvas.pack()
root.attributes("-fullscreen", True)
root.configure(background="black")
button = tkinter.Button(root, command=root.destroy)
button.config(width=750, height=750, background="black", activebackground="black", borderwidth=0)
button.pack()
root.mainloop()