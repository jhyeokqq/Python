# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpeg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(182, 158, 24), (37, 34, 58), (228, 224, 62), (26, 49, 30), (200, 48, 15), (197, 135, 163), (75, 178, 226), (249, 242, 245), (18, 13, 11), (234, 223, 15), (214, 158, 76), (163, 16, 9), (83, 96, 109), (52, 43, 89), (31, 18, 21), (84, 99, 89), (157, 11, 15), (151, 164, 156), (185, 97, 88), (232, 171, 166), (135, 72, 76), (39, 75, 44), (214, 176, 187), (186, 103, 106), (150, 206, 228), (184, 188, 211), (119, 125, 147)]

import turtle as turtle_module
import random


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101


for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()