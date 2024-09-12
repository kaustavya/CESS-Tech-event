import turtle
import random

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle for the snake's head
head = turtle.Turtle()
head.color("green")
head.shape("square")
head.speed(0)
head.penup()

# Create a list to store the snake's body parts
body = []

# Create a turtle for the food
food = turtle.Turtle()
food.color("red")
food.shape("circle")
food.speed(0)
food.penup()
food.goto(random.randint(-200, 200), random.randint(-200, 200))

# Set the initial direction
direction = "right"

# Function to move the snake
def move():
    global direction
    if direction == "right":
        head.setx(head.xcor() + 20)
    elif direction == "left":
        head.setx(head.xcor() - 20)
    elif direction == "up":
        head.sety(head.ycor() + 20)
    elif direction == "down":
        head.sety(head.ycor() - 20)

    # Check for collision with food
    if head.distance(food) < 20:
        food.goto(random.randint(-200, 200), random.randint(-200, 200))
        body_part = turtle.Turtle()
        body_part.color("green")
        body_part.shape("square")
        body_part.speed(0)
        body_part.penup()
        body.append(body_part)

    # Move the body parts
    for i in range(len(body) - 1, 0, -1):
        body[i].goto(body[i - 1].xcor(), body[i - 1].ycor())
    if len(body) > 0:
        body[0].goto(head.xcor(), head.ycor())

    # Check for collision with wall or self
    if (head.xcor() > 200 or head.xcor() < -200 or
        head.ycor() > 200 or head.ycor() < -200 or
        head in body):
        print("Game over!")
        turtle.done()

    # Repeat the movement
    screen.ontimer(move, 100)

# Function to change direction
def up():
    global direction
    if direction != "down":
        direction = "up"

def down():
    global direction
    if direction != "up":
        direction = "down"

def left():
    global direction
    if direction != "right":
        direction = "left"

def right():
    global direction
    if direction != "left":
        direction = "right"

# Set up the keyboard controls
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

# Start the game
move()

turtle.done()