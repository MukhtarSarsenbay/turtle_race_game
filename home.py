from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_input = screen.textinput(title="Make your bet!", prompt="Choose the color of your turtle!")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [60, 30, 0, -30, -60, -90]
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print("User won!LUCKY BASTARD")
            else:
                print(f"{winning_color} is won, you looseer!")
            is_race_on = False
        turtle.forward(random.randint(0, 10))

# timmy1 = Turtle(shape="turtle")
# timmy1.penup()
# timmy1.color("red")
# timmy1.goto(x=-230, y=30)
# timmy2 = Turtle(shape="turtle")
# timmy2.penup()
# timmy2.goto(x=-230, y=0)
# timmy2.color("orange")
# timmy3 = Turtle(shape="turtle")
# timmy3.penup()
# timmy3.goto(x=-230, y=-30)
# timmy3.color("yellow")
# timmy4 = Turtle(shape="turtle")
# timmy4.penup()
# timmy4.color("green")
# timmy4.goto(x=-230, y=-60)
# timmy5 = Turtle(shape="turtle")
# timmy5.penup()
# timmy5.color("blue")
# timmy5.goto(x=-230, y=-90)


screen.exitonclick()
