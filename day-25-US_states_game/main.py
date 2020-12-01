from turtle import Screen, Turtle
import pandas


def main():
    screen = Screen()
    screen.bgpic("blank_states_img.gif")
    screen.setup(width=725, height=491)
    screen.title("Guess the state game")
    screen.onkey(screen.bye, "Escape")
    screen.listen()
    states = pandas.read_csv("50_states.csv")

    states_guessed = []
    while len(states_guessed) < len(states):
        answer = screen.textinput(title=f"{len(states_guessed)}/50 Guessed states", prompt="Guess the name of the "
                                                                                           "states")
        if answer.lower() == "exit":
            new_csv = []
            for state in states.state:
                if state not in states_guessed:
                    state_data = states[states.state == state]
                    x = int(state_data.x)
                    y = int(state_data.y)
                    new_csv.append([state])

            df = pandas.DataFrame(new_csv, columns=['state'])
            df.to_csv("Missed_states.csv")

            screen.bye()
        elif answer is not None:
            answer = answer.title()

        if answer in states.state.to_list():
            states_guessed.append(answer)
            state_data = states[states.state == answer]
            x = int(state_data.x)
            y = int(state_data.y)
            position = (x, y)

            t = Turtle()
            t.hideturtle()
            t.penup()
            t.setpos(position)
            t.write(answer)


if __name__ == '__main__':
    main()
