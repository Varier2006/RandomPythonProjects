def fixed(x, y=0):
    nejakyList = []
    if y != 0:
        z = y - 1
        x = x - 1
        while z > x:
            nejakyList.append(z)
            z = z - 1
    else:
        z = x
        while z > 0:
            z = z - 1
            nejakyList.append(z)
    return reversed(nejakyList)
