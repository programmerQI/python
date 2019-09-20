def Vowel(c):
    if(c == "A" or c == "E" or c == "I" or c == "O" or c == "U"):
        return True
    return False

def Even(n):
    if(n % 2 == 0):
        return True
    return False

def ABCs(letters, numbers):
    for i in range(len(letters)):
        if(Even(numbers[i]) and (not Vowel(letters[i]))):
                return False
    return True

letters = ['A', 'B', 'C']
numbers = [1, 2, 3]
print(ABCs(letters, numbers))

letters = ['A', 'A', 'A', 'A']
numbers = [1, 2, 3, 4]
print(ABCs(letters, numbers))

letters = ['Z', 'A', 'I', 'I', 'B', 'U']
numbers = [1, 20, 4, 16, 123, 100]
print(ABCs(letters, numbers))
