import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Tic Tac Toe")
screen.setup(width=600, height=600)

# Turtle to draw the grid and marks
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(5)
pen.hideturtle()

# Draw the Tic Tac Toe grid
def draw_grid():
    # Draw vertical lines
    pen.penup()
    pen.goto(-100, 300)
    pen.pendown()
    pen.goto(-100, -300)

    pen.penup()
    pen.goto(100, 300)
    pen.pendown()
    pen.goto(100, -300)

    # Draw horizontal lines
    pen.penup()
    pen.goto(-300, 100)
    pen.pendown()
    pen.goto(300, 100)

    pen.penup()
    pen.goto(-300, -100)
    pen.pendown()
    pen.goto(300, -100)

# Draw X
def draw_x(x, y):
    pen.penup()
    pen.goto(x - 60, y + 60)
    pen.pendown()
    pen.setheading(-45)
    pen.forward(170)

    pen.penup()
    pen.goto(x + 60, y + 60)
    pen.setheading(-135)
    pen.pendown()
    pen.forward(170)

# Draw O
def draw_o(x, y):
    pen.penup()
    pen.goto(x, y - 80)
    pen.setheading(0)
    pen.pendown()
    pen.circle(80)

# Grid positions
positions = [
    [(-200, 200), (0, 200), (200, 200)],
    [(-200, 0), (0, 0), (200, 0)],
    [(-200, -200), (0, -200), (200, -200)]
]

# Game board
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

# Check for winner
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

# Mouse click handler
def handle_click(x, y):
    global current_player, game_over

    if game_over:
        return

    # Determine which square was clicked
    row, col = None, None
    if -300 < x < -100:
        col = 0
    elif -100 < x < 100:
        col = 1
    elif 100 < x < 300:
        col = 2

    if 100 < y < 300:
        row = 0
    elif -100 < y < 100:
        row = 1
    elif -300 < y < -100:
        row = 2

    if row is None or col is None or board[row][col] != "":
        return

    # Update board and draw the current player's mark
    board[row][col] = current_player
    if current_player == "X":
        draw_x(*positions[row][col])
        current_player = "O"
    else:
        draw_o(*positions[row][col])
        current_player = "X"

    # Check if there's a winner
    winner = check_winner()
    if winner:
        game_over = True
        print(f"{winner} wins!")
    elif all(board[r][c] != "" for r in range(3) for c in range(3)):
        game_over = True
        print("It's a draw!")

# Draw the grid
draw_grid()

# Listen for clicks
screen.onclick(handle_click)

# Keep the window open
turtle.mainloop()