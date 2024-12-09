def find_antinodes_of_two_antennas(antenna_1, antenna_2):
    slope_x = antenna_2[1] - antenna_1[1]
    slope_y = antenna_2[0] - antenna_1[0]
    
    antinode_location_1 = (antenna_1[0] - slope_y, antenna_1[1] - slope_x)
    antinode_location_2 = (antenna_2[0] + slope_y, antenna_2[1] + slope_x)
    return [antinode_location_1, antinode_location_2]

def find_antinodes_for_antenna_type(antenna_locations):
    antinode_locations = []
    N = len(antenna_locations)
    for first_antenna_index in range(N-1):
        for second_antenna_index in range(first_antenna_index+1, N):
            antenna_1 = antenna_locations[first_antenna_index]
            antenna_2 = antenna_locations[second_antenna_index]
            print(antenna_1)
            print(antenna_2)
            print(find_antinodes_of_two_antennas(antenna_1, antenna_2))
            print()
            antinode_locations += find_antinodes_of_two_antennas(antenna_1, antenna_2)
    return antinode_locations

def in_map(location, map_height, map_width):
    row_index = location[0]
    column_index = location[1]

    row_index_is_in_map = 0 <= row_index < map_height
    column_index_is_in_map = 0 <= column_index < map_width

    return row_index_is_in_map and column_index_is_in_map

antenna_locations = {}
map_height = 0
map_width = 0
with open('input.txt', 'r') as input_file:
    for line_index, line in enumerate(input_file.readlines()):
        map_height += 1
        map_width = len(line.strip())
        for character_index, character in enumerate(line.strip()):
            if character == '.':
                continue

            antenna_location = (line_index, character_index)
            if character in antenna_locations.keys():
                antenna_locations[character].append(antenna_location)
            else:
                antenna_locations[character] = [antenna_location]

print(antenna_locations)

unique_antinode_locations_in_map = set()
for antinode_locations_by_antenna_type in antenna_locations.values():
    potential_antinode_locations = find_antinodes_for_antenna_type(antinode_locations_by_antenna_type)
    for antinode_location in potential_antinode_locations:
        if in_map(antinode_location, map_height, map_width):
            unique_antinode_locations_in_map.add(antinode_location)

print(len(unique_antinode_locations_in_map))
