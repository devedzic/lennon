"""Demonstrates peculiarities of if, for, while and other statements
"""


def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings (), but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """


def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """

    for i in range(1, 21, 2):
        print(i, end='  ')
    print()
    print()

    l = [i for i in range(1, 21, 2)]
    for i in l[0:4]:
        print(i, end='  ')
    print()
    print()

    for _ in range(1, 21, 2):
        print('JL', end='  ')
    print()
    print()


if __name__ == '__main__':
    demonstrate_branching()
    demonstrate_loops()
