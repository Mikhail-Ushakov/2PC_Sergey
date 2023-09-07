import turtle

# screen = turtle.getscreen()
# t = turtle.Turtle()

# for i in range(50):
#     t.forward(45)
#     t.left(165)
#     t.forward(45)
#     t.right(175)

class Sq():
    def __init__(self, len, wid, color):
        self.len = len
        self.wid = wid
        self.color = color

    def draw(self):
        t.begin_fill()
        t.color(self.color)
        for i in range(2):
            t.forward(self.len)
            t.left(90)
            t.forward(self.wid)
            t.left(90)
        t.end_fill()

# len_ = abs(int(input('Введите длину'))) 
# wid_ = abs(int(input('Введите ширину')))
# color_ = input('Введите цвет на английском').lower()
# a = Sq(len_, wid_, color_)

class Tr():
    def __init__(self, len, color):
        self.len = len
        self.color = color
    
    def draw(self, t):
        t.begin_fill()
        t.color(self.color)
        for i in range(3):
            t.forward(self.len)
            t.left(120)
        t.end_fill()

# len__ = abs(int(input('Введите длину'))) 
# color__ = input('Введите цвет на английском').lower()
# b = Tr(len__, color__)

# b.draw()
if __name__ == '__main__':
    a = Sq(100, 60, 'red')
    a.draw()

    t.goto(0, -30)
    t.begin_fill()
    t.color('black')
    t.circle(30)
    t.end_fill()
    t.penup()


    t.goto(100, -30)
    t.pendown()
    t.begin_fill()
    t.color('black')
    t.circle(30)
    t.end_fill()
    t.penup()


    t.goto(0, -10)
    t.pendown()
    t.begin_fill()
    t.color('white')
    t.circle(10)
    t.end_fill()
    t.penup()


    t.goto(100, -10)
    t.pendown()
    t.begin_fill()
    t.color('white')
    t.circle(10)
    t.end_fill()








# screen.mainloop()