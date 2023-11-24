import turtle
import random
from turtle import Turtle, Screen
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

timm = Turtle()
timm.shape("turtle")
timm.color("PaleGreen4")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
timm.pensize(1)
timm.speed("fastest")

for _ in range(50):
    timm.color(random_color())
    timm.circle(50)
    timm.left(10)
    timm.circle(50)

# for _ in range(200):
#     timm.color(random_color())
#     timm.forward(30)
#     timm.setheading(random.choice(directions))

# for _ in range(3):
#     timm.forward(100)
#     timm.right(120)
# for _ in range(4):
#     timm.color("Red")
#     timm.forward(100)
#     timm.right(90)
# for _ in range(5):
#     timm.color("Blue")
#     timm.forward(100)
#     timm.right(72)
# for _ in range(6):
#     timm.color("Orange")
#     timm.forward(100)
#     timm.right(60)
# for _ in range(7):
#     timm.color("Black")
#     timm.forward(100)
#     timm.right(51.4)
# for _ in range(8):
#     timm.color("Pink")
#     timm.forward(100)
#     timm.right(45)
# for _ in range(9):
#     timm.color("Green")
#     timm.forward(100)
#     timm.right(40)








# #rysuje przerywaną linię
# for _ in range(15):
#     timm.forward(10)
#     timm.pendown()
#     timm.forward(10)
#     timm.penup()

# #rysuje kwadrat
# for _ in range(4):
#     timm.forward(100)
#     timm.left(90)


screen = Screen()
screen.exitonclick()
