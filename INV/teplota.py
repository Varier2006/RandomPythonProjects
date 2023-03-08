jednotka = input("Zadaj jednotku teploty:\n")
temp = input("Zadaj teplotu:\n")
temp = int(temp)
# zmenime teplotu na celzius
if jednotka == "K" or jednotka == "kelvin" or jednotka == "k":
    temp = temp - 273.15
elif jednotka == "F" or jednotka == "fahrenheit" or jednotka == "f":
    temp = (temp - 32) * 5 / 9
else:
    print("Bola zadana nespravana jednoka")
    exit(-1)
# zistime ci je teplota dostatocne vysoka
if temp > 0:
    print("Teplota je dostatocne vysoka.")
elif temp == 0:
    print("Teplota je 0 stupnov.")
elif temp < 0:
    print("Teplota je priliz nizka")
# float obmedzit na 2 des miesta
print(temp)
print("%.2f" % temp + " Stupnov Celzius")
# print("%.2f" % temp)
