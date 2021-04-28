from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick_manager import BrickManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Breakout")
screen.tracer(0)

bricks = BrickManager()
paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

game_over = False

while not game_over:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with walls:
    if ball.xcor() >= 380 or ball.xcor() <= -380:
        ball.bounce_x()

    # Detect collision with ceiling:
    if ball.ycor() > 380:
        ball.bounce_y()

    # Detect collision with bricks:
    for brick in bricks.all_bricks:
        if ball.distance(brick) < 30:
            bricks.all_bricks.remove(brick)
            brick.goto(-3000, -3000)
            ball.bounce_y()

    # Detect collision with paddle:
    if ball.distance(paddle) < 60 and -350 < ball.ycor() < -320:
        ball.bounce_y()

    # Detect paddle misses:
    if ball.ycor() < -370:
        ball.reset_position((paddle.xcor(), paddle.ycor() + 30))
        scoreboard.lose_a_life()
        if scoreboard.lives == 0:
            game_over = True

    # Level completed:
    if not bricks.all_bricks:
        # Progress to next level --> Redraw bricks, increase speed
        bricks.refresh_bricks()
        ball.reset_position((paddle.xcor(), paddle.ycor() + 30))
        scoreboard.next_level()
        ball.move_speed *= 0.9


# Lives depleted:
scoreboard.game_over()

screen.exitonclick()
