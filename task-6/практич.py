from turtle import *
tracer(0)
screensize(10_000,10_000)
k = 10

for i in range(8):
    fd(16*k)
    rt(90)
    fd(22*k)
    rt(90)

up()
fd(5*k)
rt(90)
fd(5*k)
lt(90)
down()

for i in range(8):
    fd(52*k)
    rt(90)
    fd(77*k)
    rt(90)

for x in range(5,17):
    for y in range(-22,-4):
        teleport(x*k,y*k)
        dot(3,"red")
update()
done()