# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

pth = input()

if os.path.exists(pth):
	print("Exists")
	print(os.path.basename(pth))
	print(os.path.dirname(pth))
else:
    print("Not exists")