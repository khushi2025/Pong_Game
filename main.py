from turtle import Turtle,Screen
from paddle import Paddle
from ball import  Ball
from scoreboard import Scoreboard
import time

#Setting the screen
screen=Screen()
screen.bgcolor("#000000")
screen.setup(width=800,height=600)
screen.title("Pong Game.")
screen.tracer(0)
screen.listen()

#Creating two objects that is left and right paddle
r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball=Ball()
score=Scoreboard()
#Adding functionality on key press
"""Used the method onkeypress because when we use up and down key in onkey method it works fine and smoothly
but when we use some other key it moves abruptly and not so smooth."""
screen.onkeypress(fun=r_paddle.up,key="Up")
screen.onkeypress(fun=r_paddle.down,key="Down")
screen.onkeypress(fun=l_paddle.up,key="w")
screen.onkeypress(fun=l_paddle.down,key="s")

is_game_on=True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detecting the collison with rop and bottom wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if (ball.distance(r_paddle)<50 and ball.xcor()>320)or(ball.distance(l_paddle)<50 and ball.xcor()<-320) :
        ball.bounce_x()
    if ball.xcor()>380:
        ball.resume()
        score.l_score_update()
        score.update()
    if ball.xcor()<-380:
        ball.resume()
        score.r_score_update()
        score.update()





screen.exitonclick()