A = 0
B = 1
C = 2

def get_inputs():
    ACTUAL_FILE = 'input.txt'
    TEST_FILE = 'input_test.txt'
    registers = []
    program = None
    with open(TEST_FILE, 'r') as input_file:
        for row_index, line in enumerate(input_file.readlines()):
            if row_index < 3:
                registers.append(int(line.strip().split(' ')[-1]))
            if row_index > 3:
                program = [int(n) for n in line.strip().split(' ')[-1].split(',')]

    return registers, program

registers, program = get_inputs()
outputs = []
n = 0
while True:
    if n + 1 >= len(program):
        break

    opcode = program[n]
    literal_operand = program[n+1]

    # Calculate combo operand
    combo_operand = None
    if 0 <= literal_operand <= 3:
        combo_operand = literal_operand
    elif 4 <= literal_operand <= 6:
        combo_operand = registers[literal_operand - 4]
    else:
        print(f'INVALID OPERAND FOUND: {literal_operand}')

    # Do operation
    if opcode == 0:
        numerator = registers[A]
        denominator = 2**combo_operand
        registers[A] = numerator // denominator

    if opcode == 1:
        registers[B] = registers[B] ^ literal_operand

    if opcode == 2:
        registers[B] = combo_operand % 8

    if opcode == 3:
        if registers[A] == 0:
            pass
        else:
            n = literal_operand
            continue

    if opcode == 4:
        registers[B] = registers[B] ^ registers[C]

    if opcode == 5:
        outputs.append(str(combo_operand % 8))

    if opcode == 6:
        numerator = registers[A]
        denominator = 2**combo_operand
        registers[B] = numerator // denominator

    if opcode == 7:
        numerator = registers[A]
        denominator = 2**combo_operand
        registers[C] = numerator // denominator

    # Increment instruction pointer
    n += 2

print(','.join(outputs))