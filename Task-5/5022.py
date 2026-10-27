a = []
for N in range(1,10_000):
    R = bin(N)[2:]
    if N % 3 == 0:
        #R = R + R[-3]+ R[-2] + R[-1]
        R = R + R [:-3:]
    else:
        ost = (N%3)*3
        ost_2 = bin(ost)[2:]
        R = R + str(ost_2)
    R = int(R, 2)
    if R > 151:
        a.append(R)
print(min(a))













