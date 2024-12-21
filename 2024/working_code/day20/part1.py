from math import inf

# Cells on map
WALL = '#'
START = 'S'
END = 'E'
SPACE = '.'

# Directions in (X,Y)
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)
DIRECTIONS = [LEFT, RIGHT, UP, DOWN]

def get_grid():
    ACTUAL_FILE = 'input.txt'
    TEST_FILE = 'input_test.txt'
    grid = []
    with open(ACTUAL_FILE, 'r') as input_file:
        for y, line in enumerate(input_file.readlines()):
            row = []
            for x, character in enumerate(line.strip()):
                if character == START:
                    start_location = (x, y)
                    row.append(0)
                elif character == END:
                    end_location = (x, y)
                    row.append(inf)
                elif character == SPACE:
                    row.append(inf)
                else:
                    row.append(character)
            grid.append(row)

    return grid, start_location, end_location

def copy_grid(grid):
    copied_grid = []
    for row in grid:
        copied_grid.append([element for element in row])
    return copied_grid

def print_grid(grid):
    for row in grid:
        for element in row:
            if element == WALL:
                print(WALL, end='')
            else:
                print('.', end='')
        print()
    print()

def get_next_location(current_location, direction):
    return (current_location[0] + direction[0], current_location[1] + direction[1])

def location_in_grid(location, grid):
    grid_width, grid_height = len(grid[0]), len(grid)
    return 0 <= location[0] < grid_width and 0 <= location[1] < grid_height

def traverse_without_cheats(grid, current_location):
    locations_to_visit = []
    for direction in DIRECTIONS:
        next_location = get_next_location(current_location, direction)
        if not location_in_grid(next_location, grid):
            continue
        if grid[next_location[1]][next_location[0]] == WALL:
            continue
        current_time = grid[current_location[1]][current_location[0]]
        next_time = current_time + 1
        if grid[next_location[1]][next_location[0]] <= next_time:
            continue

        grid[next_location[1]][next_location[0]] = next_time
        locations_to_visit.append(next_location)

    return locations_to_visit

def traverse_with_cheats(initial_grid, current_location, faster_times, depth, time_threshold):
    for direction in DIRECTIONS:
        grid = copy_grid(initial_grid)
        '''
        input()
        print(depth)
        print(faster_times)
        print(direction)
        print_grid(grid)
        '''
        next_location = get_next_location(current_location, direction)
        if not location_in_grid(next_location, grid):
            continue
        current_time = grid[current_location[1]][current_location[0]]
        next_time = current_time + 1
        if grid[next_location[1]][next_location[0]] == WALL:
            grid[next_location[1]][next_location[0]] = next_time
        elif grid[next_location[1]][next_location[0]] <= next_time:
            continue

        time_difference = grid[next_location[1]][next_location[0]] - next_time
        if time_difference >= time_threshold:
            faster_times.append(time_difference)
            continue
        grid[next_location[1]][next_location[0]] = next_time
        if depth > 0:
            faster_times = traverse_with_cheats(copy_grid(grid), next_location, faster_times, depth-1, time_threshold)

    return faster_times

def initial_traversal(grid, start_location):
    locations_to_visit = traverse_without_cheats(grid, start_location)
    route = [start_location]
    while len(locations_to_visit) > 0:
        next_location = locations_to_visit.pop(0)
        route.append(next_location)
        locations_to_visit += traverse_without_cheats(grid, next_location)

    return grid, route

grid, start_location, end_location = get_grid()
grid, route = initial_traversal(grid, start_location)
default_time = grid[end_location[1]][end_location[0]]
faster_times = []
for location in route:
    faster_times += traverse_with_cheats(copy_grid(grid), location, [], 1, 100)
print(len(faster_times))

'''
cheat_counts = {}
for location in route:
    faster_times = traverse_with_cheats(copy_grid(grid), location, [], 1)
    for faster_time in faster_times:
        if faster_time in cheat_counts:
            cheat_counts[faster_time] += 1
        else:
            cheat_counts[faster_time] = 1
cheat_counts = dict(sorted(cheat_counts.items()))
print(cheat_counts)
'''
