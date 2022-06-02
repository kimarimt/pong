import turtle


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = turtle.getscreen()
screen.title('Pong Game')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.color('white')
drawer.setheading(270)
drawer.speed(0)
drawer.goto(0, 240)


def draw_net():
    while drawer.ycor() > -240:
        drawer.pendown()
        drawer.forward(15)
        drawer.penup()
        drawer.forward(5)


score = 0


def draw_scoreboard():
    drawer.goto((-30, 180))
    drawer.write(f'{score}', align='center', font=('Arial', 52, 'normal'))
    drawer.goto((30, 180))
    drawer.write(f'{score}', align='center', font=('Arial', 52, 'normal'))


if __name__ == '__main__':
    is_running = True

    draw_net()
    draw_scoreboard()

    while is_running:
        screen.update()
