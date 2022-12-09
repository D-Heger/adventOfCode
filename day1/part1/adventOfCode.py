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

# Find the Elf with the most food items
most_food_items = 0
most_food_items_elf = None
for i, elf_items in enumerate(elf_food_items):
    total_calories = sum(elf_items)
    if total_calories > most_food_items:
        most_food_items = total_calories
        most_food_items_elf = i

# Print the result
print(f"Elf {most_food_items_elf + 1} is carrying the most food items, with a total of {most_food_items} Calories.")
