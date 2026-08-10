# Текстовый файл состоит из символов А, В и С.
# Определите максимальное количество идущих подряд пар символов АВ или АС
# в прилагаемом файле.
# Для выполнения этого задания следует написать программу

from re import finditer
with open(r"24_2942.txt") as file:
    data = file.readline()

# t_1 = ACACACABBAAC
pattern = r"(A[CB])+"
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches, key = len))/2)
#2397
