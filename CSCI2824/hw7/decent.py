def common_decency(num):
    cnt3 = 0
    cnt5 = 0
    while not(num == 0):
        d = num % 10
        if d == 3:
            cnt3 = cnt3 + 1
        elif d == 5:
            cnt5 = cnt5 + 1
        else:
            return False
        num = num // 10
    if cnt3 % 5 == 0 and cnt5 % 3 == 0:
        return True
    return False

print(common_decency(2))
print(common_decency(555))
print(common_decency(53535))
