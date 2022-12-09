# Define a mapping from handsigns to integers
handsigns = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}

# Read the input file line by line
with open("input.txt") as input_file:
    lines = input_file.readlines()

# Parse the input lines and calculate the total score
total_score = 0
for line in lines:
    # Split the line into the opponent's and player's handsign
    opponent, player = line.strip().split()

    # Calculate the score for the player's handsign
    player_score = 0
    if player == "X":
        player_score = 1
    elif player == "Y":
        player_score = 2
    elif player == "Z":
        player_score = 3

    # Calculate the outcome of the Rock, Paper, Scissors game
    outcome = 0
    if handsigns[opponent] == handsigns[player]:
        # If both handsigns are the same, the round is a draw
        outcome = 3
    elif (handsigns[opponent] + 1) % 3 == handsigns[player]:
        # If the player's handsign wins, the player gets 6 points
        outcome = 6
    else:
        # Otherwise, the player gets 0 points
        outcome = 0

    # Calculate the score for the round and add it to the total score
    round_score = player_score + outcome
    total_score += round_score

# Print the total score
print(total_score)
