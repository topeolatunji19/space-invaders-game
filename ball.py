from turtle import Turtle


class Ball(Turtle):
    def __init__(self, coordinates):
        super(Ball, self).__init__()
        self.coordinates = coordinates
        self.setpos(self.coordinates)
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.35, stretch_len=0.35)
        self.penup()
        self.speed("slowest")
        self.x_moves = 10
        self.y_moves = 10
        # self.ball_in_play = True

        # self.move_straight()
        # self.move_straight()
    #
    # def move_ball(self):
    #     x_val = self.xcor() + self.x_moves
    #     y_val = self.ycor() + self.y_moves
    #     self.goto(x_val, y_val)

    def y_bounce(self):
        self.y_moves *= -1

    def x_bounce(self):
        self.x_moves *= -1

    # def reset(self):
    #     self.setpos(0, 0)
    #     self.y_bounce()

    def move_straight(self, x_val):
        # self.goto(0, -250)
        # while self.ball_in_play:
        # x_val = 0
        y_val = self.ycor() + self.y_moves
        self.goto(x_val, y_val)

    def new_pos(self, new_x, new_y):
        self.setpos(new_x, new_y)
        self.move_straight(new_x)
