#Write a Python program to convert a given camel case string to snake case.
import re

def change_case(str):
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str).lower()

print(change_case("camelCaseString"))