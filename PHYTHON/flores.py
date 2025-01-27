import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t= turtle.Turtle()
t.shape("turtle")
t.speed(10)

def petal():
    t.circle(100,60)
    t.left(120)
    t.circle(100,60)
    t.left(120)
    
for _ in range(6):
    petal()
    t.right(60)
    
t.penup()
t.goto(0, -40)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(40)
t.end_fill()


t.hideturtle()

turtle.done()