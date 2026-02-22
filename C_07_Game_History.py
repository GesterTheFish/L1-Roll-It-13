# Initialize list to hold game history
game_history = []

# Get data  (Base does this already)
user_score = 0
comp_score = 0

while True:
    rounds_played = input("Round: ")
    if rounds_played == "":
        break

    user_points = int(input("User Points: "))
    comp_points = int(input("Comp Points: "))
    winner = input("Winner: ")
    user_score = int(input("User Score: "))
    comp_score = int(input("Comp Score: "))

    game_results = f"Round {rounds_played}: User Points {user_points} | Computer Points {comp_points}, {winner} wins ({user_score} | {comp_score})"

    game_history.append(game_results)

print("Game History")

for item in game_history:
    print(item)