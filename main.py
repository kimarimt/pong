from calendar import c
import turtle
from drawer import Drawer
from paddle import Paddle


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = turtle.getscreen()
screen.title('Pong Game')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')

screen.tracer(False)
drawer = Drawer()
player = Paddle(coords=(-380, 0))
computer = Paddle(coords=(370, 0))
screen.tracer(True)


if __name__ == '__main__':
    is_running = True

    screen.onkey(player.go_up, 'w')
    screen.onkey(player.go_down, 's')
    screen.listen()

    while is_running:
        screen.update()
        computer.move()
