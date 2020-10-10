import turtle
from playsound import playsound

game_window = turtle.Screen()
game_window.title("Pong Game")
game_window.bgcolor("black")
game_window.setup(width=800, height=600)
game_window.tracer(0)  # stops window from updating

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # animation speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Sound
def play_sound():
    playsound("bounce.wav", 0)


# Paddle A Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)


# Paddle A Functions
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)


# Key Binding
game_window.listen()
game_window.onkeypress(paddle_a_up, "w")
game_window.onkeypress(paddle_a_down, "s")

game_window.onkeypress(paddle_b_up, "Up")
game_window.onkeypress(paddle_b_down, "Down")

# Ball
ball = turtle.Turtle()
ball.speed(0)  # animation speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# Ball Movement
ball.dx = 0.2
ball.dy = 0.2

# Score using Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Main Game Loop
while True:
    game_window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverse direction
        play_sound()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        play_sound()

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball Collision
    if (340 < ball.xcor() < 350) and (
            paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        play_sound()

    if (-340 > ball.xcor() > -350) and (
            paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        play_sound()
