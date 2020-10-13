"""The class representing the concept of lineup of a festival.
It includes a list of Performer objects and a show date for these performers.
"""

from datetime import date, datetime, time
import json

from woodstock.music.performer import Performer
from woodstock.util.utility import format_date


class Lineup():
    """The class describing the concept of lineup of a festival.
    It includes a list of Performer objects and a show date for these performers.
    """

    # Class variables: like static fields in Java; typically defined and initialized before __init__()
    # Insert a class variable (static field), such as definition, date_pattern,...

    def __init__(self, *performers, date=date.today()):
        pass                                            # introduce and initialize iterator counter, self.__i

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    # Alternative constructor 1
    @classmethod
    def from_name_list(cls, names, date=date.today()):
        pass

    # Alternative constructor 2
    @classmethod
    def from_lineup_str(cls, lineup_str):
        pass

    @staticmethod
    def is_date_valid(d):
        """The first rock festival, the KFRC Fantasy Fair and Magic Mountain Music Festival,
        had been held on June 10-11, 1967, at Mount Tamalpais in Marin County.
        So, the valid date for creating a lineup for a r'n'r festival is between June 10-11, 1967, and today."""

        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


def next_performer(lineup):
    """Generator that shows performers from a lineup, one at a time.
    """


class LineupEncoder(json.JSONEncoder):
    """JSON encoder for Lineup objects.
    """

    def default(self, o):
        # recommendation: always use double quotes with JSON

        pass


def lineup_json_to_py(lineup_json):
    """JSON decoder for Lineup objects (object_hook parameter in json.loads()).
    """


if __name__ == "__main__":

    pass

    # class variables (like static fields in Java; typically defined and initialized before __init__())
    # object class (like the Object class in Java; all classes inherit from object
    #   try, e.g., list.__mro__ in the console)
    #   object class defines object.__eq__(self, other) etc.
    #   object.__ne__(self, other), the inverse of object.__eq__(self, other),
    #   is provided by Python automatically once object.__eq__(self, other) is implemented

    # Data

    # # Some of the Woodstock performers, Aug 15-16, 1969
    # melanie = Performer('Melanie', is_band=False)
    # arloGuthrie = Performer('Arlo Guthrie', is_band=False)
    # # Some of the Woodstock performers, Aug 16-17, 1969
    # gratefulDead = Performer('Grateful Dead', is_band=True)
    # jeffersonAirplane = Performer('Jefferson Airplane', is_band=True)
    # theWho = Performer('The Who', is_band=True)
    # ccr = Performer('Creedence Clearwater Revival', is_band=True)
    # # Some of the Woodstock performers, Aug 17-18, 1969
    # csny = Performer('Crosby, Stills, Nash and Young', is_band=True)
    # jimiHendrix = Performer('Jimi Hendrix', is_band=False)
    # theBand = Performer('The Band', is_band=True)

    # Check the basic methods (__init__(), __str__(),...)
    print()

    # Check the alternative constructor 1 (@classmethod from_name_list(name_list))
    print()

    # Check the alternative constructor 2 (@classmethod from_lineup_str(lineup_str))
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

    # Demonstrate JSON encoding/decoding of Lineup objects
    # Single object
    print()

    # List of objects
    print()


