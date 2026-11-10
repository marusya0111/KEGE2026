# a = []
# for N in range(4,1000):
#     R = bin(N)[2:]
#     if N % 2 == 0:
#         R = R + R[:3]
#     else:
#         R = "1" + R + "01"
#     R = int(R,2)
#     if R >600:
#         a.append(R)
# print(min(a))
a = []
# from string import printable as alph
# def conv(num,sys):
#     res = ""
#     while num:
#         res = res + alph[num%sys]
#         num = num//sys
#     return res[::-1] if res else"0"

for N in range(1,1000):
    R = bin(N)[2:]
    if N % 8 == 0:
        R = R + R[-2:]
    else:
       osti = (N % 8)*2
       osti_2 = bin(osti)[2:]
    R = int(R,3)
    if R > 3000:
        a.append(N)
print(min(a))



#
# r = "123456"
# print(r[-3:])
