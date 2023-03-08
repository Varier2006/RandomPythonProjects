import drandom
import tkinter

lis = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
color = []
root = tkinter.Canvas(width=1280, height=720, background="#7a7a7a")
root.pack()
while True:
    color = "#"
    for i in range(6):
        run = random.randrange(15)
        color = color + lis[run]
    root.config(background=color)
    #nejak displaynut color name v strede
    root.delete("text")
    root.create_text(680, 360, text=color, tags="text", font="bolder")
    root.pack()
    print(color)
    root.update()
    root.after(250)
#mainloop asi netreba Hmm
tkinter.mainloop()
# var = f"#{value1:02x}{value2:02x}{value3:02x}"
