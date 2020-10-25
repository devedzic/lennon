"""Demonstrates tuples
"""


def demonstrate_tuples():
    """Creating and using tuples.
    - create and print 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    empty_tuple = ()
    print(empty_tuple)
    one_tuple = ('John Lennon', )
    print(one_tuple)
    two_tuple = ('John Lennon', 1940)
    print(two_tuple)
    n_tuple = ('John Lennon', 1940, True)
    print(n_tuple)
    print(type(n_tuple))
    print(n_tuple[0])
    # n_tuple[0] = 1              # no; tuples are immutable
    print()

    print()


def demonstrate_zip():
    """Using the built-in zip() function with tuples and double-counter for-loop.
    """

    john = ('John Lennon', 1940, 'Liverpool')
    paul = ('Paul McCartney', 1942, 'Liverpool')
    george = ('George Harrison', 1944, 'Liverpool')
    ringo = ('Ringo Starr', 1940, 'Liverpool')
    the_beatles_zip = zip(john, paul, george, ringo)
    print(the_beatles_zip)
    for i, j, k, l in the_beatles_zip:
        print(str(i) + ';', str(j) + ';', str(k) + ';', str(l) + ';', )

    the_beatles_zip = zip(john, paul, george, ringo)                    # it is essential to re-create the zip object;
    for i in the_beatles_zip:                                           # otherwise, this second loop prints nothing,
        print(i)                                                        # (zip iterator exhausted in the first loop)


def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    name = 'John Lennon'
    year = 1940
    city = 'Liverpool'
    john = name, year, city
    print(john)
    print()
    n, y, c = john
    print(n, y, c)


if __name__ == '__main__':

    # demonstrate_tuples()
    # demonstrate_zip()
    demonstrate_packing()
