from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('snake_game_update/data.txt', 'r') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.ht()
        self.penup()
        self.goto(0, 275)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(align=ALIGNMENT, font=FONT, arg=f'Score: {self.score} High Score: {self.high_score}')

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snake_game_update/data.txt', mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.write_score()

    def detect_score(self):
        self.score += 1
        self.write_score()


