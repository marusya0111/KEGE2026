from string import printable as alph
def conv(num,sys):
    res = ""
    while num:
        res = res + alph[num%sys]
        num = num//sys
    return res[::-1] if res else"0"

num = 4*625**9 - 25**15 + 2*5**11 -7
print(conv(num,5).count("4"))
########################################
num = 4*625**9 - 25**15 + 2*5**11 - 7
cnt = 0
while num:
    if num % 5 == 4: cnt += 1
    num //= 5
print(cnt)
