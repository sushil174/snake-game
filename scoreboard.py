from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align="center",font=("Arial", 24 ,"normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER.", align="center",font=("Arial", 24 ,"normal"))
