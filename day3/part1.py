import re

# Open File
with open('input.txt', 'r') as input_file:
    data = input_file.read()

# Get regex matches for mul(X,Y)
regex = "mul\(([0-9]*),([0-9]*)\)"
matches = re.findall(regex, data)
total = 0
for match in matches:
    n1 = int(match[0])
    n2 = int(match[1])
    total += n1 * n2

print(total)
