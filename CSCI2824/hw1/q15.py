def DecToBin(b):
    output = []
    if b == 0:
        output.append(0)
        return output
    while b > 0 :
        output.insert(0, b % 2)
        b //= 2
    return output

num = int(input())
print(DecToBin(num))
