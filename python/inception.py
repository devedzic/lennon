"""The very first module in a more structured version of the project.
"""


# Moving code from main.py
def show_birth_year():
    """John Lennon's birth year.
    """

    print('John Lennon\'s birth year')
    # birth_year = input('The year: ')
    birth_year = int(input('The year: '))
    print(type(birth_year))
    # print(f'John Lennon\'s birth year is {birth_year}.')
    # print(f'John Lennon\'s birth year is', birth_year, '.')
    print(f'John Lennon\'s birth year is', str(birth_year) + '.')

    print(__name__)


# Taking care of the module __name__

if __name__ == '__main__':

    # # Printing with ' ' and printing without '\n'
    # print('John Lennon')
    # print('John Lennon' + ' was born in 1940.')
    # print('John Lennon', 'was born in 1940.')
    # print()
    # print('John Lennon', 'was born in 1940.' + '\nHe was the greatest musician ever.')
    # print('John Lennon', 'was born in', str(1940) + '.' + '\nHe was the greatest musician ever.')

    # Printing with classical formatting (%)
    print('John Lennon was born in %d in %s.' % (1940, 'Liverpool'))
    print()

    # Keyboard input
    show_birth_year()
    print()

    # break and continue
    for i in range(5):
        if i == 3:
            # continue
            break
        print(i)
    print()

    # Printing docstrings
    print(__name__)
    print(__file__)
    print(show_birth_year.__doc__)
    print()

    # Printing a list using enumerate()
    theBeatles = ['John', 'Paul', 'George', 'Ringo']
    for i, v in list(enumerate(theBeatles)):
        print(str(i) + ':', v)

    # Importing from Standard Library
    from datetime import date
    date_of_birth = date(1940, 10, 9)
    print(date_of_birth)
    preferred_date_format = '%b %d, %Y'
    print(date_of_birth.strftime(preferred_date_format))
