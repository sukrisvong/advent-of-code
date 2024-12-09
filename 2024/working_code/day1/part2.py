# Get Input
dict_1, dict_2 = {}, {}
with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        numbers_as_strings = line.split('   ')
        number_1, number_2 = int(numbers_as_strings[0]), int(numbers_as_strings[1])
        dict_1[number_1] = dict_1[number_1] + 1 if number_1 in dict_1 else 1
        dict_2[number_2] = dict_2[number_2] + 1 if number_2 in dict_2 else 1

# Sum products
total = 0
for key in dict_1.keys():
    if key not in dict_2:
        continue 

    total += key * dict_2[key]

print(total)