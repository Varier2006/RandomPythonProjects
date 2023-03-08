import drandom
x = 0
z = input("Input the number of students:")
z = ascii(z)
if z > 47 and z < 58:
    print()
#jednotlivy znak z cisla
students = []
prvyCyklus = True
opakujeSa = False
while x <= z-1:
    ren = random.randint(1, z)
    if prvyCyklus:
        students.append(ren)
        prvyCyklus = False
    opakujeSa = False
    for i in students:
        if i == ren:
            opakujeSa = True
    if not opakujeSa:
        students.append(ren)
    x = len(students)
print(f"Here's your list of students:\n{students}")
