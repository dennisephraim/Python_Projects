from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.ht()
        self.penup()
        self.goto(0, 275)
        self.write_score()

    def write_score(self):
        self.write(align=ALIGNMENT, font=FONT, arg=f'Score: {self.score}')

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def detect_score(self):
        self.score += 1
        self.clear()
        self.write_score()


