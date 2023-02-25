#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

def find(text):
    pattern = r'a{1}.*b$'
    if re.search(pattern, text):
        return 'Yes'
    else:
        return 'No'
        
print(find('ab'))
print(find('Acaasdsb'))
print(find('DFHKJsdadfgj_lkk_b'))
print(find('AASDasda'))