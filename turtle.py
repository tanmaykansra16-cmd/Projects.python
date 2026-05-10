import random
from turtle import Turtle, Screen

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? enter your input :")
print(user_bet)
color = ["red", "orange", "yellow", "green", "blue", "purple"]
directions = [-70, -40, -10, 20, 50, 80]

turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-230, y=directions[turtle_index])
    turtles.append(new_turtle)


if user_bet:
    race_on = True

while race_on:


    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_colour = turtle.pencolor()
            race_on= False
            if winning_colour == user_bet:
                print(f"you won!! {winning_colour}!! won ")
            else:
                print(f"you lost!! {winning_colour}!! won ")

        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)
        
screen.exitonclick()
