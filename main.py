import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess The States")
image = "blank_states_img.gif"
screen.addshape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

turtle.shape(image)

answer_state = screen.textinput(title="Guess the States", prompt="What is your guess?")

print(answer_state)

if answer_state:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_date = data[data.state == answer_state]
    t.goto(0,0)


turtle.mainloop()
screen.exitonclick()