#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        Final = a / b
    except ZeroDivisionError:
        Final = None
    finally:
        print("Inside result: {}".format(result))
        return Final


