TRAILHEAD = '0'
TRAILEND = '9'
DOWN = 'down'
LEFT = 'left'
UP = 'up'
RIGHT = 'right'
DIRECTIONS = [DOWN, LEFT, UP, RIGHT]

TEST_FILE = 'input_test.txt'
ACTUAL_FILE = 'input.txt'

def get_heights():
    with open(TEST_FILE, 'r') as input_file:
        heights = []
        for line in input_file.readlines():
            row = []
            for character in line.strip():
                row.append(character)
            heights.append(row)
        return heights

def get_next_location(location, direction):
        if direction == DOWN:
            return (location[0] - 1, location[1])
        if direction == LEFT:
            return (location[0], location[1] - 1)
        if direction == UP:
            return (location[0] + 1, location[1])
        if direction == RIGHT:
            return (location[0], location[1] + 1)

def traverse(heights, traversed, start_location):
    row_size, column_size = len(heights), len(heights[0])
    locations_to_visit = []
    for direction in DIRECTIONS:
        next_location = get_next_location(start_location, direction)
        if next_location[0] < 0 or next_location[0] >= row_size or next_location[1] < 0 or next_location[1] >= column_size:
            continue

        start_height = int(heights[start_location[0]][start_location[1]])
        next_height = int(heights[next_location[0]][next_location[1]])
        if next_height != start_height + 1:
            continue
        # if traversed[next_location[0]][next_location[1]]:
        #     continue
        locations_to_visit.append(next_location)
    # traversed[start_location[0]][start_location[1]] = True

    return locations_to_visit

def calculate_score(heights, start_location):
    traversed = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
    locations_to_visit = traverse(heights, traversed, start_location)
    score = 0
    while len(locations_to_visit) > 0:
        next_location = locations_to_visit.pop(0)
        # if traversed[next_location[0]][next_location[1]]:
        #     continue
        if heights[next_location[0]][next_location[1]] == TRAILEND:
            score += 1
            # traversed[next_location[0]][next_location[1]] = True
            continue
        locations_to_visit += traverse(heights, traversed, next_location)
    return score

heights = get_heights()
trailhead_scores = 0
for row_index, row in enumerate(heights):
    for column_index, height in enumerate(row):
        if height == TRAILHEAD:
            height_location = (row_index, column_index)
            trailhead_scores += calculate_score(heights, height_location)
print(trailhead_scores)
