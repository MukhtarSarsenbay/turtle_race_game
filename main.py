from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def left_side():
    tim.left(10)

def right_side():
    tim.right(10)

def clear_everything():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


tim.speed("fastest")
screen.listen()
screen.onkey(key="w", fun=move_forward)  # function on key # higher order function, here keyword arguments
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=left_side)
screen.onkey(key="d", fun=right_side)
screen.onkey(key="c", fun=clear_everything)
screen.exitonclick()

