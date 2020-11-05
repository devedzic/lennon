"""The class representing the concept of a music group/band.
It includes a list of Musician objects (band members) and the date when the band started performing together.
"""

from datetime import date, datetime, time
import json

# from music.musician import Musician
# from util.utility import format_date


class Band():
    """The class describing the concept of a music group/band.
    It includes a list of Musician objects (band members) and the date when the band started performing together.
    """

    # Class variables: like static fields in Java; typically defined and initialized before __init__()
    # Insert a class variable (static field), such as definition, date_pattern,...

    def __init__(self, *members, start=date.today()):
        pass                                            # introduce and initialize iterator counter, self.__i

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    # Alternative constructor 1
    @classmethod
    def from_name_list(cls, names, start=date.today()):
        pass

    # Alternative constructor 2
    @classmethod
    def from_band_str(cls, band_str):
        pass

    @staticmethod
    def is_date_valid(d):
        """It is assumed that a band does not perform together since more than ~60 years ago.
        So, the valid date to denote the start of a band's career is between Jan 01, 1960, and today."""

        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


def next_member(lineup):
    """Generator that shows members of a band, one at a time.
    """


class BandEncoder(json.JSONEncoder):
    """JSON encoder for Band objects.
    """

    def default(self, o):
        # recommendation: always use double quotes with JSON

        pass


def band_json_to_py(lineup_json):
    """JSON decoder for Band objects (object_hook parameter in json.loads()).
    """


if __name__ == "__main__":

    # from testdata.musicians import *

    # class variables (like static fields in Java; typically defined and initialized before __init__())
    # object class (like the Object class in Java; all classes inherit from object
    #   try, e.g., list.__mro__ in the console)
    #   object class defines object.__eq__(self, other) etc.
    #   object.__ne__(self, other), the inverse of object.__eq__(self, other),
    #   is provided by Python automatically once object.__eq__(self, other) is implemented

    # Check the basic methods (__init__(), __str__(),...)
    print()

    # Check the alternative constructor 1 (@classmethod from_name_list(name_list))
    print()

    # Check the alternative constructor 2 (@classmethod from_band_str(band_str))
    print()

    # Check date validator (@staticmethod validate_date(date))
    print()

    # Check the iterator
    print()

    # Repeated attempt to run the iterator fails, because the iterator is exhausted

    # Demonstrate generators
    print()

    # Demonstrate generator expressions
    print()

    # Demonstrate JSON encoding/decoding of Band objects
    # Single object
    print()

    # List of objects
    print()


