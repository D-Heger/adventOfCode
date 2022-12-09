# Read the input file
with open("input.txt", "r") as input_file:
    input_lines = input_file.readlines()

# Parse the input into a list of lists, where each sublist represents the food items
# carried by a single Elf
elf_food_items = []
current_elf_items = []
for line in input_lines:
    line = line.strip()  # Remove leading and trailing whitespace

    # If the line is empty, this signals the end of the current Elf's inventory and the start
    # of the next Elf's inventory
    if line == "":
        elf_food_items.append(current_elf_items)
        current_elf_items = []
    else:
        current_elf_items.append(int(line))

# Add the last Elf's inventory to the list
elf_food_items.append(current_elf_items)

# Find the top 3 Elves with the most food items
top_3_elves = sorted(enumerate(elf_food_items), key=lambda x: sum(x[1]), reverse=True)[:3]

# Calculate the total Calories carried by the top 3 Elves
top_3_calories = sum([sum(elf[1]) for elf in top_3_elves])

# Print the result
print(f"The top three Elves are carrying a total of {top_3_calories} Calories.")
