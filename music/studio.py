"""The class representing the concept of a music/recording studio.
"""

from datetime import date
import sys
from pathlib import Path
from pickle import dump, load

from music.musician import *
from music.band import *
from util.utility import *

import json


class Studio:
    """The class describing the concept of a music/recording studio.
    It includes the studio name, a list of Band objects (bands recording in that studio over a certain period of time),
    location and the start and end dates for the scheduled recording sessions.
    """

    def __init__(self, name, location, *bands, start_date=date(1962, 1, 1), end_date=date(1970, 12, 31)):
        if start_date > end_date:
            raise RecordingDateError(start_date, end_date)
        elif not all([band.formed < end_date for band in bands]):
            raise BandStartDateError(bands[[band.formed < end_date for band in bands].index(False)], end_date)
        else:
            self.name = name
            self.location = location
            self.start_date = start_date
            self.end_date = end_date
            self.bands = bands

    def __str__(self):
        studio = f'"{self.name}" studio, {self.location}'
        sessions = f'Recording sessions: {self.start_date} - {self.end_date}'
        bands = f'Bands: {", ".join([band.name for band in list(self.bands)])}'
        return f'{studio}\n{sessions}\n{bands}'

    def __eq__(self, other):
        return isinstance(other, Studio) and self.__dict__ == other.__dict__


class StudioError(Exception):
    """Base class for exceptions in this module.
    """

    pass


class RecordingDateError(StudioError):
    """Exception raised when the start date of the recording sessions is not before the end date.
    """

    def __init__(self, start_date, end_date):
        self.message = f'session start date ({start_date}) after session end date ({end_date}).'


def check_band_start_date(band, start_date, end_date):
    """Checks if the date when the band started performing together is between start_date and end_date.
    """

    return start_date < band.formed < end_date


class BandStartDateError(StudioError):
    """Exception raised when a the date when a band started performing together is
    after the end date of the recording sessions.
    """

    def __init__(self, band, end_date):
        self.message = f'band started performing together {band.formed}, ' \
                       f'after the end of the recording sessions ({end_date})'


class StudioEncoder(json.JSONEncoder):
    """JSON encoder for Studio objects (cls= parameter in json.dumps()).
    """

    def default(self, studio):
        # recommendation: always use double quotes with JSON

        return studio_py_to_json(studio)


def studio_py_to_json(studio):
    """JSON encoder for Studio objects (default= parameter in json.dumps()).
    """

    if isinstance(studio, Studio):
        d = studio.__dict__.copy()
        d['bands'] = json.dumps(studio.bands, default=band_py_to_json)
        d['start_date'] = date_py_to_json(studio.start_date)
        d['end_date'] = date_py_to_json(studio.end_date)
        return {"__Studio__": d}
    return {f"__{studio.__class__.__name__}__": studio.__dict__}
    # Alternatively:
    # else:
    #   raise TypeError(f'object of type {musician.__class__.__name__}')


def studio_json_to_py(studio_json):
    """JSON decoder for Studio objects (object_hook= parameter in json.loads()).
    """

    if "__Studio__" in studio_json:
        s = Studio('', '')
        s.__dict__.update(studio_json["__Studio__"])
        s.bands = tuple(json.loads(s.bands, object_hook=band_json_to_py))
        s.start_date = date_json_to_py(s.start_date)
        s.end_date = date_json_to_py(s.end_date)
        return s
    return studio_json


