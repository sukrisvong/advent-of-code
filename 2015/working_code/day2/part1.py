total = 0
with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        length, width, height = [int(character) for character in line.strip().split('x')]
        side1, side2, side3 = length*width, width*height, height*length
        total += 2*side1 + 2*side2 + 2*side3 + min(side1, side2, side3)

print(total)
