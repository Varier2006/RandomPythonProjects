import drandom
import mojRange
y = 0
z = 0
"""
for i in mojRange(100):
    c = 0
    for f in mojRange(100):
        x = random.randrange(1000)
        y = y + x
        print(x)
    print(f"Hotovo, konecna suma je {y}")
    c = y / 100
    print(f"priemer je {c}")
    z = z + c
z = z / 100
print(f"priemer konecny je {z}")
"""
for i in mojRange.fixed(10,13):
    print(i)