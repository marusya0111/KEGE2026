a = []
for N in range(1,10_000):
    R = bin(N)[2:]
    R = R + str(R.count("1") % 2)
    #R = R + str(sum(int(i)for i in R) % 2)
    R = R + str(sum(map(int,R))%2 )
    R = int(R,2)
    if R >77:
        a.append(N)
print(min(a))

# test = "1234"
# print(*map(int,test))









