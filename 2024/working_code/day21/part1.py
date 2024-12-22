''' 
NOTES
-------------
For a pressing the directional pad, this is the value of each button press from A:
A --> A           --> 1
^ --> <A          --> 2 --> 8
> --> vA          --> 2 --> 
v --> <vA | v<A   --> 3
< --> v<<A | <v<A --> 4

-----------------
LEFT/UP
LEFT/DOWN
RIGHT/UP
RIGHT/DOWN


'''


ACCEPT = "A"
UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

NUMERIC = 'numeric'
DIRECTIONAL = 'directional'

NUMERIC_KEYPAD = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '0': (3, 1),
    ACCEPT: (3, 2),
}
DIRECTIONAL_KEYPAD = {
    UP: (0, 1),
    ACCEPT: (0, 2),
    LEFT: (1, 0),
    DOWN: (1, 1),
    RIGHT: (1, 2),
}

def get_codes():
    ACTUAL_FILE = "input.txt"
    TEST_FILE = "input_test.txt"
    codes = []
    with open(ACTUAL_FILE, "r") as input_file:
        for line in input_file.readlines():
            codes.append(line.strip())

    return codes

def keypresses_up(n):
    keypresses = ''
    for _ in range(abs(n)):
        keypresses += UP
    return keypresses
def keypresses_down(n):
    keypresses = ''
    for _ in range(abs(n)):
        keypresses += DOWN
    return keypresses
def keypresses_left(n):
    keypresses = ''
    for _ in range(abs(n)):
        keypresses += LEFT
    return keypresses
def keypresses_right(n):
    keypresses = ''
    for _ in range(abs(n)):
        keypresses += RIGHT
    return keypresses

def keypresses_up_or_down(n):
    if n < 0:
        return keypresses_up(n)
    return keypresses_down(n)
def keypresses_left_or_right(n):
    if n < 0:
        return keypresses_left(n)
    return keypresses_right(n)

def will_hit_blank_space_numeric(movement, current_location):
    if current_location[0] == 3 and current_location[1] + movement[1] == 0:
        return True
    if current_location[1] == 0 and current_location[0] + movement[0] == 3:
        return True
    return False

def will_hit_blank_space_directional(movement, current_location):
    if current_location[0] == 0 and current_location[1] + movement[1] == 0:
        return True
    if current_location[1] == 0 and current_location[0] + movement[0] == 0:
        return True
    return False

def get_keypresses_numeric(movement, current_location):
    keypresses = ''
    if will_hit_blank_space_numeric(movement, current_location):
        if movement[0] < 0:
            keypresses += keypresses_up(movement[0])
            keypresses += keypresses_left_or_right(movement[1])
        else:
            keypresses += keypresses_left_or_right(movement[1])
            keypresses += keypresses_down(movement[0])
    else:
        if movement[0] < 0 and movement[1] < 0:
            keypresses += keypresses_left(movement[1])
            keypresses += keypresses_up(movement[0])
        elif movement[0] < 0 and movement[1] > 0:
            # This can vary
            keypresses += keypresses_right(movement[1])
            keypresses += keypresses_up(movement[0])
        elif movement[0] > 0 and movement[1] < 0:
            # This can vary
            keypresses += keypresses_left(movement[1])
            keypresses += keypresses_down(movement[0])
        elif movement[0] > 0 and movement[1] > 0:
            # This can vary
            keypresses += keypresses_down(movement[0])
            keypresses += keypresses_right(movement[1])
        else:
            # This can vary
            keypresses += keypresses_left_or_right(movement[1])
            keypresses += keypresses_up_or_down(movement[0])
    return keypresses
def get_keypresses_directional(movement, current_location):
    keypresses = ''
    if will_hit_blank_space_directional(movement, current_location):
        if movement[0] < 0:
            keypresses += keypresses_left_or_right(movement[1])
            keypresses += keypresses_up(movement[0])
        else:
            keypresses += keypresses_down(movement[0])
            keypresses += keypresses_left_or_right(movement[1])
    else:
        if movement[0] < 0 and movement[1] < 0:
            keypresses += keypresses_up(movement[0])
            keypresses += keypresses_left(movement[1])
        elif movement[0] < 0 and movement[1] > 0:
            keypresses += keypresses_up(movement[0])
            keypresses += keypresses_right(movement[1])
        elif movement[0] > 0 and movement[1] < 0:
            keypresses += keypresses_left(movement[1])
            keypresses += keypresses_down(movement[0])
        elif movement[0] > 0 and movement[1] > 0:
            keypresses += keypresses_down(movement[0])
            keypresses += keypresses_right(movement[1])
        else:
            keypresses += keypresses_left_or_right(movement[1])
            keypresses += keypresses_up_or_down(movement[0])
    return keypresses

