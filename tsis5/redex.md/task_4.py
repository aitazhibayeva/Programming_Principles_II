#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

def find(text):
    pattern = r'[A-Z]{1}+[a-z]+'
    if re.search(pattern, text):
        return 'Yes'
    else:
        return 'No'

print(find('ab'))
print(find('Acasdasd'))
print(find('AASDasda'))
print(find('faSd'))