def powerSet(set):
    ans = []
    l = len(set)
    lp = pow(2, l)
    for pi in range(0, lp):
        arr = []
        tpi = pi
        cnt = 0;
        while not(tpi == 0):
            if(tpi % 2 == 1):
                arr.append(set[cnt])
            cnt = cnt + 1
            tpi = tpi // 2
        ans.append(arr)
    return ans

A = [0, 1, 2]
B = ['a', 'b', 'c', 'd']
print(powerSet(B))
