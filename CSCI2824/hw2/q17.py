def Odd(n):
    if(n % 2 == 1):
        return True
    return False

def check_proposition(array):
    for i in array:
        if Odd(i):
            flag = True
            for j in array:
                if i == j - 1 :
                    flag = False
                    break
            if flag == True:
                return False
    return True

print(check_proposition([-2, -1, 0, 1, 2]))

print(check_proposition([-2, -1, 0, 1, 3, 4]))
