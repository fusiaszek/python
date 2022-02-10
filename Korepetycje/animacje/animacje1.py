import turtle
import random
screen = turtle.Screen()
screen.setup(500,600)
screen.tracer(0)
don = turtle.Turtle()
screen.bgcolor('black')
screen.title('Stars')
don.color('yellow')
don.speed(0)
don.width(3)
don.hideturtle()
don.penup()
don.pendown()
listakropek=['red','orange','yellow']
def kropka():
    don.color(random.choice(listakropek))
    don.penup()
    don.goto(random.randint(-200,200),random.randint(-250,250))
    don.pendown()
    don.circle(1)
    don.color('yellow')
def gwiazda():
    i=0
    while i<5:
        i+=1
        don.forward(50)
        don.right(144)
gwiazda()
screen.update()
don.right(90)
polozenie1=random.randint(-200,200),500
polozenie2=random.randint(-200,200),500
polozenie3=random.randint(-200,200),500
predkosc1=random.randint(50,150)/100
predkosc2=random.randint(50,150)/100
predkosc3=random.randint(50,150)/100

don.color('yellow')
don.fillcolor('yellow')

def gwiazdawypelnienie(polozenie):
    don.penup()
    don.goto(polozenie)
    don.pendown()
    don.begin_fill()
    gwiazda()
    don.end_fill()
while True:
    don.clear()
    kropka()
    gwiazdawypelnienie(polozenie1)
    gwiazdawypelnienie(polozenie2)
    gwiazdawypelnienie(polozenie3)
    screen.update()
    polozenie1=polozenie1[0],polozenie1[1]-predkosc1
    polozenie2=polozenie2[0],polozenie2[1]-predkosc2
    polozenie3=polozenie3[0],polozenie3[1]-predkosc3
    if polozenie1[1]<-600:
        polozenie1=random.randint(-200, 200),500
    if polozenie2[1]<-600:
        polozenie2=random.randint(-200, 200),500
    if polozenie3[1]<-600:
        polozenie3=random.randint(-200, 200),500