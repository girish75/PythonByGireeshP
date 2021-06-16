import re
string = "Is Search inside of this text search please"
#simple way
print('Search' in string)
print('search' in string)

a = re.search('search', string) # exact match not found so None
print(a)
a = re.search('Search', string)
print(a)
print(a.span())
print(a.start())
print(a.end())
print(a.group()) # useful.. will see later

print('================ pattern checking ========== https://regex101.com/')
pattern = re.compile(r"[sS]earch")
a = pattern.search(string)
print("Search is = ", a)
a = pattern.findall(string)
print("find all = ", a)
string1 = "Search"
a = pattern.fullmatch(string1)
print(a)
a = pattern.match(string)
print(a)
print('================ Password checking ========== https://regex101.com/')
""" Criteria: 
At least 8 char long
Contain any sort letters, numbers, $%#@
"""
# pylint
# pyflakes






