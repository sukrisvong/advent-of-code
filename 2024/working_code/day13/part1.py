from functools import reduce
from math import inf
import re

def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

class Location:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
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
                claw_machines[-1].button_a = Location(*re.findall(LOCATION_REGEX, line)[0])
            if line_number % 4 == 1:
                claw_machines[-1].button_b = Location(*re.findall(LOCATION_REGEX, line)[0])
            if line_number % 4 == 2:
                claw_machines[-1].prize = Location(*re.findall(LOCATION_REGEX, line)[0])
            if line_number % 4 == 3:
                claw_machines.append(ClawMachine())

    return claw_machines

def calculate_minimum_tokens_required(claw_machine):
    a_presses, b_presses = 0, 0
    x_total, y_total = 0, 0
    a_increment, b_increment = claw_machine.button_a, claw_machine.button_b
    x_target, y_target = claw_machine.prize.x, claw_machine.prize.y
    minimum_tokens_used = inf

    # Fill with A presses
    while x_total < x_target and y_total < y_target:
        a_presses += 1
        x_total += a_increment.x
        y_total += a_increment.y

    # Check if condition met
    if x_total == x_target and y_total == y_target:
        tokens_used = a_presses * 3 + b_presses
        if tokens_used < minimum_tokens_used:
            minimum_tokens_used = tokens_used

    while a_presses >= 0:
        # Decrement A by 1
        a_presses -= 1
        x_total -= a_increment.x
        y_total -= a_increment.y

        # Fill with B presses
        while x_total < x_target and y_total < y_target:
            b_presses += 1
            x_total += b_increment.x
            y_total += b_increment.y

        # Check if condition met
        if x_total == x_target and y_total == y_target:
            tokens_used = a_presses * 3 + b_presses
            if tokens_used < minimum_tokens_used:
                minimum_tokens_used = tokens_used

    return minimum_tokens_used    





claw_machines = get_claw_machines()
total_tokens = 0
for claw_machine in claw_machines:
    tokens_required = calculate_minimum_tokens_required(claw_machine)
    if tokens_required != inf:
        total_tokens += tokens_required

print(total_tokens)
