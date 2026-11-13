from string import printable as alph
def conv(num,sys):
    res = ""
    while num:
        res = res + alph[num%sys]
        num = num//sys
    return res[::-1] if res else"0"

a = []
for N in [12]:
    R = conv(N,3)
    sumi = sum(map(int, R))
    if sumi % 3 == 0:
        R = R + "212"
    else:
        sumi = sumi * 2
        sumi = conv(sumi,3)
        R = R + sumi
    R = int(R,3)
print(R)
#     if R >490:
#         a.append(R)
# print(min(a))















