import turtle

turtle.down()
turtle.speed(speed=0)
turtle.screensize(canvwidth=800, canvheight=800, bg=None)

x = 0
y = 0
while y<5:
    turtle.forward(100)
    while x<18:
        turtle.forward(50)
        turtle.circle(10,extent = 180)
        turtle.right(160)
        turtle.backward(50)
        x = x + 1
    turtle.right(160) 
    turtle.forward(100)
    x=0
    y=y+1

turtle.done()

        