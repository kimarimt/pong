from os import scandir
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
player_1 = Paddle(coords=(-380, 0))
player_2 = Paddle(coords=(370, 0))
screen.tracer(True)

x_move = -10
y_move = 10
ball = turtle.Turtle()
ball.penup()
ball.color('white')
ball.shape('circle')
ball.shapesize(0.5)
ball.speed(0)

def move():
    x = ball.xcor() + x_move
    y = ball.ycor() + y_move
    screen.tracer(False)
    ball.goto(x, y)
    screen.tracer(True)

def bounce():
    global y_move
    if ball.ycor() > 230:
        y_move *= -1

if __name__ == '__main__':
    is_running = True

    screen.onkeypress(player_1.go_up, 'w')
    screen.onkeypress(player_1.go_down, 's')
    screen.onkeypress(player_2.go_up, 'Up')
    screen.onkeypress(player_2.go_down, 'Down')
    screen.listen()
    
    while is_running:
        screen.update()
        move()
        bounce()
