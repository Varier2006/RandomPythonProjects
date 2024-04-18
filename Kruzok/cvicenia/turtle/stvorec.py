from turtle import *


def stvorec(dlzka):
    for i in range(4):
        fd(dlzka)
        rt(90)


for m in range(5):
    rt(90)
    for n in range(5):
        stvorec((n + m * 10 + 1) * 10)
        rt(180)
        stvorec((n + m * 10 + 1) * 10)
        rt(180)
mainloop()
