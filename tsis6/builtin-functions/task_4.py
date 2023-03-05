# Write a Python program that invoke square root function after specific milliseconds.

import time
number = int(input())
after = int(input())
result = number**0.5
time.sleep(after/100)
print(f"Square root of {number} after {after} miliseconds is {result}") 