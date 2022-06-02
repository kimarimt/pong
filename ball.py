from turtle import Turtle
import random


class Ball(Turtle):
    speeds = [-5, 5]

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
        if self.ycor() > 230 or self.ycor() < -230:
            self.y_move *= -1

    def enters_goal(self):
        if self.xcor() < -400:
            return 'player_2', True
        elif self.xcor() > 400:
            return 'player_1', True
        else:
            return '', False

    def reset(self):
        self.x_move = random.choice(self.speeds)
        self.y_move = random.choice(self.speeds)
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.move()

