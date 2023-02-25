#Write a Python program to convert a given camel case string to snake case.
import re

def snakeСase(text):
    text = [text[0].upper()]
    pattern = r'[A-Z]{1}[a-z]*'
    tt = re.findall(pattern, text).lower()
    text = '_'.join(tt)
    text = [x.lower() for x in text]
    return text


print(snakeСase("camelCaseString"))