from turtle import Turtle,Screen
from snake import Snake_body
import time
from food import Food 
from score import Score_board


window=Screen()
window.setup(800,800)
sam=Snake_body()
window.tracer(0)
food = Food()
score=Score_board()


game_on=True
while game_on:
    sam.move()
    
    window.update()
    time.sleep(.1)
    window.listen()

    window.onkey(sam.up,"Up")
    window.onkey(sam.down,"Down")
    window.onkey(sam.right,"Right")
    window.onkey(sam.left,"Left")

    if sam.head.distance(food) < 15:
        food.appear()
        sam.add()
        score.new_points()
    if sam.head.xcor() < -370 or sam.head.xcor() > 370 or sam.head.ycor() > 370 or sam.head.ycor() < -370:
        game_on=False
        score.game_over()
    
    for pieces in sam.turtles[:-1]:
        if sam.head.distance(pieces) <10:
            game_on = False
            score.game_over()
window.exitonclick()
