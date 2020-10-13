"""Demonstrates pass, returning None, functions as parameters of other functions,
functions as return values of other functions and user-defined decorators
"""


import functools

from woodstock.python import functions


def return_none():
    """Demonstrates returning None and the pass statement.
    """


def pass_function_as_parameter(f, *args, **kwargs):
    """Demonstrates using another function as a parameter. It works because functions are objects.
    The argument/parameter list specified as in this function is a fairly general one -
    it works regardless of the number of *args and **kwargs in the function call (both can be 0).
    If a call to f includes positional arguments, then they are part of the *args argument of this function.
    The same holds for optional *args in the call to f, as well as for the default arguments of f (if any).
    Likewise, if f is called with keyword arguments, they are included in the **kwargs argument of this function.
    In other words, from https://stackoverflow.com/a/3394898/1899061:
    You can use *args and **kwargs along with named arguments too. The explicit arguments get values first
    and then everything else is passed to *args and **kwargs. The named arguments come first in the list. For example:
        def table_things(titlestring, **kwargs)
    """

    # Try something like this in Python Console:
    #     p = *[1,2,3]        # generates an error
    #     p = *[1,2,3],       # generates a tuple
    #     p = 44, *[1,2,3]    # generates another tuple
    #     print(p)
    #     print(*p)


def return_function(full_name, first_name_flag):
    """Demonstrates using a function as the return value from another function.
    In this example, depending on the first_name_flag, return_function() returns one of the following functions:
    - a function that returns a person's first name
    - a function that returns a person's family name
    """


def return_function_with_args(*args):
    """Demonstrates using a function as the return value from another function.
    The returned function has parameters/arguments.
    In this example, depending on len(args), return_function_with_args() returns one of the following functions:
    - a function that returns an empty list
    - a function that returns a tuple of args (or a list or args, or...)
    """


def a_very_simple_decorator(f, *args):
    """Illustrates the essential idea of decorators:
        - take a function (f) as a parameter of a decorator function (decorator)
        - use the parameter function f inside an inner wrapper function (g)
        - return the inner wrapper function g from the decorator function
    Then define f and run f = decorator(f) before calling f.
    Even better, just put @decorator before the definition of f. Each call to f will then actually run decorator(f).
    """

    # Examples (run them in Python Console):

    # def decorator(f):
    #     def g():
    #         return f('Woodstock')
    #     return g
    #
    # def something(x):
    #     return x
    # ...
    # >>> something(4)
    # 4
    # ...
    # >>> something = decorator(something)
    # >>> something
    # <function __main__.decorator.<locals>.g()>
    # >>> something()
    # Woodstock

    # def decorator(f, *args):
    #     def g():
    #         print('Woodstock')
    #         return f(*args)
    #     return g
    #
    # def something(x):
    #     return x
    # ...
    # >>> something(4)
    # 4
    # ...
    # >>> something = decorator(something, 'Woodstock')
    # >>> something
    # <function __main__.decorator.<locals>.g()>
    # >>> something()
    # Woodstock
    # Woodstock


def highlight_performers(f_to_decorate):
    """Demonstrates how to develop a decorator. Uses the decorator-writing pattern:
    import functools
    def decorator(f_to_decorate):
        @functools.wraps(f_to_decorate)			        # preserves func's identity after it's decorated
        def wrapper_decorator(*args, **kwargs):
            # Do something before
            decorated_f = f_to_decorate(*args, **kwargs)
            # Do something after
            return decorated_f
        return wrapper_decorator
    """


# @highlight_performers
def print_festival(name, *performers):
    """Prints the name and the performers of a festival, assuming that both name and *performers are strings.
    The decorator before the function signature (@highlight_performers) illustrates how to apply a decorator.;
    omit it if decorating manually.
    """


if __name__ == '__main__':

    pass
