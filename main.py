import turtle
from drawer import Drawer
from paddle import Paddle
from ball import Ball


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = turtle.getscreen()
screen.title('Pong Game')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')

screen.tracer(False)
drawer = Drawer()
player_1 = Paddle(coords=(-380, 0))
player_2 = Paddle(coords=(370, 0))
ball = Ball()
screen.tracer(True)


if __name__ == '__main__':
    is_running = True

    screen.onkeypress(player_1.go_up, 'w')
    screen.onkeypress(player_1.go_down, 's')
    screen.onkeypress(player_2.go_up, 'Up')
    screen.onkeypress(player_2.go_down, 'Down')
    screen.listen()

    while is_running:
        screen.update()
        ball.move()
        ball.bounce()
