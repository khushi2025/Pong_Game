from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#ffffff")
        self.penup()
        self.shapesize(1,1)
        self.xcord=10
        self.ycord=10
        self.move_speed=0.1


    def move(self):
        new_x=self.xcor()+self.xcord
        new_y=self.ycor()+self.ycord
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.ycord*=-1
    def bounce_x(self):
        self.xcord*=-1
        self.move_speed*=0.9
    def resume(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()



