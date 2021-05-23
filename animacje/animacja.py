import turtle

screen = turtle.Screen()
screen.setup(500,500)
screen.tracer(0)

don = turtle.Turtle()
don.color('red')
don.speed(0)
don.width(3)
don.hideturtle()


don.penup()
don.goto(-350, 0)
don.pendown()

while True :
    don.clear()
    don.fillcolor('red')
    don.begin_fill()
    don.circle(100)
    don.end_fill()
    screen.update()
    don.forward(100)
    if don.xcor()>500:
        don.goto(-350,0)

