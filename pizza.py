import turtle
from random import randint
from turtlee import Tr

screen = turtle.getscreen()
t = turtle.Turtle()

t.color('brown')
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(0, 8)

t.pendown()
t.color('yellow')
t.begin_fill()
t.circle(92)
t.end_fill()

a = Tr(10, 'green')

for i in range(20):
    t.penup()
    t.goto(0,100)
    t.left(randint(0,360))
    t.forward(randint(0,92))
    # t.pendown()
    a.draw(t)

    t.penup()
    t.goto(0,100)
    t.left(randint(0,360))
    t.forward(randint(0,92))
    t.pendown()
    t.color('red')
    t.begin_fill()
    t.circle(5)
    t.end_fill()

screen.mainloop()