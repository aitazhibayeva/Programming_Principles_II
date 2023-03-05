# Write a Python program to list only directories, files and all directories, files in a specified path.
import os

pth = input()
def only_dir(pth):
	lst = []
	for i in os.listdir(pth):
		if os.path.isdir(os.path.join(pth, i)):
			lst.append(i)
	return lst

def only_file(pth):
	lst = []
	for i in os.listdir(pth):
		if os.path.isfile(os.path.join(pth, i)):
			lst.append(i)
	return lst

def both(pth):
	return os.listdir(pth)

print(*only_dir(pth))
print(*only_file(pth))
print(*both(pth))