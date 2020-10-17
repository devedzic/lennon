"""Demonstrates how operators and expressions work in Python.
"""

from settings import *


# Demonstrate arithmetic operators (function demonstrate_arithmetic_operators())
def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    """
    print(((13 // 3) % 3) - 7)


# Demonstrate relational operators (function demonstrate_relational_operators())
def demonstrate_relational_operators():
    """Working with relational operators.
    """

    # - simple comparisons
    if 12 >= 14:
        print('12 >= 14')
    else:
        print('12 < 14')
    if '':
        print(True)
    else:
        print(False)
    if 0.0:
        print(True)
    else:
        print(False)
    print()

    # - comparing dates (== vs. is)
    from datetime import date
    d1 = date(1940, 10, 9)
    d2 = date.today()
    d1_id = id(d1)
    d2_id = id(d2)
    print('d1:', d1.strftime(PREFERRED_DATE_FORMAT))
    print('d1:', d2.strftime(PREFERRED_DATE_FORMAT))
    print('id(d1):', d1_id)
    print('id(d2):', d2_id)
    print()

    if d1 == d2:
        print('d1 = d2')
    else:
        print('d1 not = d2')
    if d1 < d2:
        print('d1 < d2')
    else:
        print('d1 not < d2')
    if d1 is d2:
        print('d1 is d2')
    else:
        print('d1 is not d2')
    print()

    # - comparing dates (>, <, etc. with dates)
    from datetime import date
    d1 = date(1940, 10, 9)
    d2 = date.today()

    print('d2 > d1:', d2 > d1)
    print('d2 <= d1:', d2 <= d1)
    print()

    # - None in comparisons, type(None)
    print(None)
    print(type(None))
    if not None:
        print('not None is True')
    else:
        print('not None is not True')


# Demonstrate logical operators (function demonstrate_logical_operators())
def demonstrate_logical_operators():
    """Working with logical operators.
    """

    # - logical operations with True, False and None
    print('True and False:', True and False)
    print('True or False:', True or False)
    print('not False:', not False)
    print('True and None:', True and None)
    print('1 and None:', 1 and None)
    print('A string and None:', 'qqq' and None)
    print()

    # - logical operations with dates
    from datetime import date
    d1 = date(1940, 10, 9)
    d2 = date.today()
    print('d1 and d2:', d1 and d2)
    print('d1 or d2:', d1 or d2)
    print('not d2:', not d2)
    print('not (d1 and d2):', not (d1 and d2))
    print()

    # - logical operations with None (incl. None and int, None and date, etc.)
    print('None and True:', None and True)
    print('None or 1:', None or 1)
    print('not None:', not None)

    from datetime import date
    d1 = date(1940, 10, 9)
    d2 = date.today()

    print('None and d2:', None and d2)
    print('None or d2:', None or d2)
    print('not None:', not None)
    print()

    # - None and date vs. None > date
    print(None and d1)
    # print(None > d1)


if __name__ == '__main__':

    # demonstrate_arithmetic_operators()
    # demonstrate_relational_operators()
    demonstrate_logical_operators()
