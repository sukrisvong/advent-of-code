from .Equation import Equation
from .numbers_as_base import to_base

class ValueCalculator:
    def __init__(self, target, numbers, base):
        self.target = target
        self.numbers = numbers
        self.base = base

    def calculate(self):
        number_of_operators = len(self.numbers)-1
        for n in range((self.base**number_of_operators)):
            operators = to_base(n, number_of_operators, self.base)
            equation = Equation(self.numbers, operators)
            calculated_total = equation.calculate()
            if calculated_total == self.target:
                return calculated_total
        return 0
