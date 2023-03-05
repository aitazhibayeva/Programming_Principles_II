# Write a Python program with builtin function that returns True if all elements of the tuple are true.

t = (True, False, True)
print(all(t))

t = (True, True, True)
print(all(t))

t = (2, 4, 6)
print(all(t))
 
t = (0, False, False)
print(all(t))
 
t = (5, 0, 3, 1, False)
print(all(t))
 
t = ()
print(all(t))

