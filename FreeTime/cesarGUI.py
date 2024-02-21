from tkinter import *

width = 1280
height = 720
root = Tk()
root.resizable(True, True)

text = Text(root, height=20)
text.pack()
label = Label(root, text="d")
label.pack()
mainloop()
