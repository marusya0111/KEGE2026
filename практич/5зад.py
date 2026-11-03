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
# a = []
# from string import printable as alph
# def conv(num,sys):
#     res = ""
#     while num:
#         res = res + alph[num%sys]
#         num = num//sys
#     return res[::-1] if res else"0"
#
# for N in range(1,1000):
#     R = conv(N,4)
#     if N % 4 == 0:
#         R = "2" + R + "03"
#     else:
#         ost = (N % 4)*5
#         ost_4 = conv(ost,4)
#         R = R + ost_4
#     R = int(R,4)
#     if R < 567:
#         a.append(N)
# print(max(a))



#
# r = "123456"
# print(r[:3])
