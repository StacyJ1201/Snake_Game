from turtle import Turtle
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle('square')
        tim.color('white')
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def move(self):
        for tim_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[tim_num - 1].xcor()
            new_y = self.segments[tim_num - 1].ycor()
            self.segments[tim_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def extend(self):
        self.add_segment(self.segments[-1].position())
