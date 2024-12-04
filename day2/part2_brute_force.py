def is_safe(numbers):
    directions = {
        'increasing': 0,
        'decreasing': 0,
        'no_change': 0
    }
    for n in range(len(numbers) - 1):
        n1, n2 = numbers[n], numbers[n+1]

        directions[direction(n1, n2)] += 1
        if not is_inside_range(numbers[n], numbers[n+1]):
            return False

    if directions_has_mistakes(directions, len(numbers) - 1):
        return False

    return True

def directions_has_mistakes(directions, N):
    max_count = max(directions.values())

    if max_count == N:
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
    return 'no_change'

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
            continue
        
        # Check with one mistake
        for n in range(len(numbers)):
            if is_safe(numbers[:n] + numbers[n+1:]):
                number_of_safe_reports += 1
                break


    # Print output
    print(number_of_safe_reports)