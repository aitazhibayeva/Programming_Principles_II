#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

def find(text):
    text = re.sub('[\s,.]', ':', text)
    return text
    
    
print(find('Write a Python program to replace all occurrences of space, comma, or dot with a colon.')) 