if __name__ == "__main__":

    from testdata.musicians import *

    # # Demonstrate exceptions
    # # Here's the hierarchy of built-in exceptions: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
    #
    # # Demonstrate exceptions - the general structure of try-except statements, possibly including else and finally
    # the_beatles = [johnLennon, paulMcCartney, georgeHarrison, ringoStarr]
    # try:
    #     # print(the_beatles[3])
    #     print(3/0)
    # except IndexError:
    #     print('Caught an IndexError!')
    # except:
    #     print('Caught an Exception!')
    # else:
    #     print('This is printed in the else clause - the try block has completed normally.')
    # finally:
    #     print('This is printed in the finally clause, '
    #           'regardless of whether the try block has completed normally or not.')
    # print()
    #
    # # Demonstrate exceptions - except: Exception as <e> (and then type(<e>), <e>.__class__.__name__, <e>.args,...)
    # try:
    #     print(the_beatles[4])
    # except Exception as e:
    #     print('Caught an Exception:', e)
    #     print('Caught an Exception:', type(e))
    #     print('Caught an Exception:', e.__class__.__name__)
    #     print('Caught an Exception:', e.args)
    # print()

    # # Demonstrate exceptions - user-defined exceptions (wrong recording date(s), wrong band start date)
    # the_beatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
    #                    formed=date(1962, 8, 18), split=date(1970, 4, 10))
    # pink_floyd = Band('Pink Floyd', rogerWaters, nickMason, rickWright, davidGilmour,
    #                   formed=date(1965, 2, 12), split=date(1995, 3, 14))
    #
    # # Create a Studio object
    # abbey_road = Studio('Abbey Road', 'London', *[the_beatles, pink_floyd],
    #                     start_date=date(1967, 1, 1), end_date=date(1967, 12, 31), )
    # print(abbey_road)
    # print()
    #
    # try:
    #     abbey_road = Studio('Abbey Road', 'London', *[the_beatles, pink_floyd],
    #                         start_date=date(1977, 1, 1), end_date=date(1977, 12, 31), )
    #     # print(3/0)
    # except BandStartDateError as e:
    #     # print(f'Caught a {e.__class__.__name__}: {e.message}')
    #     sys.stderr.write(f'Caught a {e.__class__.__name__}: {e.args[0]}\n')
    #     raise
    # except RecordingDateError as e:
    #     # print(f'Caught a {e.__class__.__name__}: {e.message}')
    #     sys.stderr.write(f'Caught a {e.__class__.__name__}: {e.args[0]}\n')
    #     # sys.stderr.write(f'Caught a {e.__class__.__name__}: {e.args[0], e.message}\n')
    #     raise
    # except Exception as e:
    #     # print(f'Caught a {e.__class__.__name__}: {e.args[0]}')
    #     sys.stderr.write(f'Caught a {e.__class__.__name__}: {e.args[0]}\n')
    #     raise
    # print()

    # # Demonstrate writing to a text file - <outfile>.write(), <outfile>.writelines()
    # the_beatles = [johnLennon, paulMcCartney, georgeHarrison, ringoStarr]
    # file = get_data_dir() / 'the_beatles.txt'
    # with open(file, 'w') as f:
    #     # for beatle in the_beatles:
    #     #     f.write(str(beatle) + '\n')
    #     f.writelines([str(beatle) + '\n' for beatle in the_beatles])
    # print()

    # # Demonstrate reading from a text file - <infile>.read(), <infile>.readline()
    # the_beatles = [johnLennon, paulMcCartney, georgeHarrison, ringoStarr]
    # file = get_data_dir() / 'the_beatles.txt'
    # the_beatles_members = []
    # with open(file, 'r') as f:
    #     # s = f.read()
    #     # print(s)
    #     while True:
    #         m = f.readline()
    #         if m:
    #             the_beatles_members.append(Musician.from_str(m))
    #         else:
    #             break
    #     for beatle in the_beatles_members:
    #         print(beatle)
    # print()

    # # Demonstrate writing to a binary file - pickle.dump() and <f>.write()/<f>.writelines() with str.encode(<obj>)
    # the_beatles = [johnLennon, paulMcCartney, georgeHarrison, ringoStarr]
    # file = get_data_dir() / 'the_beatles.bin'
    # # with open(file, 'wb') as f:
    # #     dump(the_beatles, f)
    # with open(file, 'wb') as f:
    #     f.writelines([str.encode(str(beatle) + '\n') for beatle in the_beatles])
    # print()

    # # # Demonstrate reading from a binary file - pickle.load() and <f>.read().decode()/<f>.readlines().decode()
    # the_beatles = [johnLennon, paulMcCartney, georgeHarrison, ringoStarr]
    # file = get_data_dir() / 'the_beatles.bin'
    # # with open(file, 'rb') as f:
    # #     loaded = load(f)
    # # print(loaded)
    # # for m in loaded:
    # #     print(m)
    # with open(file, 'rb') as f:
    #     loaded = f.read().decode()
    # print(loaded)
    # # print()

    # Demonstrate get_project_dir(), get_data_dir() and writing/reading to/from files in data dir
    print()

    # Demonstrate JSON encoding/decoding of Studio objects
    # Single object
    the_beatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
                       formed=date(1962, 8, 18), split=date(1970, 4, 10))
    pink_floyd = Band('Pink Floyd', rogerWaters, nickMason, rickWright, davidGilmour,
                      formed=date(1965, 2, 12), split=date(1995, 3, 14))
    abbey_road = Studio('Abbey Road', 'London', *[the_beatles, pink_floyd],
                        start_date=date(1967, 1, 1), end_date=date(1967, 12, 31), )
    abbey_road_json = json.dumps(abbey_road, default=studio_py_to_json, indent=4)
    print(abbey_road_json)
    abbey_road_py = json.loads(abbey_road_json, object_hook=studio_json_to_py)
    print()
    print(abbey_road)
    print(abbey_road_py)
    print()

    # # List of objects
    # the_beatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
    #                    formed=date(1962, 8, 18), split=date(1970, 4, 10))
    # pink_floyd = Band('Pink Floyd', rogerWaters, nickMason, rickWright, davidGilmour,
    #                   formed=date(1965, 2, 12), split=date(1995, 3, 14))
    # abbey_road_1 = Studio('Abbey Road', 'London', *[the_beatles, pink_floyd],
    #                     start_date=date(1967, 1, 1), end_date=date(1967, 12, 31), )
    # abbey_road_2 = Studio('Abbey Road', 'London', *[the_beatles, pink_floyd],
    #                     start_date=date(1967, 1, 1), end_date=date(1967, 12, 31), )
    # studios_json = json.dumps([abbey_road_1, abbey_road_2], default=studio_py_to_json, indent=4)
    # print(studios_json)
    # studios_py = json.loads(studios_json, object_hook=studio_json_to_py)
    # for studio in studios_py:
    #     print(studio, '\n')
    # print()

    # print(vars(the_beatles))



