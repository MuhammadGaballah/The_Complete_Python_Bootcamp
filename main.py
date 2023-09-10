import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

print(all_states)

states_answered = []
states_guessed = 0

game_over = False

while not game_over:
    answer_state = screen.textinput(title=f"Guess the State {states_guessed}/50",
                                    prompt="What's another state's name?").title()
    answer_state_x_cor = data[data["state"] == answer_state].x

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in states_answered:
                missing_states.append(state)
        df = pd.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        game_over = True

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        state_x_cor = data[data["state"] == answer_state].x.iloc[0]
        state_y_cor = data[data["state"] == answer_state].y.iloc[0]
        t.penup()
        t.goto(int(state_x_cor), int(state_y_cor))
        t.write(answer_state)

        if answer_state not in states_answered:
            states_guessed += 1
            states_answered.append(answer_state)

    if len(states_answered) == 50:
        game_over = True
        t.write("You guessed all 50 states!")

