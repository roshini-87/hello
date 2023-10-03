import re
s = input()
digits = len(re.findall('[0-9]',s))
letters = len(re.findall('[A-z]', s))
print("Total letters found:",letters)
print("Total digits found :", digits)
