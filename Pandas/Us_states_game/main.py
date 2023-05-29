import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.bgpic('blank_states_img.gif')


data = pandas.read_csv('50_states.csv')
states = data.state.to_list()
correct_states = []
game_on = True
timmy = Turtle()
timmy.penup()
timmy.ht()

while game_on:
    print(correct_states)
    answer = screen.textinput(title= f'{len(correct_states)}/50 Guess the State', prompt= "What's another State name?: ").title()
    if answer in states:
        if answer not in correct_states:
            correct_state = data[data["state"] == answer]
            x_cor = int(correct_state['x'])
            y_cor = int(correct_state['y'])
            
            timmy.goto(x_cor, y_cor)
            timmy.write(answer)
            correct_states.append(answer)
    elif answer == "Exit":
        break
    


learn_states = [state for state in states if state not in correct_states]

learn_df = pandas.DataFrame(learn_states)
learn_df.to_csv('States_to_learn')