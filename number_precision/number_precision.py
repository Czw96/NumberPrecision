from decimal import Decimal
import functools


class NP:
    @staticmethod
    def plus(*numbers, round: int = None, number_type=float):
        assert len(numbers) > 0

        numbers = [Decimal(str(number)) for number in numbers]
        return number_type(NP.round(sum(numbers), ndigits=round))

    @staticmethod
    def minus(*numbers, round: int = None, number_type=float):
        assert len(numbers) > 0

        numbers = [-Decimal(str(number)) for number in numbers]
        numbers[0] = -numbers[0]
        return number_type(NP.round(sum(numbers), ndigits=round))

    @staticmethod
    def times(*numbers, round: int = None, number_type=float):
        assert len(numbers) > 0

        numbers = [Decimal(str(number)) for number in numbers]
        value = functools.reduce(lambda total, number: total * number, numbers)
        return number_type(NP.round(value, ndigits=round))

    @staticmethod
    def divide(*numbers, round: int = None, number_type=float):
        assert len(numbers) > 0

        numbers = [Decimal(str(number)) for number in numbers]
        if Decimal('0') in numbers:
            return number_type(0)

        value = functools.reduce(lambda total, number: total / number, numbers)
        return number_type(NP.round(value, ndigits=round))

    @staticmethod
    def round(value: Decimal, ndigits: int = None):
        assert ndigits is None or ndigits >= 0
        return value if ndigits is None else value.quantize(Decimal('0.' + '0' * ndigits))
