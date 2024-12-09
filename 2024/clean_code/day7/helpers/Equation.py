class Equation:
    MULTIPLY = '0'
    ADD = '1'
    CONCATENATE = '2'

    def __init__(self, numbers, operators):
        self.numbers = numbers
        self.operators = operators

    def calculate(self):
        running_total = self.numbers[0]
        for n in range(len(self.operators)):
            operator, number = self.operators[n], self.numbers[n+1]
            if operator == self.MULTIPLY:
                running_total *= number
            if operator == self.ADD:
                running_total += number
            if operator == self.CONCATENATE:
                running_total = int(str(running_total) + str(number))
        return running_total
