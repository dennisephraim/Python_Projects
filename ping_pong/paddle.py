from turtle import Turtle


TURTLE_POSITION = [(350, 0), (-350, 0)]


class Paddle:
    def __init__(self):
        self.paddles = []
        self.create_paddle()
        self.paddle1 = self.paddles[0]
        self.paddle2 = self.paddles[1]

    def add_paddle(self, position):
        paddle = Turtle()

        paddle.shape('square')
        paddle.turtlesize(stretch_wid=5, outline=5, stretch_len=1)
        paddle.penup()
        paddle.color("white")
        paddle.goto(position)

        self.paddles.append(paddle)

    def create_paddle(self):
        for position in TURTLE_POSITION:
            self.add_paddle(position)

    def paddle1_up(self):
        self.paddle1.goto(350, self.paddle1.ycor() + 20)

    def paddle1_down(self):
        self.paddle1.goto(350, self.paddle1.ycor() - 20)

    def paddle2_up(self):
        self.paddle2.goto(-350, self.paddle2.ycor() + 20)

    def paddle2_down(self):
        self.paddle2.goto(-350, self.paddle2.ycor() - 20)





