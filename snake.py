from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.new_tail(position)

    def move(self):
        for parts in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[parts - 1].xcor()
            new_y = self.snakes[parts - 1].ycor()
            self.snakes[parts].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def new_tail(self, position):
        new = Turtle("square")
        new.penup()
        new.color("white")
        new.goto(position)
        self.snakes.append(new)

    def extend(self):
        self.new_tail(self.snakes[-1].position())

