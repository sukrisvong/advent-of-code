from functools import cache
from math import floor, log10

def get_initial_stones():
    ACTUAL_FILE = 'input.txt'
    TEST_FILE = 'input_test.txt'
    with open(ACTUAL_FILE, 'r') as input_file:
        stones = [int(word) for word in input_file.readlines()[0].strip().split(' ')]
    return stones

@cache
def stone_count(stone, depth=2):
    # Base case
    if depth == 0:
        return 1

    # Rule 1
    if stone == 0:
        return stone_count(1, depth - 1)

    # Rule 2
    stone_length = floor(log10(stone)) + 1
    if (stone_length) % 2 == 0:
        left_count = stone_count(stone // 10**(stone_length//2), depth-1)
        right_count = stone_count(stone % 10**(stone_length//2), depth-1)
        return left_count + right_count

    # Rule 3
    return stone_count(stone*2024, depth-1)

stones = get_initial_stones()
total_count = 0
for stone in stones:
    total_count += stone_count(stone, 75)
print(total_count)
