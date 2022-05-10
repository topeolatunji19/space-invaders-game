from turtle import Turtle, Screen


class Spaceship(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates

        self.penup()
        self.setpos(self.coordinates)
        self.color("white")
        self.shape("turtle")
        self.tilt(90)
        self.shapesize(stretch_len=2, stretch_wid=2)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
