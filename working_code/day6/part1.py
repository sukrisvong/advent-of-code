"""
CONSTANTS
"""
UP = "^"
RIGHT = ">"
DOWN = "v"
LEFT = "<"
OBSTACLE = "#"
NOT_VISITED = "."
VISITED = "X"

"""
HELPER FUNCTIONS
"""
def in_map(guard_location, map):
    for index in guard_location:
        if index < 0 or index > len(map) - 1:
            return False
    return True

def next_direction(guard_direction):
    if guard_direction == UP:
        return RIGHT
    if guard_direction == RIGHT:
        return DOWN
    if guard_direction == DOWN:
        return LEFT
    if guard_direction == LEFT:
        return UP

def move(guard_location, guard_direction, map):
    map[guard_location[0]][guard_location[1]] = 'X'
    new_location = (-1,-1)

    if guard_direction == UP:
        new_location = (guard_location[0]-1, guard_location[1])
    if guard_direction == RIGHT:
        new_location = (guard_location[0], guard_location[1]+1)
    if guard_direction == DOWN:
        new_location = (guard_location[0]+1, guard_location[1])
    if guard_direction == LEFT:
        new_location = (guard_location[0], guard_location[1]-1)

    if not in_map(new_location, map):
        return new_location, guard_direction, map

    new_location_type = map[new_location[0]][new_location[1]]
    if new_location_type == OBSTACLE:
        return guard_location, next_direction(guard_direction), map

    return new_location, guard_direction, map

def print_map(map):
    for row in map:
        print("".join(row))
    print()

"""
MAIN FUNCTIONALITY
"""
map = []
obstacle_locations = []
guard_location = (-1, -1)
guard_direction = ""

# Get input map
with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        map.append([character for character in line.strip()])

# Parse information from map
for row_index, row in enumerate(map):
    for column_index, character in enumerate(row):
        location = (row_index, column_index)
        if character == OBSTACLE:
            obstacle_locations.append(location)
        if character == UP:
            guard_location = location
            guard_direction = UP
        if character == RIGHT:
            guard_location = location
            guard_direction = RIGHT
        if character == DOWN:
            guard_location = location
            guard_direction = DOWN
        if character == LEFT:
            guard_location = location
            guard_direction = LEFT

# Traverse map
while in_map(guard_location, map):
    guard_location, guard_direction, map = move(guard_location, guard_direction, map)

# Count traversals
visited_count = 0
for row in map:
    for position in row:
        if position == VISITED:
            visited_count += 1

print(visited_count)
