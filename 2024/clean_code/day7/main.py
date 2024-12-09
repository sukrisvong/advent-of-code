from helpers.ValueCalculator import ValueCalculator
from helpers.InputParser import InputParser
from tqdm import tqdm

part_1_total, part_2_total = 0, 0
with open('inputs/input_test.txt', 'r') as input_file:
    for line in tqdm(input_file.readlines()):
        total, numbers = InputParser(line).parse_input()
        part_1_total += ValueCalculator(total, numbers, 2).calculate()
        part_2_total += ValueCalculator(total, numbers, 3).calculate()

print(f'Part 1 Total: {part_1_total}')
print(f'Part 2 Total: {part_2_total}')
