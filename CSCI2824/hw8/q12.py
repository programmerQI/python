import math
def treasure_hunt(m, n, p):
    a = m * n
    k = m * n - p
    d = math.factorial(a) / math.factorial(a - p) / math.factorial(p)
    t = a - p
    return int(k * d * t)

print(treasure_hunt(3, 4, 2))
