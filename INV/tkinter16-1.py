import tkinter

root = tkinter.Canvas(width=1280, height=720)
root.pack()

img = tkinter.PhotoImage(file="../img/screenshot1.png")
imge = img.zoom(3,3)
img = imge.subsample(2,2)
root.create_image(680, 360, image=img)
tkinter.mainloop()