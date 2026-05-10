color_list = [(236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95),
              (220, 171, 45),
              (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91),
              (243, 218, 56),
              (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), (239, 162, 193), (145, 27, 25),
              (243, 167, 156),
              (163, 211, 178), (26, 187, 225), (6, 116, 54), (138, 210, 232), (74, 135, 184), (170, 191, 221),
              (114, 10, 8)]

import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.setheading(225)

tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots = 101
tim.speed("fastest")
for dot_count in range(1, number_of_dots):

    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.fd(50)
    if dot_count % 10 == 0:
        tim.lt(90)
        tim.fd(50)
        tim.lt(90)
        tim.fd(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
