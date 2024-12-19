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

def get_maze():
    ACTUAL_FILE = 'input.txt'
    TEST_FILE = 'input_test.txt'
    maze = []
    with open(ACTUAL_FILE, 'r') as input_file:
        for y, line in enumerate(input_file.readlines()):
            row = []
            for x, character in enumerate(line.strip()):
                if character == START:
                    row.append((0, RIGHT))
                    start_location = (x, y)
                elif character == END:
                    end_location = (x, y)
                    row.append((inf, None))
                elif character == SPACE:
                    row.append((inf, None))
                else:
                    row.append((character, None))
            maze.append(row)

    return maze, start_location, end_location

def print_maze(maze):
    for row in maze:
        for element in row:
            if element[0] == inf:
                print(SPACE, end='')
            elif element[1] == LEFT:
                print('<', end='')
            elif element[1] == RIGHT:
                print('>', end='')
            elif element[1] == UP:
                print('^', end='')
            elif element[1] == DOWN:
                print('v', end='')
            else:
                print(element[0], end='')
        print()
    print()

def get_next_location(current_location, direction):
    return (current_location[0] + direction[0], current_location[1] + direction[1])

def location_in_maze(location, maze):
    maze_height, maze_width = len(maze[0]), len(maze)
    return 0 <= location[0] < maze_width and 0 <= location[1] < maze_height

def movement_cost(direction_1, direction_2):
    if direction_1 == direction_2:
        return 1
    if direction_1[0] == direction_2[0] or direction_1[1] == direction_2[1]:
        return 2001
    return 1001

def traverse(grid, traversed, current_location):
    locations_to_visit = []
    for direction in DIRECTIONS:
        next_location = get_next_location(current_location, direction)
        if not location_in_maze(next_location, maze):
            continue
        next_value, _ = grid[next_location[1]][next_location[0]]
        if next_value == WALL:
            continue

        score, current_direction = grid[current_location[1]][current_location[0]]
        score += movement_cost(current_direction, direction)
        if score >= next_value:
            continue

        grid[next_location[1]][next_location[0]] = (score, direction)
        locations_to_visit.append(next_location)

    traversed[current_location[1]][current_location[0]] = True

    return locations_to_visit

def traverse_all_paths(maze, start_location):
    traversed = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    locations_to_visit = traverse(maze, traversed, start_location)
    while len(locations_to_visit) > 0:
        #print_maze(maze)
        #input()
        current_location = locations_to_visit.pop(0)
        locations_to_visit += traverse(maze, traversed, current_location)
    return maze
    


maze, start_location, end_location = get_maze()
maze = traverse_all_paths(maze, start_location)
print(maze[end_location[1]][end_location[0]])
