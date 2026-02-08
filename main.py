from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_controller import GameController
from config import SCREEN_SIZE


def main():
    screen = Screen()
    screen.setup(SCREEN_SIZE, SCREEN_SIZE)
    screen.bgcolor("black")
    screen.title("Snake Game (OOP)")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    controller = GameController(screen, snake, food, scoreboard)

    screen.listen()
    screen.onkey(lambda: snake.set_direction("UP"), "Up")
    screen.onkey(lambda: snake.set_direction("DOWN"), "Down")
    screen.onkey(lambda: snake.set_direction("LEFT"), "Left")
    screen.onkey(lambda: snake.set_direction("RIGHT"), "Right")

    controller.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
