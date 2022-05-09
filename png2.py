import turtle

win = turtle.Screen()

win.title("ARV pong 2 game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#variables
score_a = 0
score_b = 0



#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.penup()
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5 , stretch_len=1)
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.penup()
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5 , stretch_len=1)
paddle_b.goto(350,0)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.penup()
ball.shape("circle")
ball.goto(0,0)
ball.dx =0.2
ball.dy =0.2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.color("white")
pen.write( "Player A = 0 Player B = 0", align = "center", font=("Courier",12,"normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


#Main game loop

while True:
    win.update()

    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a +=1
        pen.clear()
        pen.write( "Player A = 0 Player B = 0", align = "center", font=("Courier",12,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b +=1
        pen.clear()
        pen.write( "Player A = {} Player B = {}".format(score_a,score_b), align = "center", font=("Courier",12,"normal"))
        
    #for ball and paddle collison
    if (ball.xcor() > 340 and ball.xcor() > 350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor() - 40 ):
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor() - 40 ):
        ball.setx(-340)
        ball.dx *=-1


    if score_b>=10 or score_a>=10 :
        print("The score of Player A is: ",score_a,"The score of Player B is: ",score_b)
        print("Thank You for playing with us")
        quit()
