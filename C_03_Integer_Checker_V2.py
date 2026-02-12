def int_check():
    """Checks if user enters int>=13"""

    error = "please enter an integer that is greater than or equal to 13"

    while True:
        try:
            response = int(input("What is your game goal? \n"))

            if response < 13:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

# Main routine starts here
game_goal = int_check()
print(game_goal)