import math
def wrangle_rectangles(m, n):
    sum = 0
    for i in range(0, m):
        pi = m - i
        for j in range(0, n):
            pj = n - j
            sum = sum + pi * pj
    return sum

print(wrangle_rectangles(1, 1))
print(wrangle_rectangles(2, 1))
