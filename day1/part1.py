# Get Input
list_1, list_2 = [], []
with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        numbers_as_strings = line.split('   ')
        list_1.append(int(numbers_as_strings[0]))
        list_2.append(int(numbers_as_strings[1]))

# Sort both lists
list_1.sort()
list_2.sort()

# Sum differences
total = 0
for item_1, item_2 in zip(list_1, list_2):
    total += abs(item_1 - item_2)

print(total)