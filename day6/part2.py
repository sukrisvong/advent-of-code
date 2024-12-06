from tqdm import tqdm

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
LOOP = "loop"
NOT_LOOP = "not_loop"

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

def move(guard_location, guard_direction, map, traversal_directions):
    map[guard_location[0]][guard_location[1]] = 'X'
    traversal_directions[guard_location[0]][guard_location[1]].add(guard_direction)
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
        return new_location, guard_direction, map, traversal_directions

    new_location_type = map[new_location[0]][new_location[1]]
    if new_location_type == OBSTACLE:
        return guard_location, next_direction(guard_direction), map, traversal_directions

    return new_location, guard_direction, map, traversal_directions

def print_map(map):
    for row in map:
        print("".join(row))
    print()

def loop_detected(guard_location, guard_direction, traversal_directions):
    if guard_direction in traversal_directions[guard_location[0]][guard_location[1]]:
        return True
    return False

def traverse_map(guard_location, guard_direction, map):
    traversal_directions = [[set() for _ in range(len(map[0]))] for _ in range(len(map))]

    while in_map(guard_location, map):
        if loop_detected(guard_location, guard_direction, traversal_directions):
            return LOOP
        guard_location, guard_direction, map, traversal_directions = move(guard_location, guard_direction, map, traversal_directions)
    return NOT_LOOP

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

loop_count = 0
for row_index, row in enumerate(tqdm(map)):
    for column_index, node in enumerate(row):
        if node == NOT_VISITED:
            new_map = [[node for node in row] for row in map]
            new_map[row_index][column_index] = OBSTACLE
            loop_outcome = traverse_map(guard_location, guard_direction, new_map)
            if loop_outcome == LOOP:
                loop_count += 1

print(loop_count)
