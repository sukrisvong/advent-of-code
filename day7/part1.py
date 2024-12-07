# define constants
MULTIPLY = '0'
ADD = '1'
OPERATORS = [MULTIPLY, ADD]

"""
MAIN FUNCTIONALITY
"""
map = []
obstacle_locations = []
guard_location = (-1, -1)
guard_direction = ""

def parse_line(line):
    line = line.split(':')
    total = int(line[0])
    numbers = [int(number) for number in line[1].strip().split(' ')]
    return total, numbers

def calculate(numbers, operators):
    running_total = numbers[0]
    # print("calculating: " + str(numbers) + " : " + operators)
    for n in range(len(operators)):
        operator, number = operators[n],numbers[n+1]
        if operator == MULTIPLY:
            running_total *= number
        if operator == ADD:
            running_total += number
        # print(running_total)
    return running_total

def value_of_solution(total, numbers):
    number_of_operators = len(numbers)-1
    binary_format_string = "#0" + str(number_of_operators+2) + "b"

    for n in range((2**number_of_operators)):
        n_as_binary = format(n, binary_format_string)[2:]
        # print(str(n) + "/" + str(number_of_operators**2) + ": " + n_as_binary)
        calculated_total = calculate(numbers, n_as_binary)
        if calculated_total == total:
            return calculated_total
    return 0

class Equation:
    def __init__(self, total, numbers):
        self.total = total
        self.numbers = numbers

    def __repr__(self):
        return str(self.total) + ':' + str(self.numbers)

# Get equations
equations = []
with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        total, numbers = parse_line(line)
        equations.append(Equation(total, numbers))

total = 0
for equation in equations:
    # print(equation)
    total += value_of_solution(equation.total, equation.numbers)

print(total)