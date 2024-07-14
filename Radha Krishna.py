import turtle
import time

# Keeping the background color dark blue
turtle.bgcolor('#000033')

# Defining the title of the program
turtle.title("Radhe Krishna")

# Creating turtle screen
screen = turtle.Screen()
# Defining height and width of the screen
screen.setup(650, 580)

# Creating turtle for drawing Radha Krishna
t1 = turtle.Turtle()

# Setting the turtle speed
t1.speed(4)

# Moving the turtle down and left to the start position
t1.right(90)
t1.pu()
t1.forward(180)
t1.left(90)

# Drawing the base
t1.pd()
t1.fillcolor("#ff99d1")  # Light pink color
t1.begin_fill()
t1.forward(400)
t1.right(90)
t1.forward(100)
t1.right(90)
t1.forward(800)
t1.right(90)
t1.forward(100)
t1.right(90)
t1.forward(400)
t1.end_fill()

# Drawing the moon
t1.fillcolor("#CDEEF1")  # Light blue color
t1.begin_fill()
t1.forward(160)
t1.left(40)
t1.circle(250, 280)
t1.left(40)
t1.forward(160)
t1.end_fill()

# Drawing Radha
t1.fillcolor("#012427")  # Dark teal color
t1.begin_fill()
t1.forward(160)
t1.left(130)
t1.circle(-300, 30)
t1.forward(95)
t1.circle(50, 40)
t1.right(40)
t1.forward(43)
t1.circle(80, 25)
t1.circle(50, 30)
t1.left(10)
t1.circle(35, 28)
# Radha done

# Drawing Krishna's turban
t1.right(160)
t1.circle(10, 100)
t1.right(100)
t1.circle(10, 80)
t1.forward(20)
t1.left(80)
t1.circle(100, 15)
t1.right(90)
t1.forward(6)
t1.left(65)
t1.circle(60, 55)

# Drawing Krishna's morpankh
t1.right(160)
t1.circle(20, 100)
t1.forward(10)
t1.circle(-20, 25)
t1.left(170)
t1.circle(-20, 40)
t1.forward(10)
t1.circle(20, 80)
# Morpankh done

# Drawing rest part of Krishna's turban
t1.right(135)
t1.circle(60, 15)
t1.left(70)
t1.forward(6)
t1.right(110)
t1.forward(9)
t1.left(80)
t1.circle(70, 24)
t1.right(60)
t1.circle(65, 30)
t1.circle(-5, 110)

# Drawing right hand of Krishna
t1.circle(5, 120)
t1.right(90)
t1.circle(5, 60)
t1.forward(10)
t1.circle(10, 5)
t1.right(80)
t1.forward(15)
t1.circle(-5, 160)
# Drawing the first open finger of right hand
t1.forward(6)
t1.circle(2, 180)
t1.forward(6)
t1.circle(20, 30)

# Drawing fingers holding bansuri
t1.right(140)
t1.circle(3, 150)
t1.right(110)
t1.circle(4, 80)
t1.forward(2)
t1.right(100)

# Drawing second open finger of Krishna
t1.forward(6)
t1.right(60)
t1.forward(9)
t1.circle(2, 180)
t1.forward(10)
t1.left(30)
t1.forward(15)

# Drawing bansuri
t1.right(85)
t1.forward(40)
t1.right(60)
t1.circle(5, 310)
t1.right(80)
t1.forward(3)
t1.right(90)
# Drawing dor on bansuri
t1.forward(42)
t1.right(30)
t1.forward(10)
t1.left(90)
t1.circle(20, 60)
t1.left(95)
t1.forward(12)
t1.right(29)
t1.forward(42)

# Drawing the rest part of bansuri
t1.right(90)
t1.forward(34)
t1.right(85)

# Drawing left hand of Krishna
t1.forward(2)
t1.circle(60, 25)

# Drawing Krishna's duppata
t1.right(80)
t1.circle(10, 40)
t1.forward(45)
t1.left(10)
t1.forward(130)
# Drawing the plates of duppata
t1.left(90)
t1.forward(20)
t1.right(90)
t1.forward(10)
t1.left(90)
t1.forward(10)
t1.right(90)
t1.forward(5)
t1.left(90)
t1.forward(25)
# Completing drawing duppata
t1.left(100)
t1.forward(120)
t1.right(175)
t1.circle(50, 50)

# Drawing Krishna's dhoti
t1.right(80)
t1.circle(110, 15)
t1.forward(75)

# Completing the drawing at the base
t1.left(97)
t1.forward(260)
t1.end_fill()

# Moving to position to write text
t1.pu()
t1.right(90)
t1.forward(100)
t1.right(90)
t1.forward(420)

# Creating a separate turtle for the text animation
t2 = turtle.Turtle()
t2.pu()
t2.goto(-200, -250)

# Function to animate the text
def animate_text(turtle, text, font, colors, iterations):
    for _ in range(iterations):
        for color in colors:
            turtle.clear()
            turtle.color(color)
            turtle.write(text, font=font)
            time.sleep(0.5)

# Animating the text
t2.color("#FFD700")  # Starting with gold color
animate_text(t2, "Radhe Krishna....", ("Segoe Script", 45, "bold"), ["#FFD700", "#FF69B4", "#00FFFF", "#FF4500"], 20)

t1.hideturtle()
t2.hideturtle()

turtle.done()
