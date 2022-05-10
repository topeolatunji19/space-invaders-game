from turtle import Turtle, Screen
from spaceship import Spaceship
from ball import Ball
from wall import Wall
from scoreboard import ScoreBoard
from invaders import Invaders
import time


# To restart the shooting ball
def restart_ball():
    global x_value
    x_value = spaceship.xcor()
    ball.new_pos(spaceship.xcor(), spaceship.ycor())


my_screen = Screen()
my_screen.setup(width=490, height=800)
my_screen.title("Space Invaders")
my_screen.bgcolor("black")
my_screen.tracer(0)

spaceship = Spaceship((0, -300))
ball = Ball((spaceship.xcor(), spaceship.ycor()))

my_wall = Wall()
wall_list = my_wall.create_wall()
scores = ScoreBoard()

invaders = Invaders()
invaders_list = invaders.create_invaders()
ammo_list = invaders.create_ammo()

my_screen.listen()

# Move paddle
my_screen.onkey(spaceship.go_left, "Left")
my_screen.onkey(spaceship.go_right, "Right")

game_time = 0.1
game_is_on = True

lives = 3
x_value = spaceship.xcor()
while game_is_on:
    time.sleep(game_time)
    my_screen.update()
    ball.move_straight(x_value)
    invaders.move_invaders()

    # Create ammunition for invaders
    invaders.create_ammo()

    if len(ammo_list) == 0:
        pass
    else:
        # Move ammunition
        for ammo in ammo_list:
            invaders.move_ammo(ammo)

    # Moving ball to initial position
    if ball.ycor() > 370:
        pad_x = spaceship.xcor()
        pad_y = spaceship.ycor()
        my_screen.onkey(restart_ball, "Return")

    else:
        my_screen.onkey(None, "Return")

    # Detect wall collision
    range_list = [True for invader in invaders_list if invader.xcor() > 220 or invader.xcor() < -220]
    if any(range_list):
        invaders.bounce_invaders()

    # Detect Brick Collison
    for wall in wall_list:
        if ball.distance(wall) < 20:
            # ball.reset()
            ball.sety(400)
            wall.reset()
            wall.setx(1000)
            wall_list.remove(wall)
            game_time /= 1.15
            # if len(wall_list) == 0:
            #     scores.you_win()
            #     game_is_on = False

    for wall in wall_list:
        for ammunition in ammo_list:
            if ammunition.distance(wall) < 20:
                ammunition.setx(1000)
                wall.reset()
                wall.setx(1000)
                wall_list.remove(wall)

    # Collision with invaders
    for invader in invaders_list:
        if ball.distance(invader) < 20:
            # ball.reset()
            ball.sety(400)
            invader.reset()
            invader.setx(1000)
            scores.point()
            invaders_list.remove(invader)

    # Collision with ammo
    for ammo in ammo_list:
        if ball.distance(ammo) < 20:
            # ball.reset()
            ball.sety(400)
            ammo.setx(1000)
            scores.point()
            ammo_list.remove(ammo)

    # Collision with spaceship
    for ammunition in ammo_list:
        if spaceship.distance(ammunition) < 20:
            # If you're out of your 3 lives
            if lives < 0:
                scores.show_final_score()
                game_is_on = False
            # If you still have lives
            else:
                ball.sety(400)
                game_time = 0.1
                lives -= 1
                for ammo in ammo_list:
                    ammo.setx(1000)
                ammo_list.clear()
                invaders.create_ammo()

    # Killed all invaders
    if len(invaders_list) == 0:
        scores.you_win()
        game_is_on = False



my_screen.exitonclick()
