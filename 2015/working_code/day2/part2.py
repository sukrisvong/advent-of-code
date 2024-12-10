total = 0
with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        edges = [int(character) for character in line.strip().split('x')]
        edges.sort()
        total += (2*edges[0] + 2*edges[1]) + edges[0] * edges[1] * edges[2]

print(total)
