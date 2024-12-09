def is_safe(numbers, base_case=False):
    directions = {
        'increasing': 0,
        'decreasing': 0,
        'no_change': 0
    }
    mistake_indices = set()

    for n in range(len(numbers) - 1):
        n1, n2 = numbers[n], numbers[n+1]

        directions[direction(n1, n2)] += 1
        if not is_inside_range(numbers[n], numbers[n+1]):
            mistake_indices.add(n)
    print(numbers)
    print(mistake_indices)
    print(mistake_indices_for_directions(directions, numbers))
    print()
    mistake_indices = mistake_indices.union(mistake_indices_for_directions(directions, numbers))

    if len(mistake_indices) == 0:
        return True

    if len(mistake_indices) > 1:
        return False

    if not base_case:
        mistake_index = list(mistake_indices)[0]
        numbers_without_index = numbers[:mistake_index+1] + numbers[mistake_index+2:]
        return is_safe(numbers_without_index, True)

    return False

def mistake_indices_for_directions(directions, numbers):
    N = len(numbers) - 1
    max_count = max(directions.values())
    for key, value in directions.items():
        if value == max_count:
            max_direction = key

    # No mistakes
    if max_count == N:
        return set()
    
    # Failing condition, return value with 2 or more indices will cause
    # the logic in the parent function to return unsafe. Negative indices
    # cannot exist, so this guarantees the report will be marked unsafe.
    if max_count <= N - 2:
        return {-1, -2}
    
    # Get index of the actual failure
    mistake_direction = None
    for key, value in directions.items():
        if value == 1:
            mistake_direction = key

    for n in range(N):
        n1, n2 = numbers[n], numbers[n+1]

        if mistake_direction == direction(n1, n2):
            return {n}
    

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

    # Print output
    print(number_of_safe_reports)