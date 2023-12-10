# Bandana Pachabhaiya Magar
# StudentID: Co916126
# Date: 4th Dec, 2023

import turtle
import random

myScreen = turtle.Screen()
myScreen.title('This is my turtle drawing area.')
myScreen.bgcolor('light green')

myTurtle = turtle.Turtle()

# Function to change turtle color to red
def change_color_yellow():
    myTurtle.color("yellow")

# Function to change turtle color to green
def change_color_red():
    myTurtle.color("red")

# Function to change turtle color to blue
def change_color_white():
    myTurtle.color("white")

# Function to increase drawing speed
def increase_speed():
    mySpeed = myTurtle.speed()
    myTurtle.speed(mySpeed + 1)

# Function to decrease drawing speed
def decrease_speed():
    mySpeed = myTurtle.speed()
    myTurtle.speed(mySpeed - 1)

# Function to change background color
def change_background_color():
    turtle.bgcolor("black")

# Set up keyboard event listeners
turtle.listen()
turtle.onkey(change_color_yellow, 'y')
turtle.onkey(change_color_red, 'r')
turtle.onkey(change_color_white, 'w')
turtle.onkey(increase_speed, 'Up')
turtle.onkey(decrease_speed, 'Down')
turtle.onkey(change_background_color, 'b')


# Draw a house
myTurtle.color("orange")
myTurtle.penup() 
myTurtle.goto(-200,200) 
myTurtle.pendown()
myTurtle.forward(300)
myTurtle.right(45)
myTurtle.forward(100)
myTurtle.right(135)
myTurtle.forward(440)
myTurtle.right(135)
myTurtle.forward(100)
myTurtle.penup()
myTurtle.goto(-200,130) 
myTurtle.pendown()
myTurtle.right(135)
myTurtle.forward(300)
myTurtle.left(90)
myTurtle.forward(300)
myTurtle.left(90)
myTurtle.forward(300)
myTurtle.penup() 
myTurtle.goto(0,-170) 
myTurtle.pendown()
myTurtle.forward(150)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(150)

#Making cloud
def draw_cloud(radius, x, y):
    myTurtle.penup()
    myTurtle.goto(x , y - radius)
    myTurtle.pendown()
    myTurtle.color("white")

    myTurtle.begin_fill()
    myTurtle.circle(radius * 1.1)
    myTurtle.end_fill()

    myTurtle.penup()
    myTurtle.goto(x - radius * 1.1, y - radius * 0.8)
    myTurtle.pendown()

    myTurtle.begin_fill()
    myTurtle.circle(radius * 0.8)
    myTurtle.end_fill()

    myTurtle.penup()
    myTurtle.goto(x + radius * 1.5, y - radius * 0.7)
    myTurtle.pendown()

    myTurtle.begin_fill()
    myTurtle.circle(radius * 1.1)
    myTurtle.end_fill()

# Set up the Turtle
turtle.speed(2)
turtle.hideturtle()

# Making random snowflake
def move_turtle(x, y):
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.pendown()

# Draw a snowflake
def draw_snowflake(size):
    for _ in range(6):
        myTurtle.forward(size)
        myTurtle.backward(size)
        myTurtle.left(60)

def draw_random_snowfall(num_snowflakes):

    for _ in range(num_snowflakes):
        x = random.randint(-400, 400)
        y = random.randint(-200, 200)
        size = random.randint(3, 10)

        move_turtle(x, y)
        draw_snowflake(size)

def display_text(message, x, y, font_size=16, align="center"):
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.pendown()
    
    myTurtle.write(message, font=("Arial", font_size, "normal"), align=align)

display_text("To change backgroundcolor to black (PLease press b)", -50, -250)
draw_cloud(50, -100, 350)  # Draw a cloud at a specific location
draw_random_snowfall(70)   # Draw a random snowflake
display_text("Bandana Pachabhaiya Magar", -50, -270)

turtle.done()