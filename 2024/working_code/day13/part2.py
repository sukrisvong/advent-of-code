from functools import reduce
from math import inf
import re

def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'(X: {self.x}, Y: {self.y})'

class ClawMachine:
    def __init__(self):
        self.button_a = None
        self.button_b = None
        self.prize = None
    
    def __repr__(self):
        return f'Button A: {self.button_a}\nButton B: {self.button_b}\nPrize: {self.prize}'

LOCATION_REGEX = "X.([0-9]*), Y.([0-9]*)"

def get_claw_machines():
    ACTUAL_FILE = 'input.txt'
    TEST_FILE = 'input_test.txt'
    claw_machines = [ClawMachine()]
    with open(ACTUAL_FILE, 'r') as input_file:
        for line_number, line in enumerate(input_file.readlines()):
            if line_number % 4 == 0:
                claw_machines[-1].button_a = Location(*[int(n) for n in re.findall(LOCATION_REGEX, line)[0]])
            if line_number % 4 == 1:
                claw_machines[-1].button_b = Location(*[int(n) for n in re.findall(LOCATION_REGEX, line)[0]])
            if line_number % 4 == 2:
                claw_machines[-1].prize = Location(*[int(n) + 10000000000000 for n in re.findall(LOCATION_REGEX, line)[0]])
            if line_number % 4 == 3:
                claw_machines.append(ClawMachine())

    return claw_machines

# Treat this as a system of equations.
# 2 equations with 2 unknowns is solvable
def calculate_minimum_tokens_required(claw_machine):
    a_presses, b_presses = 0, 0
    x_total, y_total = 0, 0
    a, b = claw_machine.button_a, claw_machine.button_b
    t_x, t_y = claw_machine.prize.x, claw_machine.prize.y
    
    # Calculate number of b presses
    b_calc_numerator = a.x*t_y - a.y*t_x
    b_calc_denominator = b.y*a.x - b.x*a.y
    if b_calc_numerator % b_calc_denominator != 0:
        return inf
    b_presses =  b_calc_numerator // b_calc_denominator

    # Calculate number of a presses
    a_calc_numerator = t_x - b_presses * b.x
    a_calc_denominator = a.x
    if a_calc_numerator % a_calc_denominator != 0:
        return inf
    a_presses = a_calc_numerator // a_calc_denominator

    return a_presses * 3 + b_presses    

claw_machines = get_claw_machines()
total_tokens = 0
for claw_machine in claw_machines:
    tokens_required = calculate_minimum_tokens_required(claw_machine)
    if tokens_required != inf:
        total_tokens += tokens_required

print(total_tokens)
