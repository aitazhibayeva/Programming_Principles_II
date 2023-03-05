# Write a Python program to write a list to a file.
lst = list(input().split())

with open('file.txt', 'w') as f:
    for word in lst:
    	f.write(word + '\n')
cntnt = open('file.txt')
f.close()

print(cntnt.read())