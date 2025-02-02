from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from restart_game import RestartGame

def main_game():
    screen.setup(width=500, height=500)
    screen.bgcolor("black")
    screen.title("Snake game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
            game_is_on = False
            scoreboard.game_over()

        for segment in snake.turtles:
            if segment != snake.head and snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

screen = Screen()
restart = RestartGame(screen, main_game)
main_game()
screen.mainloop()