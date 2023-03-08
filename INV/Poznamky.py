"""
IP 193.87.160.18

Poznamky:
    // je znak delenia so zvyskom a outpt je pocet moznych deleni bez zvysku
    ** je umocnenie
    % delenia so zvyskom a output je zvysok
    ^ je nezname, mozno rozdiel medzi hodnotami?
    del
    vo While loop Continue ho resetne, break ukonci
"""
"""
string = ["Toast","Mlieko","Steblo"]
print(string)
x = len(string)
for i in range(x):
    temp = string.pop(0)
    temp = temp + " dreveny"
    string.append(temp)
    print(string)
print(string)
"""
"""
epiclist=[]
listlen = input("Input amount of values in list: ")
listlen =  int(listlen)
for i in range(listlen):
    inp = input("Input value of item in string: ")
    inp = str(inp)
    epiclist.append(inp)
print(epiclist)
"""
while True:
    x = input()
    x = int(x)
    y = x / 2
    y = int(y)
    z = y * 2
    z = int(z)
    if z == x:
        print("Cislo je parne")
    else:
        print("cislo je neparne")
    x = 0

