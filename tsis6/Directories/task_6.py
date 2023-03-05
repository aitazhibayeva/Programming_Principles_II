# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

for i in range(26):
    with open(f"{chr(i+65)}.txt", 'w') as f:
	    f.write('')