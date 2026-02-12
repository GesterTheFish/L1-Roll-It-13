# Functions

def yes_no(question):

    """ Checks user response is yes/no  (y/n) returns 'yes' or 'no' """

    while True:

        # Asks if user would like to see instructions
        response = input(question).lower()

        # Checks response
        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"
        else:
            print("Please enter yes or no.")

def instructions():

    """ Prints instructions """

    print("""
    ***Instructions***
    
    Roll the dice and try to win!
    """)

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

# Main Routine

want_instructions = yes_no("Would you like to see the instructions? \n").lower()

if want_instructions == "yes" or want_instructions == "y":
    instructions()

print()
game_goal = int_check()
print(game_goal)