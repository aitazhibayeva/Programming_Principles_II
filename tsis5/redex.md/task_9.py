#Write a Python program to insert spaces between words starting with capital letters.
import re

def space(text):
    pattern = r'[A-Z]{1}[a-z]*'
    tt = re.findall(pattern, text)
    text = ' '.join(tt)
    return text

print(space('WordsStartingWithCapitalLetters'))