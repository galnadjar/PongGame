#Pong in Python 3
#By @TheWave Aka Gal Nadjar

import turtle
import winsound

#Setup screen
wn = turtle.Screen()
wn.title("Pong by TheWave")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

name = turtle.textinput("Enter your Name", "Name")

#Score
player1Score = 0
player2Score = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("grey")
paddle_a.shapesize(stretch_wid=6,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("grey")
paddle_b.shapesize(stretch_wid=6,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25
ball.dy = 0.25


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("{}: 0    \t Player2: 0 ".format(name),align="center",font=("Courier",22,"normal"))




# Function

def playSound():
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

def paddle_a_up():
    y = paddle_a.ycor()
    if y + 15 < 248:
        y += 15
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y - 15 > -248:
        y -= 15
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y + 15 < 248:
        y += 15
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y - 15 > -248:
        y -= 15
        paddle_b.sety(y)


while True:

    # keyboard binding
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")

    while player1Score < 3 and player2Score < 3:
        wn.update()

        #ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)


        #border

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            playSound()


        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            playSound()


        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1
            pen.clear()
            player1Score += 1
            pen.write("{}: {}    \t Player2: {} ".format(name, player1Score, player2Score), align="center",
                      font=("Courier", 22, "normal"))


        elif ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            pen.clear()
            player2Score += 1
            pen.write("{}: {}    \t Player2: {} ".format(name,player1Score, player2Score), align="center",
                      font=("Courier", 22, "normal"))


        #paddle and ball collison
        if (ball.xcor() > 330 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -70:
            ball.setx(330)
            ball.dx *= -1
            playSound()


        elif (ball.xcor() < -330 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -70:
            ball.setx(-330)
            ball.dx *= -1
            playSound()


    #End of the game
    if player1Score > player2Score:
        winner = name
    else:
        winner = "Player 2"

    pen.clear()
    pen.write("{} is WINNER WINNER CHICKEN DINNER!".format(winner),align="center",font=("Courier",22,"bold"))

    decision = turtle.textinput("Wanna keep playing?", "Enter your choice")
    if decision == "yes":
        player1Score = 0
        player2Score = 0
        pen.clear()
        pen.write("{}: 0    \t Player2: 0 ".format(name), align="center", font=("Courier", 22, "normal"))

    elif decision == "no":
        quit()
