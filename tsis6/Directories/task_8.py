# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

path = input()

if os.path.exists(path):
	print(os.access(path, os.F_OK), os.access(path, os.R_OK), os.access(path, os.W_OK), os.access(path, os.X_OK), end = ' ')
	os.remove(path)