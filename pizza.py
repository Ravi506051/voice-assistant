import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
samosa = turtle.Turtle()
samosa.pensize(3)
samosa.speed(3)

def draw_samosa():
    samosa.penup()
    samosa.goto(-100, -50)
    samosa.pendown()
    samosa.fillcolor("goldenrod")
    samosa.begin_fill()
    
    # Draw Triangle (Samosa Shape)
    for _ in range(3):
        samosa.forward(200)
        samosa.left(120)
    
    samosa.end_fill()
    
def animate_samosa():
    for i in range(5):
        samosa.penup()
        samosa.goto(-100, -50 + (i * 10))  # Move up
        samosa.pendown()
        time.sleep(0.2)
        screen.update()

# Draw and animate the samosa
draw_samosa()
animate_samosa()

# Hold the screen
turtle.done()
