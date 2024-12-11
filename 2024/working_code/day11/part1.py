def get_initial_stones():
    ACTUAL_FILE = 'input.txt'
    TEST_FILE = 'input_test.txt'
    with open(ACTUAL_FILE, 'r') as input_file:
        stones = input_file.readlines()[0].strip().split(' ')
    return stones

def blink(stones):
    new_stones = []
    for stone in stones:
        # Rule 1
        if stone == '0':
            new_stones.append('1')
            continue
        
        # Rule 2
        if len(stone) % 2 == 0:
            new_stones.append(str(int(stone[:len(stone)//2])))
            new_stones.append(str(int(stone[len(stone)//2:])))
            continue
        
        # Rule 3
        new_stones.append(str(int(stone) * 2024))
    return new_stones

stones = get_initial_stones()
for n in range(25):
    stones = blink(stones)
print(len(stones))