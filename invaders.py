import time
import turtle
from turtle import Turtle
import random
COLOR_LIST = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72)]


class Invaders(Turtle):
    def __init__(self):
        super().__init__()
        self.x_axis = -220
        self.y_axis = 370
        self.x_moves = 10
        self.y_moves = 10
        self.invaders_list = []
        self.ammo_list = []
        self.speed("slowest")

    def create_invaders(self):
        # invaders_list = []
        for invader in range(18):
            invader = Turtle(shape="turtle")
            invader.speed("slowest")
            invader.tilt(270)
            turtle.colormode(255)
            invader.color(random.choice(COLOR_LIST))
            invader.penup()
            invader.pen(outline=3)
            invader.shapesize(stretch_len=0.8, stretch_wid=0.8, outline=1)
            invader.setpos(x=self.x_axis, y=self.y_axis)
            self.invaders_list.append(invader)
            if len(self.invaders_list) % 6 == 0:
                self.y_axis -= 30
                self.x_axis = -220
            else:
                self.x_axis += 30
        return self.invaders_list

    def move_invaders(self):
        for invaders in self.invaders_list:
            x_val = invaders.xcor() + self.x_moves
            # y_val = self.ycor() + self.y_moves
            invaders.goto(x_val, invaders.ycor())

    def bounce_invaders(self):
        self.x_moves *= -1
        for invaders in self.invaders_list:
            y_val = invaders.ycor() - 10
            invaders.goto(invaders.xcor(), y_val)

    def create_ammo(self):
        ammo = Turtle()
        ammo.shape("circle")
        turtle.colormode(255)
        ammo.color(random.choice(COLOR_LIST))
        ammo.shapesize(stretch_wid=0.35, stretch_len=0.35)
        ammo.penup()
        ammo.speed("slowest")
        invader_positions = [(invader.xcor(), invader.ycor()) for invader in self.invaders_list]
        new_coordinates = random.choice(invader_positions)
        # print(new_coordinates)
        ammo.setpos(new_coordinates)
        self.ammo_list.append(ammo)
        return self.ammo_list

    def move_ammo(self, ammo):
        y_val = ammo.ycor() - self.y_moves
        ammo.goto(ammo.xcor(), y_val)


# import turtle
# from turtle import Turtle
# import random
# COLOR_LIST = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72)]
#
#
# class Invaders(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.x_axis = -220
#         self.y_axis = 280
#         self.x_moves = 10
#         self.y_moves = 10
#         # self.invaders_list = []
#
#     def create_invaders(self):
#         invaders_list = []
#         for wall in range(18):
#             wall = Turtle(shape="turtle")
#             wall.speed("slowest")
#             wall.tilt(270)
#             turtle.colormode(255)
#             wall.color(random.choice(COLOR_LIST))
#             wall.penup()
#             wall.pen(outline=3)
#             wall.shapesize(stretch_len=1, stretch_wid=1, outline=1)
#             wall.setpos(x=self.x_axis, y=self.y_axis)
#             invaders_list.append(wall)
#             if len(invaders_list) % 6 == 0:
#                 self.y_axis -= 30
#                 self.x_axis = -220
#             else:
#                 self.x_axis += 30
#         return invaders_list
#
#     def move_invaders(self, invaders_list):
#         for invaders in invaders_list:
#             x_val = invaders.xcor() + self.x_moves
#             # y_val = self.ycor() + self.y_moves
#             self.goto(x_val, invaders.ycor())
