# Set scores to 0
user_score = 0
comp_score = 0

game_goal = int(input("Enter the game goal: "))

# Play until winner is decided
while comp_score < game_goal and user_score < game_goal:

    # Start of round loop
    # Ask user for both scores
    comp_points = int(input("Enter the computer points at the end of the round: "))
    user_points = int(input("Enter the user points at the end of the round: "))

    # Update score
    comp_score += comp_points
    user_score += user_points

    # Show overall scores
    print("*** Game Update ***")
    print(f"User score: {user_score} | Computer score: {comp_score}")

# End of game output final results
print()
if user_score > comp_score:
    winner = "user"
else:
    winner = "computer"
print(f"The {winner} won.")