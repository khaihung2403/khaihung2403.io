def f(a, L=[]):
    L.append(a)
    return L
f(1)
f(2, [])
print(f(3))