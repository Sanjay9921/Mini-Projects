import turtle
from turtle import Turtle, Screen
import pandas as pd

csv_file = "50_states.csv"

image = "blank_states_img.gif"

screen = Screen()
screen.title("U.S States Game")

screen.addshape(image)
turtle.shape(image)

data = pd.read_csv(csv_file)
all_states = data["state"].to_list()
# all_states = [state.capitalize() for state in all_states]

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    ).title()

    answer_state = answer_state.capitalize()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guesses_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)

        state_data = data[data["state"] == answer_state]
        x_cor = int(state_data["x"])
        y_cor = int(state_data["y"])
        state_name = state_data["state"].item()  # first item of df

        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_cor, y_cor)
        t.write(state_name)

print(answer_state)