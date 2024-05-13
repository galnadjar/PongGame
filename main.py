#Pong in Python 3
#By @TheWave Aka Gal Nadjar

import turtle
import winsound

TURNS_TO_WIN = 5
PADDLE_MOVE_DELTA = 15

PADDLE_EDGE_LIMIT = 248
PADDLE_X_COOR = 330
Y_AXE_BORDER = 290
X_AXE_BORDER = 370
CENTER_SCREEN_Y_COOR = 250
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

#Setup screen
wn = turtle.Screen()
wn.title("Pong by TheWave")
wn.bgcolor("black")
wn.setup(width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
wn.tracer(0)

name = turtle.textinput("Enter your Name", "Name")

name = name if name != "" else "Player1"

#Score
player1Score = 0
player2Score = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("grey")
paddle_a.shapesize(stretch_wid=6,stretch_len=2)
paddle_a.penup()
paddle_a.goto(-X_AXE_BORDER-10,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("grey")
paddle_b.shapesize(stretch_wid=6,stretch_len=2)
paddle_b.penup()
paddle_b.goto(X_AXE_BORDER,0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,CENTER_SCREEN_Y_COOR)
pen.write("{}: 0    \t Player2: 0 ".format(name),align="center",font=("Courier",22,"normal"))


# Functions
def playSound():
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

def paddle_a_up():
    y = paddle_a.ycor()
    if y + PADDLE_MOVE_DELTA < PADDLE_EDGE_LIMIT:
        y += PADDLE_MOVE_DELTA
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y - PADDLE_MOVE_DELTA > -PADDLE_EDGE_LIMIT:
        y -= PADDLE_MOVE_DELTA
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y + PADDLE_MOVE_DELTA < PADDLE_EDGE_LIMIT:
        y += PADDLE_MOVE_DELTA
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y - PADDLE_MOVE_DELTA > -PADDLE_EDGE_LIMIT:
        y -= PADDLE_MOVE_DELTA
        paddle_b.sety(y)


while True:

    # keyboard binding
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")

    while player1Score < TURNS_TO_WIN and player2Score < TURNS_TO_WIN:
        wn.update()

        #ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #border
        if ball.ycor() > Y_AXE_BORDER:
            ball.sety(Y_AXE_BORDER)
            ball.dy *= -1
            playSound()


        elif ball.ycor() < -Y_AXE_BORDER:
            ball.sety(-Y_AXE_BORDER)
            ball.dy *= -1
            playSound()


        if ball.xcor() > X_AXE_BORDER:
            ball.goto(0,0)
            ball.dx *= -1
            pen.clear()
            player1Score += 1
            pen.write("{}: {}    \t Player2: {} ".format(name, player1Score, player2Score), align="center",
                      font=("Courier", 22, "normal"))


        elif ball.xcor() < -X_AXE_BORDER:
            ball.goto(0,0)
            ball.dx *= -1
            pen.clear()
            player2Score += 1
            pen.write("{}: {}    \t Player2: {} ".format(name,player1Score, player2Score), align="center",
                      font=("Courier", 22, "normal"))


        #paddle and ball collison
        if (ball.xcor() > PADDLE_X_COOR and ball.xcor() < X_AXE_BORDER) and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -70:
            ball.setx(PADDLE_X_COOR)
            ball.dx *= -1
            playSound()


        elif (ball.xcor() < -PADDLE_X_COOR and ball.xcor() > -X_AXE_BORDER) and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -70:
            ball.setx(-PADDLE_X_COOR)
            ball.dx *= -1
            playSound()


    #End of the game
    if player1Score > player2Score:
        winner = name
    else:
        winner = "Player 2"

    pen.clear()

    turtle.TK.messagebox.showinfo(title="GAME OVER", message=f"{winner} is WINNER WINNER CHICKEN DINNER!")
    exit()