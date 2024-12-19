
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

def check_pattern(pattern, towels_by_length, lengths):
    lengths_checked = [set() for _ in range(len(pattern))]
    pattern_pointer = 0
    lengths_checked_pointer = 0
    potential_pattern = []
    while lengths_checked_pointer >= 0:
        # print(potential_pattern)
        if len(lengths_checked[lengths_checked_pointer]) == len(lengths):
            lengths_checked[lengths_checked_pointer] = set()
            lengths_checked_pointer -= 1
            try:
                pattern_pointer -= len(potential_pattern.pop(-1))
            except:
                pass
            continue

        match_found = False
        for length in lengths:
            if length in lengths_checked[lengths_checked_pointer]:
                continue
            lengths_checked[lengths_checked_pointer].add(length)

            start, end = pattern_pointer, pattern_pointer + length
            if end > len(pattern):
                continue
            
            target_fragment = pattern[start:end]
            # print(target_fragment)
            if target_fragment in towels_by_length[length]:
                pattern_pointer += length
                match_found = True
                potential_pattern.append(target_fragment)
                break

        if match_found:
            if pattern_pointer == len(pattern):
                return True
            lengths_checked_pointer += 1

    return False

towels, patterns = get_inputs()
towels_by_length = sort_towels_by_length(towels)
lengths = [key for key in towels_by_length.keys()]
possible_patterns = 0
for pattern in patterns:
    is_pattern_possible = check_pattern(pattern, towels_by_length, lengths)
    if is_pattern_possible:
        possible_patterns += 1
#print(towels)
#print(patterns)
#print(towels_by_length)
#print(lengths)
print(possible_patterns)