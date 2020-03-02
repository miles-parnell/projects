from turtle import *
from random import randint as rint

# Score var

scrA = 0
scrB = 0

# starting point for the ball

start = rint(-100, 100)

# var for making the game harder lol

hit_count = 0

more_speed = 0.2


# setting up the main frame for the game

root = Screen()
root.title('Pong')
root.bgcolor('black')
root.setup(width=800, height=600)
root.tracer(0)

# right paddle = pad_a

pad_a = Turtle()
pad_a.speed(0)
pad_a.shape('square')
pad_a.color('white')
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(350, 0)

# left paddle

pad_b = Turtle()
pad_b.speed(0)
pad_b.shape('square')
pad_b.color('white')
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(-350, 0)

# ball/square

ball = Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, start)
ball.dx = more_speed
ball.dy = more_speed

# score display/pen

pen = Turtle()
pen.speed(0)
pen.shape('square')
pen.color('orange')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {scrA}  Player B: {scrB}", align="center", font=("Courier", 24, "normal"))

# hit count

hit = Turtle()
hit.speed(0)
hit.shape('square')
hit.color('orange')
hit.penup()
hit.hideturtle()
hit.goto(0, -260)
hit.write(f"[{hit_count}] hits", align="center", font=("Courier", 20, "normal"))

 
# making ball faster

if hit_count == 2:
    more_speed += 0.1
    ball.clear()
    ball.speed(0)
    ball.shape('square')
    ball.color('white')
    ball.penup()
    ball.dx = more_speed
    ball.dy = more_speed

    

# Paddle movement functions

def padUpA():
    y = pad_a.ycor()
    y +=20
    pad_a.sety(y)

def padDwnA():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)

def padUpB():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)

def padDwnB():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)

# keyboard input

root.listen()
root.onkeypress(padUpA, "Up")
root.onkeypress(padDwnA, "Down")
root.onkeypress(padUpB, "w")
root.onkeypress(padDwnB, "s")

# running the main loop

while True:
    root.update()

    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #top and bottom border check

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # left and right border check and points (+ = r)(- = l)

    if ball.xcor() > 350:
        scrB += 1
        pen.clear()
        pen.write(f"Player A: {scrA}  Player B: {scrB}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0,start)
        ball.dx *= -1
        hit_count = 0
    elif ball.xcor() < - 350:
        scrA += 1
        pen.clear()
        pen.write(f"Player A: {scrA}  Player B: {scrB}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0,start)
        ball.dx *= -1
        hit_count = 0

    # making the paddles hit the ball

    if ball.xcor() >= 340 and ball.ycor() < pad_a.ycor() + 50 and ball.ycor() > pad_a.ycor() - 50:
        ball.dx *= -1
        hit_count += 1
        hit.clear()
        hit.write(f"[{hit_count}] hits", align="center", font=("Courier", 24, "normal"))
    elif ball.xcor() <= -340 and ball.ycor() < pad_b.ycor() + 50 and ball.ycor() > pad_b.ycor() - 50:
        ball.dx *= -1
        hit_count +=1
        hit.clear()
        hit.write(f"[{hit_count}] hits", align="center", font=("Courier", 24, "normal"))

    

