def ParityParty(d):
    output = []
    if d % 2 == 0:
        output.append(0)
        output.append((int)(d/2))
    else:
        output.append(1)
        output.append((int)((d-1)/2))
    return output

num = int(input())
print(ParityParty(num))
