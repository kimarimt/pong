from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coords):
        super().__init__()
        self.coords = coords
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.speed(0)
        self.setheading(90)
        self.goto(self.coords)

    def go_up(self):
        if self.ycor() < 215:
            y = self.ycor() + 10
            self.goto(self.coords[0], y)

    def go_down(self):
        if self.ycor() > -210:
            y = self.ycor() - 10
            self.goto(self.coords[0], y)

    def hit_ball(self, ball):
        ball.velocity *= 0.5
        return self.distance(ball.position()) < 20

