#!/usr/bin/python3
def safe_print_divsion(a, b):
        c = 0
        try:
           c = a/b
        except(TypeError, ZeroDivisionError):
           c = None
        finally:
           print("{:d}".format(c))
        return c
