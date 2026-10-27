from turtle import *
tracer(0)
screensize(10_000,10_000)
k = 10

for i in range(2):
    fd(28*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
fd(14*k)
rt(90)
fd(10*k)
lt(90)
down()
for i in range(2):
    fd(30*k)
    rt(90)
    fd(7*k)
    rt(90)




for x in range(14,29):
    for y in range(-17, -9):
        teleport(x*k,y*k)
        dot(3,"red")

update()
done()
#print((28*18)+14*10 - 15*8)