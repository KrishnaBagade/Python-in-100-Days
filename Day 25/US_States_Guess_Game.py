import turtle
import pandas

def show_state(state_to_show,x_state,y_state):
    location_reveal = turtle.Turtle()
    location_reveal.penup()
    location_reveal.hideturtle()
    location_reveal.goto(x=x_state,y=y_state)
    location_reveal.write(arg=f"{state_to_show}")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
count = 0
states = pandas.read_csv("50_states.csv")
state_name = states["state"]
states_guessed = []
while count != 50:
  for state in range(len(states)-1):
    if answer_state == state_name.values[state].title():
        count += 1
        x_cor = states["x"][state]
        y_cor = states["y"][state]
        show_state(state_to_show=answer_state,x_state=x_cor,y_state=y_cor)
        states_guessed.append(answer_state)
  if answer_state == "Exit":
    break
  guess_state = screen.textinput(title=f"{count}/50 States Correct", prompt="What's another state's name? ").lower()
  answer_state = guess_state
screen.mainloop()
states_to_learn = list(set(state_name)-set(states_guessed))
to_be_learnt = pandas.DataFrame(data=states_to_learn)
to_be_learnt.to_csv("States_to_Learn.csv")