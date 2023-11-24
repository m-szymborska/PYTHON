# import colorgram
#
# color_list = colorgram.extract('20_001.jpg', 20)
# color_palette = []
#
# for i in range(len(color_list)):
#     r = color_list[i].rgb.r
#     g = color_list[i].rgb.g
#     b = color_list[i].rgb.b
#     new_color = (r, g, b)
#     color_palette.append(new_color)
#
# print(color_palette)

import turtle
import random
from turtle import Turtle, Screen
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]

timm = Turtle()
turtle.colormode(255)
# timm.ht()
timm.penup()
timm.speed("slowest")
timm.shape("turtle")
timm.setx(-300)
timm.sety(-200)
for _ in range(10):
    for _ in range(10):
        timm.dot(20,random.choice(color_list))
        # timm.up()
        timm.forward(30)
        # timm.down()
    timm.setheading(90)
    timm.forward(30)
    timm.setheading(180)
    timm.forward(300)
    timm.setheading(0)


screen = Screen()
screen.exitonclick()