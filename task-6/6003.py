from turtle import *

screensize(10_000,10_000)
tracer(0)
lt(90)
mash = 10

for i in range(2):
    fd(10*mash)
    rt(90)
    fd(20*mash)
    rt(90)
up()
fd(3*mash)
right(90)
fd(7*mash)
left(90)
down()
for i in range(2):
    fd(70*mash)
    right(90)
    fd(90*mash)
    right(90)

for x in range(7,21):
    for y in range(3,11):
        teleport(x*mash,y*mash)
        dot(3,"red")


print(14*8)
update()
done()