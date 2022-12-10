# Open the input file
with open("input.txt") as input_file:
  # Read the file contents
  input = input_file.read()
  # Split the file contents into lines
  input = input.splitlines()

# Parse the input and create a list of pairs of ranges
pairs = []
for line in input:
  # Split the line into two ranges
  r1, r2 = line.split(",")
  # Parse each range
  r1 = tuple(map(int, r1.split("-")))
  r2 = tuple(map(int, r2.split("-")))
  # Add the pair to the list
  pairs.append((r1, r2))

# Counter for the number of overlapping pairs
counter = 0

# Iterate over the pairs of ranges
for r1, r2 in pairs:
  # Check if the ranges overlap
  if (r1[0] <= r2[1] and r1[0] >= r2[0]) or (r2[0] <= r1[1] and r2[0] >= r1[0]):
    # If so, increment the counter
    counter += 1

# Print the final value of the counter
print(counter)
