a = []
for N in range(1,10_000):
    R = bin(N)[2:]
    if N % 2 ==0:
        R = "11" + R + "11"
    else:
        R = "1" + R + "00"
    R = int(R,2)
    if R <= 113:
        a.append(R)
print(max(a))
