a = []
for N in range (1,10_000):
    R = bin(N)[2:]
    #sumi = sum(map(int,R))
    sumi = R.count("1")
    if sumi % 2 == 0:
        R = "11" + R[2:] + "1"
    else:
        if R.count("1") > R.count("0"):
            R = R + "0"
        else:
            R =R + "1"
    R = int(R,2)
    if R >271:
        a.append(N)
print(min(a))















