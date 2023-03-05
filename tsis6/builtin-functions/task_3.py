# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
stt = input()

if stt == stt[::-1]:
    print("Is palindrome")
else:
    print("Is not palindrome")
