from turtle import *


def trojuhol(dlzka):
    for i in range(3):
        fd(dlzka)
        rt(60)


for m in range(5):
    rt(90)
    for n in range(5):
        trojuhol((n + m * 2 + 1) * 10)
        rt(60)
mainloop()
