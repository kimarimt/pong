from turtle import Turtle
import random


class Ball(Turtle):
    speeds = [-10, 10]

    def __init__(self):
        super().__init__()
        self.x_move = random.choice(self.speeds)
        self.y_move = random.choice(self.speeds)
        self.penup()
        self.color('white')
        self.shape('circle')
        self.shapesize(0.5)
        self.speed(0)

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        if self.ycor() > 230:
            self.y_move *= -1
