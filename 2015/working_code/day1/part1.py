INCREMENT = '('
DECREMENT = ')'

total = 0
with open('input.txt', 'r') as input_file:
    line = input_file.readlines()[0].strip()
    for character in line:
        if character == INCREMENT:
            total += 1
        if character == DECREMENT:
            total -= 1

print(total)
