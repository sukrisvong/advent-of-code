A = 0
B = 1
C = 2

def get_inputs():
    ACTUAL_FILE = 'input.txt'
    TEST_FILE = 'input_test.txt'
    registers = []
    program = None
    with open(ACTUAL_FILE, 'r') as input_file:
        for row_index, line in enumerate(input_file.readlines()):
            if row_index < 3:
                registers.append(int(line.strip().split(' ')[-1]))
            if row_index > 3:
                program = [int(n) for n in line.strip().split(' ')[-1].split(',')]

    return registers, program

def calculate_output(registers, program):
    outputs = []
    output_index = 0
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

        # Divides A by some power of 2.
        # Floor division is the same as bit shifting by the power!
        # 15 // 2^1 = 7 --> 000111|1 --> 000111
        # 15 // 2^2 = 3 --> 00011|11 --> 00011
        # 29 // 2^3 = 3 --> 0011|101 --> 0011
        # 99 // 2^4 = 6 --> 110|0011 --> 110
        if opcode == 0:
            numerator = registers[A]
            denominator = 2**combo_operand
            registers[A] = numerator // denominator

        if opcode == 1:
            registers[B] = registers[B] ^ literal_operand

        if opcode == 2:
            registers[B] = combo_operand % 8

        # This allows us to jump to another location in the program
        # Based on the program, the possible indices to jump are [0,5,7]
        if opcode == 3:
            if registers[A] == 0:
                pass
            else:
                n = literal_operand
                continue

        if opcode == 4:
            registers[B] = registers[B] ^ registers[C]

        # This is the ONLY thing that outputs.
        # The output will always be from 0-7, because of mod 8
        # Based on the program, the possible literal operands are [3, 4, 5]
        # The possible combo operands are then 3, register A, register B
        if opcode == 5:
            outputs.append(combo_operand % 8)
            # if outputs[output_index] != program[output_index]:
            #     return False

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
    
    return outputs

registers, program = get_inputs()
'''
n = 0
while True:
    if n % 100000 == 0:
        print(f'Testing {n}')
    if calculate_output([n,0,0], program):
        break
    n += 1

print(f'Found answer!!!!!!!! The answer is: {n}')
'''

# 1 0,0 -> 1,1  |  0,3 -> 1,7
# 2 0,0 -> 2,3  |  0,3 -> 2,7
# 3 0,0 -> 3,0  |  0,3 -> 3,0
# 4 0,0 -> 4,4  |  0,3 -> 4,4
# 5 0,0 -> 5,5  |  0,3 -> 5,5
# 6 0,0 -> 6,6  |  0,3 -> 6,6
# 7 0,0 -> 7,7  |  0,3 -> 7,6

# N |15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0
#   | 3, 0, 4, 5, 1, 3, 0, 1, 0, 4, 5, 2, 2, 4, 0, X
#   |                                  6, 2, X
#   |                               7, 0, 2
#   |                                     7
#   |                                  1, 1, 0, 5
#   |                                           6
#   |                                     7
#   |                                  2, 2, 4, 0
#   |                                  6, 2
#   |                            5, 0
#   |                            6, 1, 7
#   |                      4, 1
#   |                5, 1, 0, 1
#   |       7, 5, 5, 3, 0, 1
#   |                      4, 1
#   |                5, 1, 0, 1
#   |             7, 3, 0, 1, 0, 4, 5
#   |                            5
#   |                            6
#   |                      4
#   |                   4  6  5
#   |                         7  7
#   |                      7  5
#   |                5
#   |                7  4  1  5  4  6  6  2  X
#   |                                     5  X
#   |                                     6  X
#   |                            5  0  X
#   |                               6  X
c = [ 3, 0, 4, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#    15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0
# TODO: AUTOMATE THIS
c.reverse()
N = 11
for m in range(8):
    initial_a = 0
    for n in range(len(c)):
        if n == N:
            initial_a += m*8**N
        else:
            initial_a += c[n]*8**n
    outputs = calculate_output([initial_a,0,0], program)
    # print(program)
    # print(outputs)
    print(f'{m}: {program[N] == outputs[N]}')
# print(program[N], outputs[N])
# calculate_output([3*8**15 + 4*8**13 + 4*8**12 + 4*8**11,0,0], program)

def calculate_initial_a(coefficients, potential_coefficient, coefficient_index):
    initial_a = 0
    for n in range(len(coefficients)):
        if n == coefficient_index:
            initial_a += potential_coefficient * 8 **n
        else:
            if coefficients[n] == []:
                continue
            initial_a += coefficients[n][0] * 8**n
    return initial_a

coefficients = [[] for _ in range(len(program))]
coefficients[15] = [3]
coefficient_index = 14
loop_count = 0
backtrack = False
while True:
    # print(coefficients)
    # input()
    if backtrack:
        if len(coefficients[coefficient_index]) <= 1:
            coefficients[coefficient_index] = []
            coefficient_index += 1
            continue
        else:
            coefficients[coefficient_index].pop(0)
            backtrack = False

    if len(coefficients[coefficient_index]) >= 1:
        coefficient_index -= 1
        continue

    if coefficient_index < 0:
        print("End of program")
        break

    # Find next potential coefficient
    for potential_coefficient in range(8):
        potential_initial_a = calculate_initial_a(coefficients, potential_coefficient, coefficient_index)
        outputs = calculate_output([potential_initial_a, 0,0], program)
        if outputs == program:
            print("ANSWER FOUND")
            print(potential_initial_a)
            break
        if program[coefficient_index] == outputs[coefficient_index]:
            coefficients[coefficient_index].append(potential_coefficient)

    if coefficients[coefficient_index] == []:
        backtrack = True
    else:
        coefficient_index -= 1
        
        
        

'''
initial_a_coefficients = [1, 2, 4, 2, 2, 5, 4, 0, 1, 0, 3, 1, 5, 4, 0, 3]
initial_a = 0
for n,c in enumerate(initial_a_coefficients):
        initial_a += c * 8**n
print(initial_a)
while True:
    outputs = calculate_output([initial_a,0,0], program)
    print(outputs)
    print(program)
    print()
    break
    initial_a += 1
    if outputs == program:
        break
'''