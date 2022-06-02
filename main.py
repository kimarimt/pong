import turtle
from drawer import Drawer


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = turtle.getscreen()
screen.title('Pong Game')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')

screen.tracer(False)
drawer = Drawer()
screen.tracer(True)


if __name__ == '__main__':
    is_running = True

    while is_running:
        screen.update()
