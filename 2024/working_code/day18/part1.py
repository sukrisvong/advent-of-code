SPACE = '.'
WALL = '#'
GRID_WIDTH = 71
GRID_HEIGHT = 71
START_LOCATION = (0,0)
END_LOCATION = (GRID_WIDTH-1, GRID_HEIGHT-1)

# Directions in (X,Y)
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)
DIRECTIONS = [LEFT, RIGHT, UP, DOWN]

def get_grid():
    ACTUAL_FILE = 'input.txt'
    TEST_FILE = 'input_test.txt'
    grid = [[SPACE for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    with open(ACTUAL_FILE, 'r') as input_file:
        for line_number, line in enumerate(input_file.readlines()):
            if line_number > 1024 - 1:
                break
            x, y = [int(n) for n in line.strip().split(',')]
            grid[y][x] = WALL
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

def get_next_location(current_location, direction):
    return (current_location[0] + direction[0], current_location[1] + direction[1])

def location_in_grid(location):
    return 0 <= location[0] < GRID_WIDTH and 0 <= location[1] < GRID_HEIGHT

def traverse(grid, traversed, current_location):
    locations_to_visit = []
    for direction in DIRECTIONS:
        next_location = get_next_location(current_location, direction)
        if not location_in_grid(next_location):
            continue
        if traversed[next_location[1]][next_location[0]]:
            continue
        if grid[next_location[1]][next_location[0]] == WALL:
            continue

        locations_to_visit.append(next_location)
    traversed[current_location[1]][current_location[0]] = True

    return locations_to_visit

def get_length_of_shortest_path(grid):
    traversed = [[False for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    locations_to_visit = traverse(grid, traversed, START_LOCATION)
    path_length = 0
    nodes_in_previous_level = len(locations_to_visit)
    nodes_in_current_level = 0
    while len(locations_to_visit) > 0:
        next_location = locations_to_visit.pop(0)
        if traversed[next_location[1]][next_location[0]]:
            continue
        if next_location == END_LOCATION:
            return True, path_length + 1
        locations_to_add = traverse(grid, traversed, next_location)

        added_locations = 0
        for location in locations_to_add:
            if location in locations_to_visit:
                continue
            locations_to_visit.append(location)
            added_locations += 1

        nodes_in_previous_level -= 1
        nodes_in_current_level += added_locations
        if nodes_in_previous_level == 0:
            nodes_in_previous_level = nodes_in_current_level
            nodes_in_current_level = 0
            path_length += 1

    return False, path_length

grid = get_grid()
print_grid(grid)
found_path, path_length = get_length_of_shortest_path(grid)
print(path_length)