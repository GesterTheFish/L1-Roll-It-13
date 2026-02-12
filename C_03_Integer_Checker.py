error = "please enter an integer that is greater than or equal to 13"

while True:
    try:
        game_goal = int(input("What is the game goal? \n"))

        if game_goal < 13 or game_goal < 1:
            print(error)
        else:
            print(f"Game goal: {game_goal}")
            break

    except ValueError:
        print(error)