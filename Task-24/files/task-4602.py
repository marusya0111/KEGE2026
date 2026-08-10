# Текстовый файл состоит из символов А, В, С, D и О.
# Определите максимальное количество идущих подряд пар символов вида
# согласная + гласная в прилагаемом файле.

from re import finditer
with open (r'24_4602.txt') as file:
    data = file.readline()

#CACACA
pattern = r"([BCD][AO])+"
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches,key = len))/2)
#174
