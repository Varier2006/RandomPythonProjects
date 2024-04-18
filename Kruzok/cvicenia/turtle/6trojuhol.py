from turtle import *


def trojuhol(dlzka):
    for a in range(3):
        for b in range(2):
            for i in range(2):
                fd(dlzka)
                rt(130)
            fd(dlzka)
        rt(60)


for m in range(5):
    rt(90)
    for n in range(5):
        trojuhol((n + m * 10 + 1) * 10)
        rt(60)
mainloop()
