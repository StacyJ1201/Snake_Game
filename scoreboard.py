from turtle import Turtle
alignment = 'center'
font = 'arial'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=alignment, font=(font, 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over! \nFinal score is: {self.score}", align=alignment, font=(font, 40, 'normal'))

