from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.snake_size = len(STARTING_POSITIONS)
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        turtle = Turtle('square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(position)
        # turtle.goto(turtlex, 0)
        self.segments.append(turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def update_snake(self):
        self.snake_size += 1

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_y = self.segments[seg_num - 1].ycor()
            new_x = self.segments[seg_num - 1].xcor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)