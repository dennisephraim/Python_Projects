from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

paddle = Paddle()
r_paddle = paddle.paddle1
l_paddle = paddle.paddle2
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle.paddle1_up, "Up")
screen.onkey(paddle.paddle1_down, "Down")
screen.onkey(paddle.paddle2_up, "w")
screen.onkey(paddle.paddle2_down, "s")

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 450:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -450:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()