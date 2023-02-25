#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

def find(text):
    pattern = r'^[a-z]+_[a-z]+$'
    if re.search(pattern, text):
        return 'Yes'
    else:
        return 'No'

print(find('asd_asdf'))
print(find('asdsf'))
print(find('asf_'))