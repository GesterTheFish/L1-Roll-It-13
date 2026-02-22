import random

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

def initial_points(which_player):
    """Roll the dice twice and return total / if double points apply"""

    double = "no"

    # Roll dice for user and check for double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total}")

    return total, double

def make_statement(statement, decoration):
    """Adds emojis / additional characters to headings"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")

# Main routine

# Set variables to 0
user_score = 0
comp_score = 0
rounds_played = 0

game_history = []

# Welcome statement
make_statement("Welcome to Roll It 13.", "☘️")

# Ask user if they want to see instructions
want_instructions = yes_no("Would you like to see the instructions? \n").lower()

if want_instructions == "yes" or want_instructions == "y":
    instructions()

print()
game_goal = int_check()

# Play until winner is decided
while comp_score < game_goal and user_score < game_goal:

    # Start of round loop
    rounds_played += 1
    make_statement(f"Round {rounds_played}", "🎲")

    # Roll for user and check for double
    initial_user = initial_points("User")
    initial_comp = initial_points("Comp")

    # Retrieve user points
    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]

    # Tell the user they get double points
    if double_user == "yes":
        print("Great news, if you win you'll get double points!")

    # Make user go first
    first = "User"
    second = "Computer"
    player_1_points = user_points
    player_2_points = comp_points

    # If user has fewer points, they start
    if user_points < comp_points:
        print("You start because your initial roll was less than the computer \n")
    # If they roll the same the user starts
    elif user_points == comp_points:
        print("Initial rolls were the same, you start.")
    # If computer has fewer points, it starts
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    # Loop until we have a winner
    while player_1_points < 13 and player_2_points < 13:
        print()
        input("Press <enter> to continue\n")

        # First person rolls and score is updated1
        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: Rolled a {player_1_roll} and has {player_1_points} points.")

        # If first players score is over 13 end round
        if player_1_points >= 13:
            break

        # Second person rolls and score is updated
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}: Rolled a {player_2_roll} and has {player_2_points} points.")

        print(f"{first}: {player_1_points} | {second}: {player_2_points}")

    # End of round

    # Associate points with player
    user_points = player_1_points
    comp_points = player_2_points

    # Switch if computer is player 1
    if first == "Computer":
        user_points, comp_points = comp_points, user_points

    # Check who won
    if user_points > comp_points:
        winner = "user"
        loser = "computer"
        comp_points = 0
    else:
        winner = "computer"
        loser = "user"
        user_points = 0

    round_feedback = f"The {winner} won. The {loser}'s points have been reset to zero."

    # Double user points if eligible
    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    # Output round results
    make_statement("Round Results", "=")
    print(f"User points: {user_points} | Computer points: {comp_points}")
    print(round_feedback)
    print()

    # Update score
    comp_score += comp_points
    user_score += user_points

    # Generate round results and dd to history list
    game_results = f"Round {rounds_played}: User Points {user_points} | Computer Points {comp_points}, {winner} wins ({user_score} | {comp_score})"

    game_history.append(game_results)

    # Show overall scores
    print("*** Game Update ***")
    print(f"User score: {user_score} | Computer score: {comp_score}")

# End of game output final results

make_statement("Game Over", "🏁 ")

print()
if user_score > comp_score:
    winner = "user"
else:
    winner = "computer"
make_statement(f"The {winner} won", "👑")

make_statement("Game History", "🎲")

for item in game_history:
    print(item)