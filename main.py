import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Bangladesh Districts!")

image = "bd_map.gif"

screen.addshape(image)

turtle.shape(image)


df = pd.read_csv("64districts.csv")
all_districts = df["district"].tolist()
guessed_corr = []


while len(guessed_corr) < 64:

    answer_district = screen.textinput(
        title=f"{len(guessed_corr)}/64 districts guessed correctly",
        prompt="What's another district's name?",
    ).title()

    if answer_district == "Exit":  # secret code to exit the game
        districts_to_learn = list(set(all_districts) - set(guessed_corr))
        new_data = pd.DataFrame(districts_to_learn)
        new_data.to_csv("districts_to_learn.csv")
        #creates a new csv file with the names of all the districts needed to learn

        break

    if answer_district in all_districts:  # correctly guessed the district

        guessed_corr.append(answer_district)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df["district"] == answer_district]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data["district"].item())


screen.exitonclick()
