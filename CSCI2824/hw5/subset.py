def check_subset(set, sub):
    if (not set) or (not sub):
        return True
    for i in sub:
        mark = False
        for j in set:
            if i == j:
                mark = True
        if mark == False:
            return False
    return True

A = []
B = [1, 2, 3, 4]
print(check_subset(A, B))
