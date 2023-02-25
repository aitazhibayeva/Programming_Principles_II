#Write a python program to convert snake case string to camel case string.
import re

def camelCase(text):
    tt = text.split('_')
    tt = [x.capitalize() for x in tt]
    tt[0] = tt[0].lower()
    tt = ''.join(tt)
    return tt

print(camelCase('snake_case_string'))
print(camelCase('camel_case_string'))