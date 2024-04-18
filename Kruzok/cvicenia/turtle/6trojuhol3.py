from turtle import *
from random import *

speed(200)

pencolor("#cf00c0")
# lis = ["#"]
# for i in range(6):
#     lis.append(choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]))
# print("".join(str(e) for e in lis))
# pencolor("".join(str(e) for e in lis))


def kruh(velkost):
    fd(velkost /2 / 3.14)
    rt(90)
    for i in range(36):
        fd(velkost)
        rt(10)
    rt(60)
    for b in range(4):
        for i in range(12):
            fd(velkost)
            rt(10)
        rt(120)


for m in range(50):
    kruh((m + 1)*1)
mainloop()
