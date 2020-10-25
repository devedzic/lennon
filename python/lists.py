"""Demonstrates working with lists.
"""


def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    # - create a non-empty list with different kinds of elements
    john = ['John Lennon', 1940, True]
    print(john)
    print()

    # - accessing/slicing a list
    print(john[:2])
    print(john[-1:])
    print()

    # - comparing 2 lists (== vs. is)
    john_lennon = ['John Lennon', 1940, True]
    print(john == john_lennon)
    print(john is john_lennon)
    print()

    # - concatenating 2 lists (the + operator)
    print(john + ['Liverpool', 'England'])
    print()

    # - looping through a list
    for e in john:
        print(e)
    print()
    print(', '.join(str(e) for e in john))
    print()


def demonstrate_list_methods():
    """Using
    append()
    insert()
    remove()
    pop()
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    To find indices of all occurrences of an element in a list, use enumerate().
    """

    # append()
    john = []
    john.append('John Lennon')
    john.append(1940)
    print(john)
    print()

    # insert()
    john.insert(2, 'Liverpool')
    print(john)
    print()

    # remove()
    john.remove(1940)
    print(john)
    print()

    # pop()
    john.pop()
    print(john)
    print()

    # extend()
    john.extend((1940, 'Liverpool', 1940))
    print(john)
    print()

    # count()
    print(john)
    print(john.count(1940))
    print()

    # index()
    print(john.index(1940))
    print(john.index(1940, 2, 4))
    print()

    # reverse()
    print(john.reverse())
    print(john)
    print(john.reverse())
    print(john)
    print()

    # len()
    print(len(john))
    print()

    # ...
    # Also, "in" and "not in" operators can be used to search lists
    # for the occurrence of a given element.
    print('John Lennon' in john)
    print('John Lennon' not in john)
    print()


def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """

    from array import array
    a = array('i', [3, 56, 67, 2])
    print(a)
    print(type(a))
    print()


def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """

    from random import randint, seed
    l = []
    seed(67)
    for i in range(1000):
        l.append(randint(1, 100))
    print(l[34:45])


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over an array.array()
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    # - list comprehension over an array.array()
    from array import array
    a = array('i', [3, 56, 67, 2])
    l = [i for i in a]
    print(a)
    print(l)
    l = [str(i) for i in a]
    print(l)
    print()

    # - list comprehension over a list of strings
    john = ['John Lennon', 'The Beatles', 'Liverpool']
    print(', '.join(s for s in john))
    print(', '.join(john))
    print()

    songs = ['Imagine a Man', 'There\'s a Place', 'No Expectations', 'Heaven Is A Place On Earth']

    # # Make the list of first words from all these titles - classic for loop
    # fw = []
    # for t in songs:
    #     tw = t.split()
    #     fw.append(tw[0])
    # print(' '.join(fw))
    # print()

    # Make the list of first words from all these titles - list comprehension
    first_words = [words[0] for words in [title.split() for title in songs]]
    first_words_lower = [str(word).lower() for word in first_words[1:]]
    # print(first_words_lower)
    first_words = [first_words[0]] + first_words_lower
    print(' '.join(first_words))
    print()

    # - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    john.extend(['John Lennon', 'John Lennon'])
    print(john)
    all_occurrences = [i for i, j in enumerate(john) if j == 'John Lennon']
    print(all_occurrences)


if __name__ == '__main__':

    # demonstrate_lists()
    # demonstrate_list_methods()
    # demonstrate_arrays()
    # populate_empty_list()
    # duplicate_list()
    demonstrate_list_comprehension()

