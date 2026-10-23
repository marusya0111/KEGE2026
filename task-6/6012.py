# from turtle import *
#
# screensize(10_000, 10_000)
# tracer(0)
# lt(90)
# m = 15
#
# for i in range(2):
#     fd(13 * m)
#     rt(90)
#     fd(20 * m)
#     rt(90)
#
# up()
# fd(8 * m)
# rt(90)
# bk(3 * m)
# lt(90)
# down()
#
# for i in range(2):
#     fd(16 * m)
#     rt(90)
#     fd(8 * m)
#     rt(90)
#
# for x in range(0, 6):
#     for y in range(8, 14):
#         teleport(x * m, y * m)
#         dot(3, 'red')
#
# print(14*21+17*9-6*6)
# update()
# done()


from turtle import *
tracer(0)
k = 10
rt(90)
screensize(10_000,10_000)

lt(90)
for i in range(2):
    fd(25*k)
    rt(90)
    fd(10*k)
    rt(90)

fd(3*10)
lt(90)
fd(15*k)
for i in range(2):
    fd(9*k)
    rt(90)
    fd(32*k)
    rt(90)

for x in range(-15,18):
    for y in range(-5,26):
        teleport(x*k,y*k)
        dot(3,"red")



# print(10*33)
# print(26*11)
# print()


update()
done()