A = [4, 8, 15, 16, 23, 42]
def D(i, n):
    if(A[i] % n == 0):
        return True
    else:
        return False


print(D(0, 2))
print(D(1, 3))
print(D(2, 3))
