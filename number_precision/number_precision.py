from decimal import Decimal, Context, ROUND_HALF_UP
from functools import reduce


class NP:
    @staticmethod
    def plus(*args, round=None):
        value = sum(map(lambda num: Decimal(str(num)), args))
        return NP.round(value, ndigits=round)


    @staticmethod
    def minus(*args, round=None):
        value = sum(map(lambda num: -Decimal(str(num)), args[1:]), Decimal(str(args[0])))
        return NP.round(value, ndigits=round)

    @staticmethod
    def times(*args, round=None):
        value = reduce(lambda total, num: total * Decimal(str(num)), [Decimal(1), *args])
        return NP.round(value, ndigits=round)


    @staticmethod
    def divide(*args, round=None):
        value = reduce(lambda total, num: total / Decimal(str(num)), [Decimal(str(args[0])), *args[1:]])
        return NP.round(value, ndigits=round)


    @staticmethod
    def round(value, ndigits=None):
        if ndigits is not None:
            value = Context(prec=ndigits, rounding=ROUND_HALF_UP).create_decimal(str(value))
        return float(value)


if __name__ == "__main__":
    results = [
        0.1 + 0.2,
        NP.plus(0.1, 0.2),
        NP.plus(2.3, 2.4),
        NP.minus(1.0, 0.9),
        NP.times(3, 0.3),
        NP.times(0.362, 100),
        NP.divide(1.21, 1.1),
        NP.round(0.105, 2),
    ]

    print(results)