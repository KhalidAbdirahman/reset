import turtle

class BouncingBall(turtle.Turtle):
    def __init__(self, posx, posy, color, velx, vely):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.setpos(posx, posy)
        self.shape('circle')
        self.color(color)
        self.vx = velx
        self.vy = vely
    def animate(self):
        newx = self.xcor() + self.vx
        newy = self.ycor() + self.vy
        turtle.ontimer(self.animate, 30)


turtle.delay(0)
turtle.setworldcoordinates(0,0,400,400)
b1 = BouncingBall(25,125, 'green',1,2)
b2 = BouncingBall(200,200,'blue', -2,1)
b1.animate()
b2.animate()
turtle.mainloop()