stop = ["S", "t", "o", "p"]
text = "String nejaka veta.StopDalsia veta.StopEste Dalsia veta."


def Vety(tex):
    fin = ""
    skip4 = 0
    list1 = []
    final = []
    list1[:0] = tex
    num = 1
    final.append(str(num)+". ")
    for i in range(len(list1)):
        if list1[i] == stop[0] and list1[i + 1] == stop[1] and list1[i + 2] == stop[2] and list1[i + 3] == stop[3]:
            skip4 = 4
        if skip4 == 4:
            num = num + 1
            final.append("\n"+str(num)+". ")
        if skip4 > 0:
            skip4 = skip4 - 1
        else:
            final.append(list1[i])
    for ele in final:
        fin += ele
    return fin


print(Vety(text))
