from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, is_computer, coords):
        super().__init__()
        self.is_computer = is_computer
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.setheading(90)
        self.goto(coords)

    def go_up(self):
        if self.ycor() < 215:
            self.forward(10)

    def go_down(self):
        if self.ycor() > -210:
            self.backward(10)

    def move(self):
        if self.is_computer:
            if self.ycor() < 215:
                while self.ycor() < 215:
                    self.forward(5)
            else:
                while self.ycor() > -210:
                    self.backward(5)
