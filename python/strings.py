"""Demonstrates working with strings in Python.
"""

import string

import settings


def demonstrate_formatting():
    """Using classical formatting.
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    # - using classical formatting
    print('%5.3f, %s, %4d' % (23.4, 'John', 34))

    # - \n is the new line char
    print('D:\nobody')

    # - r'...' - raw formatting
    print(r'D:\nobody ')

    # - using \"\"\"...\"\"\" for multi-line formatting
    print("""The Beatles:
    John
    Paul
    ...""")

    # - string "multiplication"
    print('John Lennon    ' * 3)

    # - substrings / slicing
    print('John Lennon'[0:4])
    print('John Lennon'[5:])
    print('John Lennon'[-3:])
    print('John Lennon'[5:8])
    print('John Lennon'[:])
    print()

    # - str() vs. repr() (usually the same, but with whitespace there is a difference)
    print(str(1))
    print(repr(1))
    print(string.whitespace)
    print(str(string.whitespace))
    print(repr(string.whitespace))


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('{} was born in {}, in {}.'.format('John Lennon', 1940, 'Liverpool'))


def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    from datetime import date
    john = 'John Lennon'
    birth_date = date(1940, 10, 9)
    birth_place = 'Liverpool'
    print(f'{john}\'s date of birth is {birth_date}; he was born in {birth_place}.')
    print(f'{john}\'s date of birth is {birth_date.strftime(settings.PREFERRED_DATE_FORMAT)}; he was born in {birth_place}.')


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals(), len(),...), strip() (lstrip(), rstrip())
    """

    john = 'John Lennon'
    print(john.endswith('Lennon'))
    print(john.split())
    print(john.center(30, '+'))
    print('Len' in john)
    print(john == 'John Lennon')
    print(len(john))
    john = '   ' + john + '   '
    print(john, end='')
    print('here')
    print(john.strip(), 'here')


if __name__ == '__main__':

    # demonstrate_formatting()
    # demonstrate_fancy_formatting()
    # demonstrate_fancy_formatting_with_f_strings()
    demonstrate_string_operations()
