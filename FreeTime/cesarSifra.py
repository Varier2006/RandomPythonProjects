inpur = "cgjqt dcchh"
out = ""
a = 0
w = 0
# while a < 200:
#     print(f"{chr(a)} {a}")
#     a += 1
# a = 0
while a < 25:
    out = ""
    for i in inpur:
        t = ord(i)
        if t == 32:
            w = t
        elif 64 < t < 91 and (t + 1 + a) > 90 or t + 1 + a > 122 and 96 < t < 123:
            w = t + 1 + a - 25
        else:
            w = t + 1 + a
        # print(f"{t},{chr(t)};{w},{chr(w)}")
        out += chr(w)
    print(out)
    # print("_____")
    a += 1
