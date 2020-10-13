"""Demonstrates details of writing Python functions: annotations, default args, kwargs
"""


def demonstrate_annotations(festival, year=1969):
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """


def show_festival(name, year=1969, location='Bethel'):
    """Demonstrates default arguments/parameters.
    - print the function arguments/parameters in one line
    """


def use_flexible_arg_list(prompt: str, *headliners):
    """Demonstrates flexible number of arguments/parameters.
    - print the prompt and the list of festival headliners in one line
    """


def use_all_categories_of_args(prompt, *headliners, year=1969, **location_details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """


if __name__ == "__main__":
    pass


