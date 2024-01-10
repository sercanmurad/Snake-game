from turtle import Turtle

#Define alignment and font of the scoreboard
ALINGMENT="center"
FONT=("Arial", 22, "normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0,270)
        self.penup()
        self.color("white")
        self.hideturtle()

    def uptade_scoreboard(self):
        self.write(f"Score:{self.score}", align=ALINGMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game over!",align=ALINGMENT,font=FONT)
    def increase_score(self):
        self.score+=1
        self.clear()
        self.uptade_scoreboard()

