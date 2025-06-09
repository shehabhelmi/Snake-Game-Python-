from turtle import  Turtle 
import random 
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5,0.5)
        self.penup()
        self.appear()

    def appear(self):
        random_x=random.randint(-380,380)
        random_y=random.randint(-380,380)
        self.goto (random_x,random_y)
