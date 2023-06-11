import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S States Games")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

write_turtle = turtle.Turtle()
write_turtle.penup()
write_turtle.ht()

data = pandas.read_csv('50_states.csv')

all_states = data.state.to_list()
print(all_states)
check = []
while len(check) != 50:
    answer_state = screen.textinput(title=f"{len(check)}/50 Guess the State", prompt="What's another state's name").title()
    correct = data[data.state == answer_state]
    x = correct.x
    y = correct.y
    list_c = correct.state.to_list()

    if answer_state == 'Exit':
        break
    elif len(list_c) == 0:
        pass
    elif list_c[0] == answer_state:
        write_turtle.goto(int(x), int(y))
        write_turtle.write(f"{answer_state}")
        check.append(list_c[0])

missing_states = [state for state in all_states if state not in check]

states_to_learn = pandas.DataFrame(missing_states)
states_to_learn.to_csv('states_to_learn.csv')