def get_keypresses(current_location, next_location, keypad_type):
    keypresses = ''
    movement = (next_location[0] - current_location[0], next_location[1] - current_location[1])
    if keypad_type == NUMERIC:
        keypresses = get_keypresses_numeric(movement, current_location)
    if keypad_type == DIRECTIONAL:
        keypresses = get_keypresses_directional(movement, current_location)
    return keypresses + ACCEPT

def get_keypresses_for_code(code):
    current_location = NUMERIC_KEYPAD[ACCEPT]
    keypresses = ''
    for digit in code:
        next_location = NUMERIC_KEYPAD[digit]
        keypresses += get_keypresses(current_location, next_location, NUMERIC)
        current_location = next_location
    return keypresses

def get_directional_keypresses_for_numeric_keypresses(code):
    current_location = DIRECTIONAL_KEYPAD[ACCEPT]
    keypresses = ''
    movement_to_a = [0, 0]
    for digit in code:
        # print(f'pressing {digit}')
        if digit == ACCEPT:
            # LOGIC FOR GOING BACK TO A
            numeric_current_location = (NUMERIC_KEYPAD[ACCEPT][0] + movement_to_a[0], NUMERIC_KEYPAD[ACCEPT][1] + movement_to_a[1])
            next_keypresses = get_keypresses(numeric_current_location, NUMERIC_KEYPAD[ACCEPT], NUMERIC)
            keypresses += next_keypresses
            current_location = DIRECTIONAL_KEYPAD[ACCEPT]
            movement_to_a = [0, 0]
        else:
            next_location = DIRECTIONAL_KEYPAD[digit]
            next_keypresses = get_keypresses(current_location, next_location, DIRECTIONAL)
            keypresses += next_keypresses
            for keypress in next_keypresses:
                if keypress == UP:
                    movement_to_a[0] -= 1
                if keypress == DOWN:
                    movement_to_a[0] += 1
                if keypress == LEFT:
                    movement_to_a[1] -= 1
                if keypress == RIGHT:
                    movement_to_a[1] += 1
            # print(keypresses)
            # print(movement_to_a)
            current_location = next_location
        # print(next_keypresses)
        # print()

    return keypresses

def get_directional_keypresses_for_directional_keypresses(code):
    current_location = DIRECTIONAL_KEYPAD[ACCEPT]
    keypresses = ''
    for digit in code:
        # print(f'pressing {digit}')
        next_location = DIRECTIONAL_KEYPAD[digit]
        next_keypresses = get_keypresses(current_location, next_location, DIRECTIONAL)
        keypresses += next_keypresses
        current_location = next_location
        # print(next_keypresses)
        # print()

    return keypresses

def parse_numeric_part_of_code(code):
    pass

codes = get_codes()
print(codes)
total_complexity = 0
for code in codes:
    numeric_keypresses = get_keypresses_for_code(code)
    # print(numeric_keypresses)
    directional_keypresses_1 = get_directional_keypresses_for_numeric_keypresses(numeric_keypresses)
    # print(directional_keypresses_1)
    directional_keypresses_2 = get_directional_keypresses_for_directional_keypresses(directional_keypresses_1)
    # print(directional_keypresses_2)
    sequence_length = len(directional_keypresses_2)
    # print(sequence_length)
    numeric_code = int(code[:3])
    complexity = sequence_length * numeric_code
    total_complexity += complexity
print(total_complexity)

'''
for direction in ['>^','^>','>v','v>','<^','^<','<v','v<']:
    step_1 = get_directional_keypresses_for_directional_keypresses(direction)
    step_2 = get_directional_keypresses_for_directional_keypresses(step_1)
    step_3 = get_directional_keypresses_for_directional_keypresses(step_2)
    print(f'{direction}: {len(step_3)}')
'''
'''
numeric_keypresses = get_keypresses_for_code('379A')
print(numeric_keypresses)
directional_keypresses_1 = get_directional_keypresses_for_numeric_keypresses(numeric_keypresses)
print(directional_keypresses_1)
directional_keypresses_2 = get_directional_keypresses_for_directional_keypresses(directional_keypresses_1)
print(directional_keypresses_2)
print(len(directional_keypresses_2))
'''

