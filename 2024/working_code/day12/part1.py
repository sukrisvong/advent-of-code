from tqdm import tqdm

DOWN = 'down'
LEFT = 'left'
UP = 'up'
RIGHT = 'right'
DIRECTIONS = [DOWN, LEFT, UP, RIGHT]

def get_plots():
    ACTUAL_FILE = 'input.txt'
    TEST_FILE = 'input_test.txt'
    plots = []
    with open(ACTUAL_FILE, 'r') as input_file:
        for line in input_file.readlines():
            row = [character for character in line.strip()]
            plots.append(row)

    return plots


def get_next_location(location, direction):
        if direction == DOWN:
            return (location[0] - 1, location[1])
        if direction == LEFT:
            return (location[0], location[1] - 1)
        if direction == UP:
            return (location[0] + 1, location[1])
        if direction == RIGHT:
            return (location[0], location[1] + 1)

def get_region(plant, start_location, plots, traversed):
    row_size, column_size = len(plots), len(plots[0])
    region = [[0 for _ in range(len(plots[0]))] for _ in range(len(plots))]
    locations_to_visit = [start_location]
    
    while locations_to_visit:
        current_location = locations_to_visit.pop(0)
        # print(locations_to_visit)
        for direction in DIRECTIONS:
            next_location = get_next_location(current_location, direction)
            if next_location[0] < 0 or next_location[0] >= row_size or next_location[1] < 0 or next_location[1] >= column_size:
                continue

            next_plant = plots[next_location[0]][next_location[1]]
            if next_plant != plant:
                continue
            if traversed[next_location[0]][next_location[1]]:
                continue
            locations_to_visit.append(next_location)
            region[next_location[0]][next_location[1]] = 1
            traversed[next_location[0]][next_location[1]] = 1
        region[start_location[0]][start_location[1]] = 1
        traversed[current_location[0]][current_location[1]] = 1

    return region

def calculate_dimensions(region):
    area, perimeter = 0, 0
    row_size, column_size = len(region), len(region[0])
    for row_index in range(row_size):
        for column_index in range(column_size):
            # print(f'Calculating dimensions for ({row_index}, {column_index})')
            if region[row_index][column_index]:
                area += 1
            else:
                continue
            for direction in DIRECTIONS:
                next_location = get_next_location((row_index, column_index), direction)
                if next_location[0] < 0 or next_location[0] >= row_size or next_location[1] < 0 or next_location[1] >= column_size:
                    perimeter += 1
                    continue
                if not region[next_location[0]][next_location[1]]:
                    perimeter += 1
    return area, perimeter

def calculate_price(plots):
    traversed = [[0 for _ in range(len(plots[0]))] for _ in range(len(plots))]
    price = 0
    for row_index in range(len(plots)):
        for column_index in range(len(plots[0])):
            # print(f'Calculating price for ({row_index}, {column_index})')
            if traversed[row_index][column_index]:
                continue

            plant = plots[row_index][column_index]
            region = get_region(plant, (row_index, column_index), plots, traversed)
            area, perimeter = calculate_dimensions(region)
            # print(area, perimeter)
            price += area * perimeter
            '''
            for row in region:
                print(row)
            print()
            '''
    return price


plots = get_plots()
price = calculate_price(plots)
print(price)
