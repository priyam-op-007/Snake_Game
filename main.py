from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("The Famous Snake Game")
my_screen.tracer(0)
snake = Snake()
khana = Food()
score = Scoreboard()
my_screen.listen()
my_screen.onkeypress(snake.up, "Up")
my_screen.onkeypress(snake.left, "Left")
my_screen.onkeypress(snake.down, "Down")
my_screen.onkeypress(snake.right, "Right")


game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(khana) < 15:
        khana.refresh()
        score.increase_score()
        snake.extend()
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
    for segments in snake.snakes[1:]:

        if snake.head.distance(segments) < 10:
            game_is_on = False
score.final_score()

my_screen.exitonclick()
