def is_safe(numbers):
    current_direction = direction(numbers[0], numbers[1])
    for n in range(len(numbers) - 1):
        if not is_inside_range(numbers[n], numbers[n+1]):
            return False
        if direction(numbers[n], numbers[n+1]) != current_direction:
            return False
    return True

def is_inside_range(x, y):
    difference = abs(x-y)
    return 1 <= difference <= 3

def direction(number_1, number_2):
    if number_1 < number_2:
        return 'increasing'
    if number_1 > number_2:
        return 'decreasing'
    return 'no change'

# Open File
with open('input.txt', 'r') as input_file:
    # Define output counter
    number_of_safe_reports = 0

    # Get Input by line
    for line in input_file.readlines():
        # Parse into ints
        numbers_as_strings = line.split(' ')
        numbers = [int(number_as_string) for number_as_string in numbers_as_strings]

        # Increment if safe
        if is_safe(numbers):
            number_of_safe_reports += 1

    # Print output
    print(number_of_safe_reports)