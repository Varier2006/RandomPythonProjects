def f():
    global foo
    print(foo)
    foo += 1

foo = 23
f()
print(foo)
