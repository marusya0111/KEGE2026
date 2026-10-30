from turtle import *
tracer(0)
screensize(10_000,10_000)

k = 10

for i in range(5):
    fd(13*k)
    rt(90)
    fd(5*k)

up()
rt(90)
fd(10*k)
lt(90)
fd(7*k)
down()

for i in range(2):
    fd(8*k)
    rt(90)
    fd(11*k)
    rt(90)



for x in range(-5,4):
    for y in range(-18,-11):
        teleport(x*k,y*k)
        dot(3,"red")



update()
done()
