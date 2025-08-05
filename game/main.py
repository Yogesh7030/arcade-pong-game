import time
from turtle import Screen
from arcade_participants import Arcade
from scoreboard import Scoreboard
from ball import Ball

Controller1_key_up = "Up"
Controller1_key_down = "Down"
Controller2_key_up = "w"
Controller2_key_down = "s"
Number_of_points = 10

STARTING_POSITIONS_PARTICIPANT1 = (350, 0)
STARTING_POSITIONS_PARTICIPANT2 = (-350,0)

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title("Arcade Game")
game_is_on = True
my_screen.tracer(0)

scoreboard = Scoreboard()
arcade = Arcade(STARTING_POSITIONS_PARTICIPANT1)
arcade2 = Arcade(STARTING_POSITIONS_PARTICIPANT2)
ball = Ball()



my_screen.listen()
my_screen.onkey(arcade.up, Controller1_key_up)
my_screen.onkey(arcade.down, Controller1_key_down)

my_screen.onkey(arcade2.up, Controller2_key_up)
my_screen.onkey(arcade2.down, Controller2_key_down)

while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(arcade) < 60 and ball.xcor() > 320 or ball.distance(arcade2) < 60 and ball.xcor() < -320:
        ball.bounce_back()

    if ball.xcor() > 370:
        scoreboard.l_score += 1
        scoreboard.display_score()
        ball.reset()

    if ball.xcor() < -370:
        scoreboard.r_score += 1
        scoreboard.display_score()
        ball.reset()

    if scoreboard.l_score == Number_of_points or scoreboard.r_score == Number_of_points:
        game_is_on = False

my_screen.exitonclick()