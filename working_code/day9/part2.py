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

# Get free space indices
free_space_locations = []
free_space_start_index = 0
free_space_end_index = 0
for n in range(len(blocks) - 1):
    # print(f'n: {n}, {blocks[n]}')
    if blocks[n] == blocks[n+1]:
        continue

    if blocks[n+1] == FREE_SPACE:
        free_space_start_index = n+1
    elif blocks[n] == FREE_SPACE:
        # print(f'APPENDING: {(free_space_start_index, free_space_end_index)}')
        free_space_end_index = n+1
        free_space_locations.append((free_space_start_index, free_space_end_index))
# print(free_space_locations)

# Move file blocks by whole files
insert_pointer_index_start = 0
remove_pointer_index_end = len(blocks) - 1
while insert_pointer_index_start < remove_pointer_index_end:
    if blocks[insert_pointer_index_start] != FREE_SPACE:
        insert_pointer_index_start += 1
        continue

    if blocks[remove_pointer_index_end] == FREE_SPACE:
        remove_pointer_index_end -= 1
        continue

    # print(f'Potential move found: {insert_pointer_index_start} <-- {remove_pointer_index_end}')

    # Get width and location of file to remove
    remove_pointer_index_start = remove_pointer_index_end
    block_to_remove = blocks[remove_pointer_index_end]
    while blocks[remove_pointer_index_start] == block_to_remove:
        remove_pointer_index_start -= 1
    file_to_remove_width = remove_pointer_index_end - remove_pointer_index_start
    remove_pointer_index_start += 1

    # Find space for file
    for free_space_location_index, free_space_location in enumerate(free_space_locations):
        free_space_start_index, free_space_end_index = free_space_location
        free_space_width = free_space_end_index - free_space_start_index
        
        if free_space_end_index > remove_pointer_index_start:
            # print(f'No move for {block_to_remove}')
            break
        if free_space_width < file_to_remove_width:
            continue

        # print(f'Move found: ({free_space_start_index},{free_space_start_index + file_to_remove_width}) <-- ({remove_pointer_index_start},{remove_pointer_index_end})')

        # print(free_space_locations)
        # Move file to found space
        for n in range(free_space_start_index, free_space_start_index + file_to_remove_width):
            blocks[n] = block_to_remove
        for n in range(remove_pointer_index_start, remove_pointer_index_end + 1):
            blocks[n] = FREE_SPACE
        if free_space_width == file_to_remove_width:
            free_space_locations.pop(free_space_location_index)
        else:
            new_location = (free_space_start_index + file_to_remove_width, free_space_end_index)
            free_space_locations[free_space_location_index] = new_location
        break

    insert_pointer_index_start = 0
    remove_pointer_index_end -= file_to_remove_width
    # print(''.join(blocks))

# print(blocks)

# Calculate checksum
checksum = 0
for index, block in enumerate(blocks):
    if block == FREE_SPACE:
        continue
    checksum += index * int(block)
    # print(f'{index} * {block}: {checksum}')
print(checksum)
