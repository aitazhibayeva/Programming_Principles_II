# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os
pth = input()

print(os.access(pth, os.F_OK), os.access(pth, os.R_OK), os.access(pth, os.W_OK), os.access(pth, os.X_OK))