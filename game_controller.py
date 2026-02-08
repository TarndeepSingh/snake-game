import time
from config import WALL_LIMIT, INITIAL_SPEED


class GameController:
    def __init__(self, screen, snake, food, scoreboard):
        self.screen = screen
        self.snake = snake
        self.food = food
        self.scoreboard = scoreboard
        self.speed = INITIAL_SPEED
        self.running = True

    def update(self):
        while self.running:
            time.sleep(self.speed)
            self.screen.update()
            self.snake.move()
            self._check_collisions()

    def _check_collisions(self):
        # Food collision
        if self.snake.head.distance(self.food) < 15:
            self.food.refresh()
            self.snake.grow()
            self.scoreboard.increase()
            self.speed *= 0.97  # dynamic difficulty

        # Wall collision
        x, y = self.snake.head.xcor(), self.snake.head.ycor()
        if abs(x) > WALL_LIMIT or abs(y) > WALL_LIMIT:
            self._game_over()

        # Self collision
        if self.snake.collided_with_self():
            self._game_over()

    def _game_over(self):
        self.running = False
        self.scoreboard.game_over()
