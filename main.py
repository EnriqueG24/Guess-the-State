import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.ht()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


def Difference(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

states_to_learn = Difference(all_states, guessed_states)
new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")