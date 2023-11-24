from turtle import Turtle, Screen
import pandas
from turtle_state import StateTurtle
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tlo = Turtle()
tlo.shape(image)
score = 0

while score != 50:
    answer_state = screen.textinput(title=f"Guess the State. {score}/50  ",
                                    prompt="What's another state's name").title()

    play = Turtle()
    data = pandas.read_csv("50_states.csv")
    ch_data = data[data.state == answer_state]
    x = int(ch_data.x)
    y = int(ch_data.y)
    play.hideturtle()
    play.penup()
    play.goto(x, y)
    play.write(f"{answer_state}")
    score += 1



# turtle.mainloop()




screen.exitonclick()