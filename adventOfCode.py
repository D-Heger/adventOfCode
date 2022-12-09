# Read the rucksack contents from the input file
rucksacks = []
with open('input.txt') as input_file:
    for line in input_file:
        rucksacks.append(line.strip())

# Initialize the sum of priorities to 0
sum_of_priorities = 0

# For each rucksack, find the item type that appears in both compartments
# and add its priority to the sum of priorities
for rucksack in rucksacks:
    # Split the rucksack into two compartments
    first_compartment = rucksack[:len(rucksack)//2]
    second_compartment = rucksack[len(rucksack)//2:]

    # Initialize the set of item types to the empty set
    item_types = set()

    # For each character in the first compartment, add it to the set of item types
    for char in first_compartment:
        item_types.add(char)

    # For each character in the second compartment, check if it's in the set of item types
    # If it is, add its priority to the sum of priorities and break out of the loop
    for char in second_compartment:
        if char in item_types:
            # Calculate the priority of the item type
            if char.islower():
                # Lowercase item types have priorities 1 through 26
                priority = ord(char) - ord('a') + 1
            else:
                # Uppercase item types have priorities 27 through 52
                priority = ord(char) - ord('A') + 27

            # Add the priority to the sum of priorities
            sum_of_priorities += priority
            break

# Print the sum of priorities
print(sum_of_priorities)