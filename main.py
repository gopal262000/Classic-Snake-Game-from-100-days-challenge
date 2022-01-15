import turtle as t
import time
from snake import Snake
from food import Food
from scorecard import ScoreCard

screen = t.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreCard()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extent()
        food.refresh()

    # collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 265 or snake.head.ycor() < -290:
        score.game_over()
        game_is_on = False

    # detecting the collision with its own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False


screen.exitonclick()
