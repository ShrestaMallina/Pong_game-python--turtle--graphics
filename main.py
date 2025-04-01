import time
import turtle
from turtle import Screen


from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.go_up,key="Up")
screen.onkey(fun=r_paddle.go_down,key="Down")
screen.onkey(fun=l_paddle.go_up,key="w")
screen.onkey(fun=l_paddle.go_down,key="s")


game_is_on = True
while game_is_on:


     time.sleep(ball.move_speed)
     screen.update()
     ball.move()
     scoreboard.update_score()
     #detect collision with wall
     if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

     #detect collision with paddle
     if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

     #detect when paddle misses(r_paddle)
     if ball.xcor()>380:
          ball.reset_position()
          scoreboard.l_point()

     # detect when (l_paddle) misses
     if ball.xcor()<-380:
         ball.reset_position()
         scoreboard.r_point()







screen.exitonclick()