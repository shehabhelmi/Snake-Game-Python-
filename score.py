from turtle import Turtle
class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.update_score()
    def update_score(self):
        self.goto(0,370)
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))

    def new_points(self):
        self.clear()
        self.score +=1
        self.update_score()

    def game_over(self):
        self.screen.bgcolor("darkred")
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=("Arial",30,"normal"))
