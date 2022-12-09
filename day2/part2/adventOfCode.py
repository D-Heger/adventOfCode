# define the possible shapes and their corresponding scores
SHAPES = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}

# define the mapping from opponent's shape to your shape for each goal
GOAL_MAP = {
    "X": {  # lose
        "A": "C",  # if opponent plays Rock, play Scissors
        "B": "A",  # if opponent plays Paper, play Rock
        "C": "B"   # if opponent plays Scissors, play Paper
    },
    "Y": {  # draw
        "A": "A",  # if opponent plays Rock, play Rock
        "B": "B",  # if opponent plays Paper, play Paper
        "C": "C"   # if opponent plays Scissors, play Scissors
    },
    "Z": {  # win
        "A": "B",  # if opponent plays Rock, play Paper
        "B": "C",  # if opponent plays Paper, play Scissors
        "C": "A"   # if opponent plays Scissors, play Rock
    }
}

# read the input file line by line
with open("input.txt", "r") as f:
    lines = f.readlines()

# initialize the total score to 0
total_score = 0
score = 0

# iterate over each line in the input file
for line in lines:
    # split the line into the opponent's shape and the goal
    opponent_shape, goal = line.split()

    # get your shape for the current goal and opponent's shape
    your_shape = GOAL_MAP[goal][opponent_shape]

    # calculate the score for the current round
    if goal == "X":
      if opponent_shape == "A" and your_shape == "C":  # lose Rock to Scissors
        score = 3
      elif opponent_shape == "B" and your_shape == "A": # lose Paper to Rock
        score = 1
      elif opponent_shape == "C" and your_shape == "B": # lose Scissors to Paper
        score = 2
    elif goal == "Y":
      if opponent_shape == "A" and your_shape == "A": # draw Rock to Rock
        score = 1 + 3
      elif opponent_shape == "B" and your_shape == "B": # draw Paper to Paper
        score = 2 + 3
      elif opponent_shape == "C" and your_shape == "C": # draw Scissors to Scissors
        score = 3 + 3
    elif goal == "Z":
      if opponent_shape == "A" and your_shape == "B": # win Rock to Paper
        score = 2 + 6
      elif opponent_shape == "B" and your_shape == "C": # win Paper to Scissors
        score = 3 + 6
      elif opponent_shape == "C" and your_shape == "A": # win Scissors to Rock
        score = 1 + 6
        

    # add the score for the current round to the total score
    total_score += score

# print the final total score
print(f"Total score: {total_score}")