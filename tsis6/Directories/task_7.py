# Write a Python program to copy the contents of a file to another file

with open('file.txt', 'r') as f1, open('file2.txt', 'w') as f2:
    for line in f1:
        f2.write(line)