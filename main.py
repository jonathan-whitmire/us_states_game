import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_guesses = 0
guessed_states = []

while correct_guesses < 50:

    answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct",
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        guessed_states_missed = pandas.DataFrame(missing_states)
        guessed_states_missed.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        correct_guesses += 1

screen.exitonclick()
