def cardinality(A, B, U):
    cnt = 0
    for i in A:
        for j in B:
            if i == j:
                cnt = cnt + 1
    a = len(U) - cnt
    ans = pow(2, a)
    return ans

A = {0, 1, 2}
B = {1, 3}
U = {0, 1, 2, 3, 4}
print(cardinality(A, B, U))
