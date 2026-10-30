from string import printable as alph

def conv (num,sys):
    res = ""
    while num:
        res = res + alph[num%sys]
        num = num//sys
    return res[::-1] if res else "0"

a = []
for N in range(1,1000):
    R = conv(N,3)
    if N % 3 == 0:
        R = "1" + R + "02"
    else:
        osti = (N % 3)*4
        osri_3 = conv(osti,3)
        R = R + osri_3
    R = int(R,3)
    if R <199:
        a.append(N)
print(max(a))
