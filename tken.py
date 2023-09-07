from tkinter import *
from time import sleep
root = Tk()
root.title('Cube')

canvas = Canvas(root, width = 600, height = 600)
canvas.pack()

class Circle:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.size = 50
        self.speed_x = 3
        self.speed_y = 2
        self.canvas_size = 600
        self.object = canvas.create_oval(self.x,self.y,self.size,self.size, fill = 'red', dash=[30, 7 , 255, 255])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        canvas.move(self.object, self.speed_x, self.speed_y)
        self.check_collision()

    def check_collision(self):
        pos = canvas.coords(self.object)
        if pos[0] <= 0 or pos[2] >= 600:
            self.speed_x = self.speed_x * -1
        elif pos[1] <= 0 or pos[3] >= 600:
            self.speed_y = self.speed_y * -1

c = Circle()

while True:
    c.move()
    
    root.update()
    sleep(0.05)









root.mainloop()