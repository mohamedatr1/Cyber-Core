import turtle , pandas

window = turtle.Screen()
window.bgpic("map game/map.gif")
window.setup(488,250)
window.title("ATR Map Game")



# ___________



# def my_function(x,y):
#     print(x,y)    


# turtle.onscreenclick(my_function)
# turtle.mainloop()
# ___________


data = pandas.read_csv("map game/coordinates.csv")
countries = data.country.to_list()
guessed = []
missing_countries = []

while len(guessed) < 17:
    answer = window.textinput(title = f"{len(guessed)}/18 guessed", prompt="Type a country name and hit Enter!").title()
    if answer in countries:
        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_x = data[data.country == answer]["x"].item()
        country_y = data[data.country == answer]["y"].item()
        t.goto(country_x, country_y)
        t.fillcolor("red")
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.write(answer, font=("arial",8))

    elif answer == "Exit":
        for country in countries:
            if country not in guessed:
                missing_countries.append(country)
        final_csv = pandas.DataFrame(missing_countries).to_csv("map game/wronganswers.csv",encoding="utf-8")

        break


    
       








