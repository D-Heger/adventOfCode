# Read the input and split it into groups of three
lines = open('input.txt').read().strip().split('\n')
groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

# Initialize the sum of priorities to 0
priority_sum = 0

# Loop through each group
for group in groups:
  # Find the common items in the group by taking the intersection
  # of the sets of items in each rucksack
  common_items = set(group[0]).intersection(group[1], group[2])

  # The badge item must be the only common item, so we can just take
  # the first item in the set of common items
  badge_item = common_items.pop()

  # Calculate the priority of the badge item by checking if it is
  # uppercase or lowercase, and adding the appropriate offset
  if badge_item.isupper():
    priority = ord(badge_item) - ord('A') + 27
  else:
    priority = ord(badge_item) - ord('a') + 1

  # Add the priority to the sum
  priority_sum += priority

# Print the final sum of priorities
print(priority_sum)