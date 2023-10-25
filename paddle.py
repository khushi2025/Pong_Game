from turtle import Turtle,Screen
class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.xcord=x
        self.ycord=y
        self.shape("square")
        self.color("#ffffff")
        self.speed("fastest")
        self.shapesize(5, 1)
        self.penup()
        self.goto(self.xcord,self.ycord)

    def up(self):
        self.new_y=self.ycor()+20
        self.goto(self.xcord,self.new_y)

    def down(self):
        self.new_y=self.ycor()-20
        self.goto(self.xcord,self.new_y)



