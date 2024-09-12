import turtle
import random

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create four turtles for the race
turtle1 = turtle.Turtle()
turtle1.color("red")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-200, 100)

turtle2 = turtle.Turtle()
turtle2.color("blue")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-200, 50)

turtle3 = turtle.Turtle()
turtle3.color("green")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-200, 0)

turtle4 = turtle.Turtle()
turtle4.color("yellow")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-200, -50)

while True:


    # Function to move the turtles
    def move_turtles():
        turtle1.forward(random.randint(1, 10))
        turtle2.forward(random.randint(1, 10))
        turtle3.forward(random.randint(1, 10))
        turtle4.forward(random.randint(1, 10))

        # Check if any turtle has reached the finish line
        if turtle1.xcor() >= 200:
            print("Red turtle wins!")
            screen.ontimer(None)
            turtle.done()
        elif turtle2.xcor() >= 200:
            print("Blue turtle wins!")
            screen.ontimer(None)
            turtle.done()
        elif turtle3.xcor() >= 200:
            print("Green turtle wins!")
            screen.ontimer(None)
            turtle.done()
        elif turtle4.xcor() >= 200:
            print("Yellow turtle wins!")
            screen.ontimer(None)
            turtle.done()
        else:
            screen.ontimer(move_turtles, 100)

    # Start the race
    move_turtles()

turtle.done()