from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Your Score is {self.score}", align="center", font=('Arial', 24, 'normal'))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 24, 'normal'))


    def updatescore(self):
        self.score +=1
        self.clear()
        self.write(f"Your Score is {self.score}", align="center", font=('Arial', 24, 'normal'))


