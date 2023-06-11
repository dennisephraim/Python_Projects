from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:

    def __init__(self):

        self.segments = []
        x = 0
        for i in range(0, 3):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=x, y=0)
            x -= 20
            self.segments.append(turtle)
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == 0:
            self.head.setheading(90)
        elif self.head.heading() == 180:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 0:
            self.head.setheading(270)
        elif self.head.heading() == 180:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 270:
            self.head.right(90)
        elif self.head.heading() == 90:
            self.head.left(90)

    def right(self):
        if self.head.heading() == 270:
            self.head.left(90)
        elif self.head.heading() == 90:
            self.head.right(90)
