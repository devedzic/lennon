"""Utility functions of the package music
"""

from enum import Enum
from datetime import date


def format_date(a_date):
    """Converts a date from datetime.date() to a string of the form '<month> <day>, <year>'.
    Uses strftime() method of datetime.date class and its pre-defined format codes from
    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    """


def date_py_to_json(a_date):
    """Converts datetime.date objects to JSON.
    """


def date_json_to_py(iso_date):
    """Converts string formatted as 'YYYY-mm-dd' to datetime.date object.
    """


def get_project_dir():
    """Returns the Path object corresponding to the project root directory.
    """


def get_data_dir():
    """Returns the Path object corresponding to the data directory
    (by convention located right under the project root directory).
    """


if __name__ == '__main__':

    pass

    # Demonstrate pathlib.Path
    # - user's home dir: Path.home()
    # - current dir: Path.cwd(), Path('.'), Path()
    # - absolute path: <path>.absolute()
    # - parent dir: <path>.parent
    # - new dir: <newDir> = <path> / '<subdir1>/<subdir2>/.../<subdirN>'
    #            <newDir>.mkdir(parents=True, exist_ok=True)
    # - remove dir: <dir>.rmdir()                                           # requires the <dir> to be empty
    # - project dir: settings.PROJECT_DIR

    # Demonstrate get_project_dir(), get_data_dir()
