import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess The States")
image = "blank_states_img.gif"
screen.addshape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

turtle.shape(image)


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What is your guess?").title()
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_date = data[data.state == answer_state]
        t.goto(state_date.x.item(), state_date.y.item())
        t.write(answer_state)


turtle.mainloop()
screen.exitonclick()