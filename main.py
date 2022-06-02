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

paddle = turtle.Turtle()
paddle.penup()
paddle.color('white')
paddle.shape('square')
paddle.shapesize(stretch_wid=1, stretch_len=3)
paddle.setheading(90)
paddle.goto(-380, 0)

def go_up():
    if paddle.ycor() < 215:
        paddle.forward(10)

def go_down():
    if paddle.ycor() > -210:
        paddle.backward(10)

computer = paddle.clone()
computer.goto(370, 0)

def move():
    if computer.ycor() < 215:
        while computer.ycor() < 215:
            computer.forward(5) 
    else:
        while computer.ycor() > -210:
            computer.backward(5)


if __name__ == '__main__':
    is_running = True
    
    screen.onkey(go_up, 'w')
    screen.onkey(go_down, 's')
    screen.listen()

    while is_running:
        screen.update()
        move()
