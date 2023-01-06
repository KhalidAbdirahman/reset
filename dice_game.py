

import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Tetris")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Create a board
board = turtle.Turtle()
board.speed(0)
board.shape("square")
board.color("white")
board.penup()
board.goto(0,0)
board.shapesize(stretch_wid=10, stretch_len=20)
 
# Create a piece
piece = turtle.Turtle()
piece.speed(0)
piece.shape("square")
piece.color("red")
piece.penup()
piece.goto(0,0)
piece.shapesize(stretch_wid=2, stretch_len=2)

# Create functions
def move_left():
    x = piece.xcor()
    x -= 20
    piece.setx(x)

def move_right():
    x = piece.xcor()
    x += 20
    piece

