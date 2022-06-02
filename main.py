import turtle
import time
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
        time.sleep(0.1)
        screen.update()
        ball.move()
        ball.bounce()
        ball.enters_goal()
        
        if player_1.hit_ball(ball) or player_2.hit_ball(ball):
            ball.x_move *= -1

        player, scored = ball.enters_goal()
        if scored:
            screen.tracer(False)
            drawer.update_score(player)
            screen.tracer(True)
            ball.reset()