import turtle

screen = turtle.getscreen()
t = turtle.Turtle()

class Re():
    def __init__(self, len):
        self.len = len
    def draw(self, color, x, y):
        t.begin_fill()
        t.color(color)
        t.goto(x,y)
        for _ in range(4):
            t.forward(self.len)
            t.left(90)
        t.end_fill()

a = Re(40)
a.draw('red', 80, 0)
a.draw('yellow', 40, 0)
a.draw('green', 0, 0)



























screen.mainloop()