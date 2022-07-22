#!/usr/bin/python3
def safe_print_division(a, b):
    X = None
    try:
        X = a / b
    except ZeroDivisionError:
        X = None
    finally:
        print("Inside result: {}".format(result))
        return X
