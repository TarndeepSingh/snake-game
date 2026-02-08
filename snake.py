from turtle import Turtle
from config import STEP, START_LENGTH


class Snake:
    def __init__(self):
        self.segments = []
        self._create_snake()
        self.head = self.segments[0]
        self.direction = "RIGHT"

    def _create_snake(self):
        for i in range(START_LENGTH):
            self._add_segment((-i * STEP, 0))

    def _add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(STEP)

    def grow(self):
        self._add_segment(self.segments[-1].pos())

    def set_direction(self, new_direction):
        opposites = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }
        if opposites.get(self.direction) != new_direction:
            self.direction = new_direction
            self.head.setheading(
                {"UP": 90, "DOWN": 270, "LEFT": 180, "RIGHT": 0}[new_direction]
            )

    def collided_with_self(self):
        return any(self.head.distance(seg) < 10 for seg in self.segments[1:])
