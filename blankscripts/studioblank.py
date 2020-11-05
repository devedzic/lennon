"""The class representing the concept of a music/recording studio.
"""

from datetime import date
import sys

# from music.musician import *
# from music.band import *
# from util.utility import *
import json


class Studio:
    """The class describing the concept of a music/recording studio.
    It includes a name, a list of Band objects (bands recording in that studio over a certain period of time),
    location and the start and end dates for scheduled recording sessions.
    """


class StudioError(Exception):
    """Base class for exceptions in this module.
    """

    pass


class RecordingDateException(StudioError):
    """Exception raised when the start date of the recording sessions is not before the end date.
    """


def check_band_start_date(band, start_date, end_date):
    """Checks if the date when the band started performing together is between start_date and end_date."""


class BandStartDateException(StudioError):
    """Exception raised when a the date when a band started performing together is not between the start and end dates
    of the recording sessions.
    """


class StudioEncoder(json.JSONEncoder):
    """JSON encoder for Studio objects.
    """

    def default(self, o):
        # recommendation: always use double quotes with JSON

        pass


def studio_json_to_py(studio_json):
    """JSON decoder for Studio objects (object_hook parameter in json.loads()).
    """


if __name__ == "__main__":

    # from testdata.musicians import *

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



