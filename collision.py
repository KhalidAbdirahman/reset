import turtle
import random


class BouncingBall(turtle.Turtle):
    def __init__(self, posx, posy, color, velx, vely, paddle):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.setpos(posx, posy)
        self.shape("circle")
        self.color(color)
        self.vx = velx
        self.vy = vely
        self.paddle = paddle

    def animate(self):
        newx = self.xcor() + self.vx
        newy = self.ycor() + self.vy
        dx = abs(self.paddle.xcor() - newx)
        dy = abs(self.paddle.ycor() - newy)
        if dx < 50 and dy < 20 and self.vy < 0:
            self.vy *= -1.1
        if newx < 0:
            newx = 0
            self.vx *= -1
        if newx > 400:
            newx = 400
            self.vx *= -1
        if newy > 400:
            newy = 400
            self.vy *= -1
        self.vy -= 0.01
        self.setpos(newx, newy)
        if newy < 0:
            self.hideturtle()
        else:
            turtle.ontimer(self.animate, 30)




turtle.delay(0)
turtle.setworldcoordinates(0, 0, 400, 400)

paddle = turtle.Turtle()
paddle.shape("square")
paddle.shapesize(1, 5)
paddle.penup()
paddle.speed(0)
paddle.setpos(200, 10)

balls = set()
for i in range(10):
    xpos = random.randint(0, 400)
    ypos = random.randint(0, 400)
    xvel = random.uniform(-2, 2)
    yvel = random.uniform(-2, 2)
    color = random.choice(("red", "green", "blue", "yellow"))
    balls.add(BouncingBall(xpos, ypos, color, xvel, yvel, paddle))
for ball in balls:
    ball.animate()


def move_paddle_left():
    paddle.setpos(paddle.xcor() - 20, paddle.ycor())


def move_paddle_right():
    paddle.setpos(paddle.xcor() + 20, paddle.ycor())


turtle.onkeypress(move_paddle_left, "Left")
turtle.onkeypress(move_paddle_right, "Right")
turtle.listen()

turtle.mainloop()