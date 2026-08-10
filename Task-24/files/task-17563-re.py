# 7*8-900
# 07-5*100
# 1-*7
# -78-789
# *98
# 0*7

#положительный (1- бесконечности) неотрицательный (0- бесконечсномти)
from re import finditer
with open ("24_17563.txt") as file:
    data = file.readline()

number = r"[7-9][07-9]*"
pattern = rf"({number}[-*])+{number}"

matches = [match.group() for match in finditer(pattern,data)]
print((len(max(matches,key = len))/2))
#20