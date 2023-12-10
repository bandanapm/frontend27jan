"""
Snake!
"""
# ----------------------- package --------------------
from turtle import * # importing all of the functions and utilities
from time import sleep
from random import randint
speed = 0.1
# ------------------------ Screen ---------------------------
screen = Screen()  # that creates a screen
screen.title('Snake game')
screen.setup(600, 600) #
screen.bgcolor('lightblue')
screen.tracer(0) # for animation
# -------------------------- head -----------------------
head = Turtle()
head.shape('square')
head.color('red')
head.direction = "right" # property keep track of the direction
head.penup() # we dont want to draw lines
head.speed('fastest')
# ------------------------- food --------------------
food = Turtle()
food.shape('circle')
food.color('green')
x = randint(-290, 290)
y = randint(-290, 290)
food.penup()
food.goto(x,y)
food.speed('fastest')

segments = []


def move():
    if head.direction == "right":
        x = head.xcor() # get the current x
        head.setx(x + 20)  # move 20 pixel (update the x)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)  # move 20 pixel
    elif head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

screen.listen() # this function listen to any event which may occur on screen

def up():
    if head.direction != "down":
        head.direction = "up"
def down():
    if head.direction != "up":
        head.direction = "down"
def left():
    if head.direction != "right":
        head.direction = "left"
def right():
    if head.direction != "left" :
        head.direction = "right"
def speedUp() :
    global speed
    speed /= 2
def speedDown():
    global speed
    speed *= 2
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(speedUp, "q")
screen.onkeypress(speedDown, "a")

# ---------------- Engine of the game ----------------------
while True:
    sleep(speed) #
    screen.update()
    move()
    # ------------------ food detection ------------------
    if head.distance(food) < 20:
        food.hideturtle() # hide the object
        x = randint(-290, 290)
        y = randint(-290, 290)
        food.goto(x, y)
        food.showturtle()
        seg = Turtle()
        seg.color('red')
        seg.shape('square')
        seg.speed('fastest')
        seg.penup()
        segments.append(seg)
        print(segments)

    # ---------------------- detect the wall ----------------

    if head.xcor() > 290 or head.xcor() < -290 :
        head.setx(head.xcor() * -1)

    if head.ycor() > 290 or head.ycor() < -290 :
        head.sety(head.ycor() * -1)

    # going to chain the list!
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].setx(x)
        segments[i].sety(y)

    # ------------- make sure the first seg follow the head....
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].setx(x)
        segments[0].sety(y)

    # -------------------------- GAME OVER! ---------------------
    for j in range(3,len(segments)):
        if head.distance(segments[j]) < 20:
            head.direction = 'NA'