#Write a Python program to convert a given camel case string to snake case.
import re

def change_case(str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    print(s1)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

print(change_case("geeksForGeeks"))