#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add
    print("{0} + {1} = {2}".format(a, b, add(a, b)))
    from calculator_1 import sub
    print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    from calculator_1 import mul
    print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    from calculator_1 import div
    print("{0} / {1} = {2}".format(a, b, div(a, b)))
