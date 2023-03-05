# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def countLower(st):
    cnt = 0
    for i in st:
        if i.islower():
            cnt += 1
    return cnt

def countUpper(st):
    cnt = 0
    for i in st:
        if i.isupper():
            cnt += 1
    return cnt

st = input()
print(f'num of uppercase: {countUpper(st)}')
print(f'num of lowercase: {countLower(st)}')