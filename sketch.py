from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()
def move_fd():
    tim.fd(10)

def move_left():
  tim.lt(10)

def move_right():
    tim.rt(10)

def move_back():
    tim.back(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key = "w" , fun = move_fd)
screen.onkey(key = "a" , fun = move_left)
screen.onkey(key = "s" , fun = move_back)
screen.onkey(key = "d" , fun = move_right)
screen.onkey(key = "c" , fun = clear)


screen.exitonclick()