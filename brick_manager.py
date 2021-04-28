from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# COLORS = ["red", "orange"]
BRICK_X = -360
BRICK_Y = 300


class BrickManager:
    def __init__(self):
        self.all_bricks = []
        self.starting_x_pos = BRICK_X
        self.starting_y_pos = BRICK_Y
        self.draw_bricks()

    def draw_bricks(self):
        for color in COLORS:
            self.create_brick_row(color)

    def create_brick_row(self, row_color):
        for num in range(12):
            new_brick = Turtle("square")
            new_brick.shapesize(stretch_wid=1, stretch_len=3)
            new_brick.penup()
            new_brick.color(row_color)
            new_brick.goto(self.starting_x_pos, self.starting_y_pos)
            self.starting_x_pos += 65
            self.all_bricks.append(new_brick)
        self.starting_y_pos -= 25
        self.starting_x_pos = BRICK_X

    def refresh_bricks(self):
        self.starting_x_pos = BRICK_X
        self.starting_y_pos = BRICK_Y
        self.draw_bricks()
