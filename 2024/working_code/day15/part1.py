WALL = '#'
BOX = 'O'
ROBOT = '@'
SPACE = '.'

LEFT = '<'
UP = '^'
DOWN = 'v'
RIGHT = '>'

def get_inputs():
    ACTUAL_FILE = 'input.txt'
    TEST_FILE = 'input_test.txt'
    map, moves = [], []
    with open(ACTUAL_FILE, 'r') as input_file:
        array_to_fill = 'map'
        for line in input_file.readlines():
            if line.strip() == '':
                array_to_fill = 'moves'
                continue

            if array_to_fill == 'map':
                map.append([c for c in line.strip()])
            else:
                moves += [c for c in line.strip()]

    return map, moves

def find_robot_location(map):
    for row_index, row in enumerate(map):
        for column_index, character in enumerate(row):
            if character == ROBOT:
                return row_index, column_index

def move(map, robot_start_location, direction):
    row_index, column_index = robot_start_location
    if direction == LEFT:
        while True:
            column_index -= 1
            next_character = map[row_index][column_index]

            if next_character == SPACE:
                break
            if next_character == WALL:
                return map, robot_start_location

        for n in range(column_index, robot_start_location[1]):
            map[row_index][n] = map[row_index][n+1]
        map[row_index][robot_start_location[1]] = SPACE
        return map, (row_index, robot_start_location[1] - 1)

    if direction == RIGHT:
        while True:
            column_index += 1
            next_character = map[row_index][column_index]

            if next_character == SPACE:
                break
            if next_character == WALL:
                return map, robot_start_location

        for n in range(column_index, robot_start_location[1], -1):
            map[row_index][n] = map[row_index][n-1]
        map[row_index][robot_start_location[1]] = SPACE
        return map, (row_index, robot_start_location[1] + 1)

    if direction == UP:
        while True:
            row_index -= 1
            next_character = map[row_index][column_index]

            if next_character == SPACE:
                break
            if next_character == WALL:
                return map, robot_start_location

        for n in range(row_index, robot_start_location[0]):
            map[n][column_index] = map[n+1][column_index]
        map[robot_start_location[0]][column_index] = SPACE
        return map, (robot_start_location[0] - 1, column_index)

    if direction == DOWN:
        while True:
            row_index += 1
            next_character = map[row_index][column_index]

            if next_character == SPACE:
                break
            if next_character == WALL:
                return map, robot_start_location

        for n in range(row_index, robot_start_location[0], -1):
            map[n][column_index] = map[n-1][column_index]
        map[robot_start_location[0]][column_index] = SPACE
        return map, (robot_start_location[0] + 1, column_index)

def calculate(map):
    sum = 0
    for row_index, row in enumerate(map):
        for column_index, character in enumerate(row):
            if character == BOX:
                sum += row_index * 100 + column_index
    return sum


map, moves = get_inputs()
robot_location = find_robot_location(map)
for direction in moves:
    map, robot_location = move(map, robot_location, direction)
    '''
    print(f'Moved: {direction}')
    for row in map:
        print(row)
    print()
    '''
print(calculate(map))


