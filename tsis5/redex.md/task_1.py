#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

def find(text):
    pattern = r'ab*'
    if re.search(pattern,  text):
        return 'Yes'
    else:
        return 'No'

print(find('abbb'))
print(find('ab'))
print(find('b'))
print(find('sabfc'))