import math
def sequence_slayer(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    a = 1
    b = 2
    c = 0
    for i in range(2, n + 1):
        c = pow(i, 2) * b - a
        a = b
        b = c
    return c

print(sequence_slayer(2))
print(sequence_slayer(3))
print(sequence_slayer(8))
