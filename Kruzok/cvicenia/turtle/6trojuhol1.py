from turtle import *
from random import *

speed(20)

pencolor("#ffff90")
lis = []


def trojuhol(dlzka):
    fd(dlzka)
    rt(130)
    for i in range(13):
        fd(dlzka/13)
        rt(10)
    fd(dlzka*2)
    rt(100)
    # for a in range(2):
    #     for i in range(2):
    #         fd(dlzka * (1 + i))
    #         rt(120)


for m in range(5):
    rt(90)
    lis = ["#"]
    for i in range(6):
        lis.append(choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]))
    print("".join(str(e) for e in lis))
    pencolor("".join(str(e) for e in lis))
    for n in range(50):
        trojuhol((n + m * 10 + 3) * 10)
        setpos(0, 0)
        rt(10)
mainloop()
