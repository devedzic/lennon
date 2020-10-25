"""Demonstrates sets
"""


def demonstrate_sets():
    """Creating and using sets.
    - create a set with an attempt to duplicate items
    - demonstrate some of the typical set operators:
        & (intersection)
        | (union)
        - (difference)
        ^ (disjoint)
    """

    the_beatles = {'John', 'Paul', 'George', 'Ringo'}
    print(the_beatles)
    print()

    # Alternatively
    the_beatles = ('John', 'Paul', 'George', 'Ringo')
    # the_beatles = ['John', 'Paul', 'George', 'Ringo']     # this is also OK; any iterable will do
    the_beatles = set(the_beatles)
    print(the_beatles)
    print()

    the_beatles.add('John')
    print(the_beatles)
    the_beatles.remove('John')
    print(the_beatles)
    print()

    the_beatles = {'John', 'Paul'} | {'George', 'Ringo'}
    print(the_beatles)
    the_beatles = the_beatles - {'John', 'George'}
    print(the_beatles)
    print(sorted(the_beatles))
    print("{'John', 'Paul'} | {'George', 'Ringo'}:", {'John', 'Paul'} & {'George', 'Ringo'})
    print("{'John', 'Paul'} ^ {'George', 'Ringo'}:", {'John', 'Paul'} ^ {'George', 'Ringo'})
    print()


if __name__ == '__main__':

    demonstrate_sets()

