import turtle
import pandas
from state import State
from message import Message

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

message = Message()

while len(guessed_states) < 50:
    ans_state = (
        screen.textinput(
            title=f"{len(guessed_states)}/{len(all_states)} States Correct",
            prompt="What's another state's name?",
        )
        .title()
        .strip()
    )

    if ans_state == "Exit":
        # save missing states
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        df = pandas.DataFrame(missing_states)
        df.to_csv("missing_states.csv")

        break

    # check if state doesnt exist
    if ans_state not in all_states:
        message.show_msg(f"State '{ans_state}' doesn't exist.")
    elif ans_state in guessed_states:
        message.show_msg(f"You already guessed '{ans_state}'.")

    elif ans_state not in guessed_states:
        guessed_state = data[data.state == ans_state]
        state = State(
            state_name=ans_state, coords=(int(guessed_state.x), int(guessed_state.y))
        )
        guessed_states.append(ans_state)

        message.clear_msg()

        # ways to get state name only
        # print(states.loc[states.state == ans_state, "state"].values[0])
        # print(sguessed_state.state.item())


if len(guessed_states) == len(all_states):
    message.show_msg("You won! Genius!")


screen.exitonclick()
