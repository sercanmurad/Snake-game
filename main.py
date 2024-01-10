from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

"""We define screen options with using of a Screen class from turtle"""
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Score()

#Use screen listen and onkey functions to move the snake
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



"""Create a game"""
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    #Use move function to move snake
    snake.move()



    #Detect collusion with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect collusion with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collusion with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on=False
            scoreboard.game_over()













screen.exitonclick()