from turtle import Turtle



WIDTH = 5
HEIGHT = 1




class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=HEIGHT, stretch_wid=WIDTH)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)














