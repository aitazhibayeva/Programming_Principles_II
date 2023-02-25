#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

def find(text):
    pattern = r'ab{2,3}'
    if re.search(pattern, text):
        return "Yes"
    else:
        return "No"

print(find('abbb'))
print(find('ab'))
print(find('ba'))
print(find('sabbbfc'))