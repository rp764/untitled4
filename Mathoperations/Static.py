class Subtraction:

    @staticmethod
    def difference(minuend, subtraend):
        return minuend - subtraend

class Addition:

    @staticmethod
    def sum(augend, addend=None):
        if isinstance(augend, list):
            return Addition.sumList(augend)
        return augend + addend

    @staticmethod
    def sumList(valueList):
        result = 0
        for value in valueList:
            result = Addition.sum(result, value)

        return result

class Multiplication:
    @staticmethod
    def product(multiplier,multiplicand):
        return multiplier * multiplicand

class Divsion:
    @staticmethod
    def quotient(numerator,denominater):
        return numerator/denominater
class exponentiation:
    @staticmethod
    def power(base,power):
        return base-power
class root:
    @staticmethod
    def root(degree,radicand):
        return degree**radicand
class log:
    @staticmethod
    def logarithm(base,x):
        return log