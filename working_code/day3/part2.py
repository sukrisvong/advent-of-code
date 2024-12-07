import re

# Open File
with open('input.txt', 'r') as input_file:
    data = input_file.read()

# Get regex matches for mul(X,Y)
do_regex = "(do\(\))"
dont_regex = "(don't\(\))"
mul_regex = "mul\(([0-9]*),([0-9]*)\)"
regex = f'{do_regex}|{dont_regex}|{mul_regex}'
matches = re.findall(regex, data)
total = 0
enabled = True
for match in matches:
    if match[0] == "do()":
        enabled = True
    elif match[1] == "don't()":
        enabled = False
    elif enabled:
        n1 = int(match[2])
        n2 = int(match[3])
        total += n1 * n2

print(total)