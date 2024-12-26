KEY = '.....'
LOCK = '#####'

def get_inputs():
    ACTUAL_FILE = "input.txt"
    TEST_FILE = "input_test.txt"
    keys = []
    locks = []
    with open(ACTUAL_FILE, "r") as input_file:
        heights = [0 for _ in range(5)]
        input_type = None
        for line_number, line in enumerate(input_file.readlines()):
            line = line.strip()
            if line_number % 8 == 7:
                continue
            elif line_number % 8 == 0:
                if line == KEY:
                    input_type = KEY
                    heights = [-1 for _ in range(5)]
                if line == LOCK:
                    input_type = LOCK
                    heights = [0 for _ in range(5)]
            else:
                for column_index, character in enumerate(line):
                    if character == '#':
                        heights[column_index] += 1

            if line_number % 8 == 6:
                if input_type == KEY:
                    keys.append(heights)
                if input_type == LOCK:
                    locks.append(heights)


    return keys, locks

def fits(key, lock):
    for key_height, lock_height in zip(key, lock):
        if key_height + lock_height > 5:
            # print(key, lock, "NO FIT")
            return False
    # print(key, lock, "FITS")
    return True

def calculate_total_fits(keys, locks):
    total_fits = 0
    for key in keys:
        for lock in locks:
            if fits(key, lock):
                total_fits += 1

    return total_fits

keys, locks = get_inputs()
total_fits = calculate_total_fits(keys, locks)
print(total_fits)
