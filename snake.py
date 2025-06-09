
from turtle import Turtle

class Snack_body:
    def __init__(self):
        self.turtles=[]
        self.positions=[(-80,0),(-60,0),(-40,0),(-20,0),(0,0)]
        self.making()
        self.head=self.turtles[-1]
    
    def making(self):
        for i in range(len(self.positions)):
            new_turtle=Turtle("square")
            new_turtle.penup()
            new_turtle.goto(self.positions[i])
            self.turtles.append(new_turtle)

    def move(self):
        for i in range (len(self.turtles) - 1):
            self.turtles[i].goto(self.turtles[i + 1].pos())
        self.head.forward(20)
    
    
    # this is a function to add a new turtle

    def add(self):
        back_turtle=Turtle("square")
        back_turtle.color("black")
        back_turtle.penup()
        back_turtle.goto(self.turtles[0].pos())
        self.turtles.insert(0,back_turtle)
    

    def up(self):
        self.head.setheading(90)
    
    def down(self):
        self.head.setheading(270)
    
    def right(self):
        self.head.setheading(0)
    
    def left(self):
        self.head.setheading(180)
