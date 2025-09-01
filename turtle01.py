import turtle
import random

screen = turtle.Screen()
screen.title("لعبة السلحفاة تجمع النقاط 🐢🎯")
screen.bgcolor("red")
screen.setup(width=800, height=600)
screen.tracer(0)  

player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.speed(10)
player.pendown() 

target = turtle.Turtle()
target.shape("turtle")
target.color("green")
target.penup()
target.speed(0)
target.goto(random.randint(-300, 300), random.randint(-250, 250))

score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.color("white")
pen.write(f"النقاط: {score}", align="center", font=("Arial", 16, "bold"))

move_distance = 30

def update_score():
    pen.clear()
    pen.write(f"النقاط: {score}", align="center", font=("Arial", 16, "bold"))

def move_up():
    y = player.ycor()
    player.sety(y + move_distance)

def move_down():
    y = player.ycor()
    player.sety(y - move_distance)

def move_left():
    x = player.xcor()
    player.setx(x - move_distance)

def move_right():
    x = player.xcor()
    player.setx(x + move_distance)

def check_collision():
    global score
    if player.distance(target) < 30:
        target.goto(random.randint(-300, 300), random.randint(-250, 250))
        score += 1
        update_score()

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

while True:
    screen.update()
    check_collision()