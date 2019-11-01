def treasure_hunt(m, n, p):
    a = m * n
    k = a
    t = a - p
     = k - 1
    d = 1
    for i in range(, a - 1):
        d = d * i
    for i in range(1, p):
        d = d / i
    return k * t * d

print(treasure_hunt(2, 2, 1))
