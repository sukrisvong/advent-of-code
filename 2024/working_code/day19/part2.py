from functools import cache

def get_inputs():
    ACTUAL_FILE = 'input.txt'
    TEST_FILE = 'input_test.txt'
    towels = []
    patterns = []
    with open(ACTUAL_FILE, 'r') as input_file:
        for line_number, line in enumerate(input_file.readlines()):
            if line_number == 0:
                towels = line.strip().split(', ')
            if line_number > 1:
                patterns.append(line.strip())
    return towels, patterns

def sort_towels_by_length(towels):
    towels_by_length = {}
    for towel in towels:
        length = len(towel)
        if length in towels_by_length:
            towels_by_length[length].append(towel)
        else:
            towels_by_length[length] = [towel]

    return towels_by_length

@cache
def calculate_possible_combinations(pattern):
    global towels_by_length
    global lengths

    if pattern == '':
        return 0

    possible_patterns = 0
    for length in lengths:
        if length > len(pattern):
            continue

        if not pattern[:length] in towels_by_length[length]:
            continue

        if length == len(pattern):
            possible_patterns += 1

        possible_patterns += calculate_possible_combinations(pattern[length:])

    return possible_patterns


towels, patterns = get_inputs()
towels_by_length = sort_towels_by_length(towels)
lengths = [key for key in towels_by_length.keys()]
possible_patterns = 0
for pattern in patterns:
    possible_patterns += calculate_possible_combinations(pattern)
print(possible_patterns)