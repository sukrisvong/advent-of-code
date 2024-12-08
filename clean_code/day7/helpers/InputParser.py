class InputParser:
    def __init__(self, input):
        self.input = input
    
    def parse_input(self):  
        split_input = self.input.split(':')
        total = int(split_input[0])
        numbers = [int(number) for number in split_input[1].strip().split(' ')]
        return total, numbers
