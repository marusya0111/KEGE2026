from re import finditer
test_1 = 'P****P'
test_2 = "P****P***P"
test_3 = "***P****P****"
test_4 = "***P*P*P"
test_5 = "P****P****P***"



with open (r"24_1975.txt", encoding ="utf-8") as file:
    data = file.readline()

pattern = r"[^P]*(P[^P]+)+P[^P]*"

matches = [match.group() for match in finditer (pattern, data)]
a = []
print(len(max(matches, key = len )))















