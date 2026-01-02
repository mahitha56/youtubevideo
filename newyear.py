import turtle
import random
import math
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("New Year Fireworks!")
screen.setup(width=800, height=600)
screen.tracer(0)  # turn off automatic updates

# Text turtle
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.goto(0, 250)

# Firework particle class
class Particle:
    def __init__(self, x, y, color):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.shape("circle")
        self.t.shapesize(0.3, 0.3)
        self.t.color(color)
        self.t.penup()
        self.x = x
        self.y = y
        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-4, 4)
        self.gravity = -0.1

    def move(self):
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy
        self.t.goto(self.x, self.y)

# Firework class
class Firework:
    def __init__(self):
        self.rocket = turtle.Turtle()
        self.rocket.hideturtle()
        self.rocket.shape("triangle")
        self.rocket.color("white")
        self.rocket.penup()
        self.rocket.speed(0)
        self.rocket.goto(random.randint(-300, 300), -250)
        self.vy = random.uniform(6, 10)
        self.exploded = False
        self.particles = []

    def update(self):
        if not self.exploded:
            self.rocket.showturtle()
            self.rocket.sety(self.rocket.ycor() + self.vy)
            self.vy -= 0.15
            if self.vy <= 0:
                self.explode()
        else:
            for p in self.particles[:]:  # copy to avoid modifying list during iteration
                p.move()
                if p.y < -300:
                    p.t.hideturtle()
                    self.particles.remove(p)

    def explode(self):
        self.exploded = True
        self.rocket.hideturtle()
        colors = ["red", "yellow", "blue", "green", "orange", "purple", "white"]
        for _ in range(30):
            color = random.choice(colors)
            self.particles.append(Particle(self.rocket.xcor(), self.rocket.ycor(), color))

# Create fireworks list
fireworks = []

# Color list for text
text_colors = ["red", "yellow", "blue", "green", "orange", "purple", "white"]

# Main loop
try:
    while True:
        # Add new firework randomly
        if random.randint(0, 20) == 0:
            fireworks.append(Firework())

        # Update fireworks
        for fw in fireworks:
            fw.update()

        # Update text safely
        text_turtle.clear()
        text_turtle.color(random.choice(text_colors))
        text_turtle.write("HAPPY NEW YEAR!", align="center", font=("Arial", 30, "bold"))

        screen.update()
        time.sleep(0.03)

except turtle.Terminator:
    # This exception occurs when window is closed
    print("Fireworks show ended!")
