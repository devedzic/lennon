"""Demonstrates dictionaries
From: https://qr.ae/TWCAvj:
Python uses dictionaries all over the place:
- the variables and functions in a module - stored in a dictionary  # can be shown using globals()
- the local variables in a function - stored in a dictionary        # can be shown using locals(); see functions.py
- the implementation of a function - a dictionary
- a class is a dictionary
- an instance of a class is another dictionary
- the modules your program has imported - you guessed it - another dictionary
- even Python set objects are implemented as modified dictionaries
To paraphrase Tim Peter's 'Zen of Python': "dictionaries are great - let's do more of them".
Read more at https://qr.ae/TWCAvj.
"""


def demonstrate_dictionaries():
    """Creating and using dictionaries.
    - create a blank (empty) dictionary
    - create a non-empty dictionary
    - print a non-empty dictionary
        - print all items using the items() function
        - print one item per line
    - pprint dictionary in one column
    - add/remove items to/from a dictionary
    - update a dictionary with the items from another dictionary or from an iterable of (k, v) pairs using dict.update()
    - using the keys() and values() functions
    """

    # - create a blank (empty) dictionary
    john = {}
    print(john)
    print(type(john))
    print()

    # - create a non-empty dictionary
    john = {'name': 'John Lennon', 'birth_year': 1940, 'alive': False}
    print(john)
    print(john['name'])
    print()

    # - print a non-empty dictionary
    #     - print all items using the items() function
    #     - print one item per line
    print(list(john.items()))
    for i, j in (list(john.items())):
        print(i + ':', j)
    print()

    # - pprint dictionary in one column
    from pprint import pprint
    pprint(john, width=1)
    print()

    # - add/remove items to/from a dictionary
    john['birth_place'] = 'Liverpool'
    print(john)

    # - update a dictionary with the items from another dictionary
    # or from an iterable of (k, v) pairs using dict.update()
    citizenship = {'original': 'UK', 'latest': 'USA'}
    john.update(citizenship)
    print(john)
    citizenship_list = [('original', 'British'), ('latest', 'American')]
    john.update(citizenship_list)
    print(john)

    # - using the keys() and values() functions
    print(john.keys())
    print(john.values())
    print(list(john.keys()))
    print(list(john.values()))
    print([(i, j) for i, j in zip(john.keys(), john.values())])
    print()


def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    - using zip()
    - using operator.itemgetter()
    - using lambda
    """

    # # - using zip()
    # if by == 'k':
    #     return dict(sorted(zip(d.keys(), d.values())))
    # elif (by == 'v') or (by == 'V'):
    #     return dict(sorted(zip(d.values(), d.keys())))
    # else:
    #     return None

    # - using operator.itemgetter()
    # from operator import itemgetter
    # if by == 'k':
    #     return dict(sorted(d.items(), key=itemgetter(0)))
    # elif (by == 'v') or (by == 'V'):
    #     return dict(sorted(d.items(), key=itemgetter(1)))
    # else:
    #     return None

    # - using lambda
    from operator import itemgetter
    if by == 'k':
        return dict(sorted(d.items(), key=lambda item: item[0]))
    elif (by == 'v') or (by == 'V'):
        return dict(sorted(d.items(), key=lambda item: item[1]))
    else:
        return None


def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """
    john = {'name': 'John Lennon', 'birth_year': 1940, 'alive': False}
    print(sort_dictionary(john, 'k'))
    # print(sort_dictionary(john, 'V'))     # TypeError: '<' not supported between instances of 'int' and 'str'
    print(sort_dictionary(john, 23))


if __name__ == '__main__':
    # demonstrate_dictionaries()
    demonstrate_dict_sorting()

    # print(globals())
    # print(demonstrate_dict_sorting.__globals__)
