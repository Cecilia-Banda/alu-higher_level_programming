#!/usr/bin/python3
def safe_print_division(a, b):


    Result = None
    try:
        Result = a/b
    except ZeroDivisionError:
        Result = None
    finally:
        print("Inside result: {}".format(result))
        return result
