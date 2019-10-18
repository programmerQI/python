def selSort(list):
    l = len(list)
    cnt = 0
    for i in range(0, l):
        min = list[i]
        id = i;
        for j in range(i + 1, l):
            cnt = cnt + 1
            if list[j] < min:
                cnt = cnt + 2
                min = list[j]
                id = j
        a = list[i]
        list[i] = min
        list[id] = a
        cnt = cnt + 3
    return (list, cnt)

print(selSort([2, 1]))
print(selSort([3, 2, 1]))
