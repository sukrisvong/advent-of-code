before_rules = {} # Key is before values
after_rules = {} # Key is after values
updates = []

def get_from_dictionary(key, dictionary):
    if key not in dictionary:
        return []

    value = dictionary[key]
    if value is None:
        return []
    return value

def parse_rules(key, value, dictionary):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]

def parse_update(line):
    updates.append([int(page) for page in line.split(',')])

def is_ordered(update):
    for page_index, page in enumerate(update):
        if fails_rules(page, page_index, update):
            return False
    return True

def fails_rules(current_page, page_index, update):
    pages_before = update[:page_index]
    pages_after = update[page_index+1:]

    for rule in get_from_dictionary(current_page,before_rules):
        if rule not in update:
            continue
        if rule in pages_before:
            return True
    
    for rule in get_from_dictionary(current_page,after_rules):
        if rule not in update:
            continue
        if rule in pages_after:
            return True
    
    return False
    


with open('input.txt', 'r') as input_file:
    # Get Input by line
    current_input = "rules"
    for line in input_file.readlines():
        if line == "\n":
            current_input = "updates"
            continue

        if current_input == "rules":
            page_numbers = line.split("|")
            page_0 = int(page_numbers[0])
            page_1 = int(page_numbers[1])

            parse_rules(page_0, page_1, before_rules)
            parse_rules(page_1, page_0, after_rules)

        if current_input == "updates":
            parse_update(line)

total = 0
for update in updates:
    if is_ordered(update):
        total += update[len(update) // 2]

print(total)