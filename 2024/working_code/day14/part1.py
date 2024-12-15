import re


GRID_HEIGHT, GRID_WIDTH = 103, 101
GRID_X_MIDPOINT = GRID_WIDTH // 2
GRID_Y_MIDPOINT = GRID_HEIGHT // 2
PART_1_INCREMENTS = 100

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'

class Robot:
    def __init__(self, start_position, velocity):
        self.start_position = start_position
        self.velocity = velocity


    def calculate_end_location(self, increments):
        x_distance, y_distance = self.velocity.x * increments, self.velocity.y * increments
        x_end_position, y_end_position = self.start_position.x + x_distance, self.start_position.y + y_distance
        x_grid_position, y_grid_position = x_end_position % GRID_WIDTH, y_end_position % GRID_HEIGHT

        return Location(x_grid_position, y_grid_position)

    def __repr__(self):
        return f'p=({self.start_position.x},{self.start_position.y}) v=({self.velocity.x},{self.velocity.y})'

LOCATION_REGEX = "p=(\-?[0-9]*),(\-?[0-9]*) v=(\-?[0-9]*),(\-?[0-9]*)"

def get_robots():
    ACTUAL_FILE = 'input.txt'
    TEST_FILE = 'input_test.txt'
    robots = []
    with open(ACTUAL_FILE, 'r') as input_file:
        for line in input_file.readlines():
            matches = [int(n) for n in re.findall(LOCATION_REGEX, line.strip())[0]]
            locations = (Location(matches[0],matches[1]), Location(matches[2], matches[3]))
            robots.append(Robot(*locations))
            # claw_machines[-1].button_a = Location(*[int(n) for n in re.findall(LOCATION_REGEX, line)[0]])

    return robots

def calculate_safety_factor(grid):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for row_index, row in enumerate(grid):
        for column_index, robot_count in enumerate(row):
            if row_index < GRID_Y_MIDPOINT and column_index < GRID_X_MIDPOINT:
                q1 += robot_count
            if row_index < GRID_Y_MIDPOINT and column_index > GRID_X_MIDPOINT:
                q2 += robot_count
            if row_index > GRID_Y_MIDPOINT and column_index < GRID_X_MIDPOINT:
                q3 += robot_count
            if row_index > GRID_Y_MIDPOINT and column_index > GRID_X_MIDPOINT:
                q4 += robot_count

    return q1 * q2 * q3 * q4


grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
robots = get_robots()
for robot in robots:
    end_location = robot.calculate_end_location(PART_1_INCREMENTS)
    grid[end_location.y][end_location.x] += 1

safety_factor = calculate_safety_factor(grid)
print(safety_factor)



