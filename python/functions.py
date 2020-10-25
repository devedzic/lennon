"""Demonstrates details of writing Python functions: annotations, default args, kwargs
"""


# def demonstrate_annotations(musician, year):
def demonstrate_annotations(musician: str, year: int = 1940) -> str:
    """
    :param musician: musician's name
    :param year: musician's year of birth
    :return: formatted string representation of the musician
    """

    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the name and the docstring of this function
    - print the value of the __annotations__ attribute of this function
    - return a formatted string (including function parameters/arguments)
    """

    print(f'musician: {musician}, born: {year}')
    print(locals())
    print(demonstrate_annotations.__name__, demonstrate_annotations.__doc__)
    print(demonstrate_annotations.__annotations__)

    return f'{musician} (born: {year})'


def show_musician(name, year=1940, city='Liverpool'):
    """Demonstrates default arguments/parameters.
    - print the function arguments/parameters in one line
    """

    print(locals())
    print(f'name: {name}, year: {year}, city: {city}')


def use_flexible_arg_list(band_name: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the band name and the list of band members in one line
    """

    # members = list(members)                                       # not necessary, although improves readability
    print(type(members))
    print(members)

    print(f'{band_name} ({", ".join(members)})' if members else f'{band_name}')


def use_all_categories_of_args(band_name, *members, year=1962, **music_details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """

    print(type(music_details))
    print(music_details)

    music_details = [str(k) + ': ' + str(v) for k, v in music_details.items()]
    # print(music_details)
    print(f'{band_name} ({", ".join(members)})' if members else f'{band_name}', end='')
    print('\n\t' + '\n\t'.join(music_details) if music_details else '')


if __name__ == "__main__":

    john = 'John Lennon'
    paul = 'Paul McCartney'
    george = 'George Harrison'
    ringo = 'Ringo Starr'
    the_beatles = [john, paul, george, ringo]

    # demonstrate_annotations(john)
    # demonstrate_annotations(musician, year=1957)

    # show_musician(john)

    # use_flexible_arg_list('The Beatles', *the_beatles)
    # use_flexible_arg_list('The Beatles')

    # use_all_categories_of_args('The Beatles', start=1962, end=1970)
    # use_all_categories_of_args('The Beatles', *the_beatles, start=1962, end=1970)

