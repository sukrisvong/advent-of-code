FREE_SPACE = '.'

# Get input
with open('input.txt', 'r') as input_file:
    line = input_file.readlines()[0].strip()
# print(line)

# Parse input
numbers = []
for character in line:
    numbers.append(int(character))
# print(numbers)

# Decompress
blocks = []
for n in range(len(numbers)):
    if n % 2 == 0:
        block_character = str(n//2)
    if n % 2 == 1:
        block_character = FREE_SPACE

    for _ in range(numbers[n]):
        blocks.append(block_character)
# print(''.join(blocks))

# Move file blocks
insert_pointer_index = 0
remove_pointer_index = len(blocks) - 1
while insert_pointer_index < remove_pointer_index:
    if blocks[insert_pointer_index] != FREE_SPACE:
        insert_pointer_index += 1
        continue

    if blocks[remove_pointer_index] == FREE_SPACE:
        remove_pointer_index -= 1
        continue

    blocks[insert_pointer_index] = blocks[remove_pointer_index]
    blocks[remove_pointer_index] = FREE_SPACE
    insert_pointer_index += 1
    remove_pointer_index -= 1
    # print(''.join(blocks))

# Calculate checksum
checksum = 0
for index, block in enumerate(blocks):
    if block == FREE_SPACE:
        break
    checksum += index * int(block)
    # print(f'{index} * {block}: {checksum}')
print(checksum)
