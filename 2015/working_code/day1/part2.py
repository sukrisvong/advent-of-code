INCREMENT = '('
DECREMENT = ')'
BASEMENT = -1

total = 0
with open('input.txt', 'r') as input_file:
    line = input_file.readlines()[0].strip()
    for index, character in enumerate(line):
        if character == INCREMENT:
            total += 1
        if character == DECREMENT:
            total -= 1
        if total == BASEMENT:
            print(index + 1)
            break
