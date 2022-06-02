from turtle import Turtle


class Drawer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.setheading(270)
        self.speed(0)
        self.draw_net()
        self.draw_scoreboard()

    def draw_net(self):
        self.goto(0, 240)
        while self.ycor() > -240:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(5)

    def draw_scoreboard(self):
        self.goto((-30, 180))
        self.write(f'0', align='center', font=('Arial', 52, 'normal'))
        self.goto((30, 180))
        self.write(f'0', align='center', font=('Arial', 52, 'normal'))
