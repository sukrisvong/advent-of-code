WALL = '#'
BOX = 'O'
BOX_LEFT = '['
BOX_RIGHT = ']'
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
                row = []
                for c in line.strip():
                    if c == WALL:
                        row.append(WALL)
                        row.append(WALL)
                    if c == BOX:
                        row.append(BOX_LEFT)
                        row.append(BOX_RIGHT)
                    if c == SPACE:
                        row.append(SPACE)
                        row.append(SPACE)
                    if c == ROBOT:
                        row.append(ROBOT)
                        row.append(SPACE)
                map.append(row)
            else:
                moves += [c for c in line.strip()]

    return map, moves

def find_robot_location(map):
    for row_index, row in enumerate(map):
        for column_index, character in enumerate(row):
            if character == ROBOT:
                return row_index, column_index

def can_move_up(map, location, width):
    if width == 1:
        next_location = (location[0] - 1, location[1])
        next_character = map[next_location[0]][next_location[1]]
        if next_character == SPACE:
            return True, [location]
        if next_character == WALL:
            return False, []
        if next_character == BOX_LEFT:
            result = can_move_up(map, (next_location[0], next_location[1]), 2)
            if result[0]:
                return True, [location] + result[1]
            return False, []
        if next_character == BOX_RIGHT:
            result = can_move_up(map, (next_location[0], next_location[1] - 1), 2)
            if result[0]:
                return True, [location] + result[1]
            return False, []
    if width == 2:
        next_locations = ((location[0] - 1, location[1]), (location[0] - 1, location[1] + 1))
        next_characters = (map[next_locations[0][0]][next_locations[0][1]], map[next_locations[1][0]][next_locations[1][1]])
        if next_characters == (SPACE, SPACE):
            return True, [location]
        if WALL in next_characters:
            return False, []
        if next_characters == (BOX_LEFT, BOX_RIGHT):
            result = can_move_up(map, (next_locations[0][0], next_locations[0][1]), 2)
            if result[0]:
                return True, [location] + result[1]
            return False, []
        if next_characters == (BOX_RIGHT, BOX_LEFT):
            can_move_up_left = can_move_up(map, (next_locations[0][0], next_locations[0][1] - 1), 2)
            can_move_up_right = can_move_up(map, (next_locations[1][0], next_locations[1][1]), 2)
            if can_move_up_left[0] and can_move_up_right[0]:
                return True, [location] + can_move_up_left[1] + can_move_up_right[1]
            return False, []
        if next_characters == (SPACE, BOX_LEFT):
            result = can_move_up(map, (next_locations[1][0], next_locations[1][1]), 2)
            if result[0]:
                return True, [location] + result[1]
            return False, []
        if next_characters == (BOX_RIGHT, SPACE):
            result = can_move_up(map, (next_locations[0][0], next_locations[0][1] - 1), 2)
            if result[0]:
                return True, [location] + result[1]
            return False, []

def can_move_down(map, location, width):
    if width == 1:
        next_location = (location[0] + 1, location[1])
        next_character = map[next_location[0]][next_location[1]]
        if next_character == SPACE:
            return True, [location]
        if next_character == WALL:
            return False, []
        if next_character == BOX_LEFT:
            result = can_move_down(map, (next_location[0], next_location[1]), 2)
            if result[0]:
                return True, [location] + result[1]
            return False, []
        if next_character == BOX_RIGHT:
            result = can_move_down(map, (next_location[0], next_location[1] - 1), 2)
            if result[0]:
                return True, [location] + result[1]
            return False, []
    if width == 2:
        next_locations = ((location[0] + 1, location[1]), (location[0] + 1, location[1] + 1))
        next_characters = (map[next_locations[0][0]][next_locations[0][1]], map[next_locations[1][0]][next_locations[1][1]])
        if next_characters == (SPACE, SPACE):
            return True, [location]
        if WALL in next_characters:
            return False, []
        if next_characters == (BOX_LEFT, BOX_RIGHT):
            result = can_move_down(map, (next_locations[0][0], next_locations[0][1]), 2)
            if result[0]:
                return True, [location] + result[1]
            return False, []
        if next_characters == (BOX_RIGHT, BOX_LEFT):
            can_move_down_left = can_move_down(map, (next_locations[0][0], next_locations[0][1] - 1), 2)
            can_move_down_right = can_move_down(map, (next_locations[1][0], next_locations[1][1]), 2)
            if can_move_down_left[0] and can_move_down_right[0]:
                return True, [location] + can_move_down_left[1] + can_move_down_right[1]
            return False, []
        if next_characters == (SPACE, BOX_LEFT):
            result = can_move_down(map, (next_locations[1][0], next_locations[1][1]), 2)
            if result[0]:
                return True, [location] + result[1]
            return False, []
        if next_characters == (BOX_RIGHT, SPACE):
            result = can_move_down(map, (next_locations[0][0], next_locations[0][1] - 1), 2)
            if result[0]:
                return True, [location] + result[1]
            return False, []

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
        can_move, items_to_move = can_move_up(map, robot_start_location, 1)
        if not can_move:
            return map, robot_start_location
        items_to_move.remove(robot_start_location)
        sorted_items_to_move = sorted(items_to_move, key=lambda x: x[0])
        for item_location in sorted_items_to_move:
            map[item_location[0]][item_location[1]] = SPACE
            map[item_location[0]][item_location[1] + 1] = SPACE
            map[item_location[0] - 1][item_location[1]] = BOX_LEFT
            map[item_location[0] - 1][item_location[1] + 1] = BOX_RIGHT

        robot_next_location = (robot_start_location[0] - 1, robot_start_location[1])
        map[robot_next_location[0]][robot_next_location[1]] = ROBOT
        map[robot_start_location[0]][robot_start_location[1]] = SPACE
        return map, robot_next_location

    if direction == DOWN:
        can_move, items_to_move = can_move_down(map, robot_start_location, 1)
        if not can_move:
            return map, robot_start_location
        items_to_move.remove(robot_start_location)
        sorted_items_to_move = sorted(items_to_move, key=lambda x: x[0])
        sorted_items_to_move.reverse()
        for item_location in sorted_items_to_move:
            map[item_location[0]][item_location[1]] = SPACE
            map[item_location[0]][item_location[1] + 1] = SPACE
            map[item_location[0] + 1][item_location[1]] = BOX_LEFT
            map[item_location[0] + 1][item_location[1] + 1] = BOX_RIGHT

        robot_next_location = (robot_start_location[0] + 1, robot_start_location[1])
        map[robot_next_location[0]][robot_next_location[1]] = ROBOT
        map[robot_start_location[0]][robot_start_location[1]] = SPACE
        return map, robot_next_location

def calculate(map):
    sum = 0
    for row_index, row in enumerate(map):
        for column_index, character in enumerate(row):
            if character == BOX_LEFT:
                sum += row_index * 100 + column_index
    return sum


map, moves = get_inputs()
'''
for row in map:
    print(''.join(row))
print()
'''
robot_location = find_robot_location(map)
for move_number, direction in enumerate(moves):
    map, robot_location = move(map, robot_location, direction)
    '''
    print(f'Step {move_number}: {direction}')
    for row in map:
        print(''.join(row))
    print()
    #input()
    '''
print(calculate(map))


