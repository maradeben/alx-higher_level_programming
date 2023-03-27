#!/usr/bin/python3

def safe_print_division(a, b):
    """
    print result of division, where a and b are integers
    result of the division should be printed on the 'finally' section
    preceded by Inside result:
    Returns value of the division, otherwise None
    """
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print(f"Inside result: {result}")

    return (result)
