from turtle import Turtle
import random
from config import WALL_LIMIT


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.6, 0.6)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-WALL_LIMIT, WALL_LIMIT)
        y = random.randint(-WALL_LIMIT, WALL_LIMIT)
        self.goto(x, y)
