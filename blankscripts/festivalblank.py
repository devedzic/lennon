"""The class representing the concept of a festival.
"""

from datetime import date
import sys

from woodstock.music.performer import *
from woodstock.music.lineup import *
from woodstock.util.utility import *


class Festival:
    """The class describing the concept of a festival.
    It includes a name, a list of Lineup objects (lineups by date), location and the start and end dates.
    """


class FestivalError(Exception):
    """Base class for exceptions in this module.
    """

    pass


class FestivalStartDateException(FestivalError):
    """Exception raised when a the tart date of a festival lineup is not between start and end dates of the festival.
    """


def check_lineup_date(lineup, start_date, end_date):
    """Checks if lineup.date is between start_date and end_date."""


class LineupDateException(FestivalError):
    """Exception raised when a the date of a festival lineup is not between start and end dates of the festival.
    """


class FestivalEncoder(json.JSONEncoder):
    """JSON encoder for Festival objects.
    """

    def default(self, o):
        # recommendation: always use double quotes with JSON

        pass


def festival_json_to_py(festival_json):
    """JSON decoder for Festival objects (object_hook parameter in json.loads()).
    """


if __name__ == "__main__":

    pass

    # # Data
    #
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
    #
    # day1_performers = [melanie, arloGuthrie]
    # day1_lineup = Lineup(*day1_performers, date=date(1969, 8, 15))
    # day2_performers = [gratefulDead, jeffersonAirplane, theWho, ccr]
    # day2_lineup = Lineup(*day2_performers, date=date(1969, 8, 16))
    # day3_performers = [csny, jimiHendrix, theBand]
    # day3_lineup = Lineup(*day3_performers, date=date(1969, 8, 17))

    # Create a Festival object
    print()

    # Demonstrate exceptions
    # Here's the hierarchy of built-in exceptions: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

    # Demonstrate exceptions - the general structure of try-except statements, possibly including else and finally
    print()

    # Demonstrate exceptions - except: <exception> as <e> (and then type(<e>), <e>.__class__.__name__, <e>.args,...)
    print()

    # Demonstrate exceptions - user-defined exceptions (wrong festival date(s), wrong lineup date)
    print()

    # Demonstrate writing to a text file
    print()

    # Demonstrate reading from a text file
    print()

    # Demonstrate writing to a binary file - pickle.dump() and <f>.write()/<f>.writelines() with str.encode(<obj>)
    print()

    # Demonstrate reading from a binary file - pickle.load() and <f>.read().decode()/<f>.readlines().decode()
    print()

    # Demonstrate get_project_dir(), get_data_dir() and writing/reading to/from files in data dir
    print()

    # Demonstrate JSON encoding/decoding of Festival objects
    # Single object
    print()

    # List of objects
    print()



