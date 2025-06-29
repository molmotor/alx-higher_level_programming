#!/usr/bin/python3
def safe_print_division(a, b):
        c = 0
        try:
           c = a/b
        except(TypeError, ZeroDivisionError):
           c = None
        finally:
           print("{:.2f}".format(c) if c is not none else "None")
        return c
