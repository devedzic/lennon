"""The class representing the concept of a music group/band.
It includes a list of Musician objects (band members) and the date when the band started performing together.
"""

from datetime import date, datetime, time
import json

from music.musician import Musician, musician_json_to_py, musician_py_to_json
from settings import PREFERRED_DATE_FORMAT
from util.utility import date_json_to_py, date_py_to_json


class Band:
    """The class describing the concept of a music group/band.
    It includes a list of Musician objects (band members) and the date when the band started performing together.
    """

    # Class variables: like static fields in Java; typically defined and initialized before __init__()
    # Insert a class variable (static field), such as definition, date_pattern,...

    formed_phrase_approx = 'the band was formed in '
    formed_phrase_date = 'the band was formed on '
    formed_phrase_approx_still_together = 'the band has been formed in '
    formed_phrase_date_still_together = 'the band has been formed on '
    formed_phrase_unknown = 'It is unknown when the band has been formed.'
    split_phrase_approx = 'the band split up in '
    split_phrase_date = 'the band split up on '
    split_phrase_negative = 'the band is still together.'
    split_phrase_unknown = 'It is unknown if the band is still together.'
    expected_keywords = ['formed', 'split']

    def __init__(self, name, *members, formed=date.today(), split=date.today()):
        self.name = name
        self.members = members
        self.formed = formed
        self.split = split
        # self.__i = 0                                      # introduce and initialize iterator counter, self.__i

    # def __init__(self, name, *members, **kwargs):
    #     self.name = name
    #     self.members = members
    #     self.__dict__.update({k: v for k, v in kwargs.items() if k in Band.expected_keywords})
    #     pass                                            # introduce and initialize iterator counter, self.__i

    def __str__(self):
        tab = '\t'
        nl = '\n'
        name_str = self.name + nl
        members_str = f'{nl.join([tab + str(m) for m in self.members]) if self.members else "members unknown"}' + nl
        formed_str = \
            Band.formed_phrase_date.capitalize() + self.formed.strftime(PREFERRED_DATE_FORMAT) \
                if isinstance(self.formed, date) else \
            Band.formed_phrase_approx.capitalize() + str(self.formed) if isinstance(self.formed, int) else \
            Band.formed_phrase_unknown
        formed_str += '\n'
        split_str = \
            Band.split_phrase_date.capitalize() + self.split.strftime(PREFERRED_DATE_FORMAT) \
                if isinstance(self.split, date) else \
            Band.split_phrase_approx.capitalize() + str(self.split) if isinstance(self.split, int) else \
            Band.split_phrase_unknown
        # split_str += '\n'
        return name_str + members_str + formed_str + split_str
        pass

    def __eq__(self, other):
        return isinstance(other, Band) and self.name == other.name and self.members == other.members

    @staticmethod
    def parse_band_str(band_str):
        """Splits a band string in its typical segments
        """
        band_name, *member_strings, formed_and_split_up_strings = band_str.split('\n\t')

        # print(band_name, member_strings, formed_and_split_up_strings)
        # print(len(formed_and_split_up_strings))

        # print(formed_and_split_up_strings.split('\n'))

        last_member_string, formed_string, split_up_string = formed_and_split_up_strings.split('\n')
        # print(last_member_string, formed_string, split_up_string)
        member_strings.append(last_member_string)
        formed = int(formed_string[-4:]) if 'in' in formed_string else \
            datetime.strptime(formed_string[-12:], PREFERRED_DATE_FORMAT).date() if 'on' in formed_string else \
            'unknown'
        split_up = int(split_up_string[-4:]) if 'in' in split_up_string else \
            datetime.strptime(split_up_string[-12:], PREFERRED_DATE_FORMAT).date() if 'on' in split_up_string else \
            'unknown'

        return band_name, member_strings, formed, split_up

    # Alternative constructor 1
    @classmethod
    def from_band_str_year(cls, band_str):
        name, members, formed, split = Band.parse_band_str(band_str)
        return cls(name, *members, formed=formed, split=split)

    # Alternative constructor 2
    @classmethod
    def from_band_str_date(cls, band_str):
        name, members, formed, split = Band.parse_band_str(band_str)
        return cls(name, *members, formed=formed, split=split) if isinstance(formed, date) and \
                                                                  isinstance(split, date) and \
                                                                  Band.is_date_valid(formed) and \
                                                                  Band.is_date_valid(formed) else None

    @staticmethod
    def is_date_valid(d):
        """It is assumed that a band does not perform together since more than ~60 years ago.
        So, the valid date to denote the start of a band's career is between Jan 01, 1960, and today."""

        return date(1960, 1, 1) < d < date.today()

    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        if self.__i < len(self.members):
            next_m = self.members[self.__i]
            self.__i += 1
            return next_m
        else:
            raise StopIteration


def next_member(band):
    """Generator that shows members of a band, one at a time.
    """

    # i = 0
    # while i < len(band.members):
    #     yield band.members[i]
    #     i += 1

    for member in band.members:
        input('Next: ')
        yield member                # yield produces a generator object, on which we call the next() built-in function
        print('Yeah!')


class BandEncoder(json.JSONEncoder):
    """JSON encoder for Band objects (cls= parameter in json.dumps()).
    """

    def default(self, band):
        # recommendation: always use double quotes with JSON

        return band_py_to_json(band)


def band_py_to_json(band):
    """JSON encoder for Band objects (default= parameter in json.dumps()).
    """

    if isinstance(band, Band):
        d = band.__dict__.copy()
        d['members'] = json.dumps(band.members, default=musician_py_to_json)
        d['formed'] = date_py_to_json(band.formed)
        d['split'] = date_py_to_json(band.split)
        return {"__Band__": d}
    return {f"__{band.__class__.__name__}__": band.__dict__}
    # Alternatively:
    # else:
    #   raise TypeError(f'object of type {musician.__class__.__name__}')


def band_json_to_py(band_json):
    """JSON decoder for Band objects (object_hook= parameter in json.loads()).
    """

    if "__Band__" in band_json:
        b = Band('')
        b.__dict__ = band_json["__Band__"]
        # b.__dict__['members'] = tuple(json.loads(b.__dict__['members'], object_hook=musician_json_to_py))
        # b.__dict__['formed'] = date_json_to_py(b.__dict__['formed'])
        # b.__dict__['split'] = date_json_to_py(b.__dict__['split'])
        b.members = tuple(json.loads(b.members, object_hook=musician_json_to_py))   # compiler complains, but it works
        b.formed = date_json_to_py(b.formed)
        b.split = date_json_to_py(b.split)
        b._Band__i = 0
        return b
    return band_json


if __name__ == "__main__":

    from testdata.musicians import *

    # the_beatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
    #                    formed=1962, split=1970)
    # the_beatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
    #                    formed=date(1962, 8, 18), split=1970)
    the_beatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
                       formed=date(1962, 8, 18), split=date(1970, 4, 10))
    # the_beatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr], formed='', split='')
    print(the_beatles)

    # class variables (like static fields in Java; typically defined and initialized before __init__())
    # object class (like the Object class in Java; all classes inherit from object
    #   try, e.g., list.__mro__ in the console)
    #   object class defines object.__eq__(self, other) etc.
    #   object.__ne__(self, other), the inverse of object.__eq__(self, other),
    #   is provided by Python automatically once object.__eq__(self, other) is implemented

    # # Check the basic methods (__init__(), __str__(),...)
    # print()

    # # Check parse_band_str(<band_str>)
    # # print(the_beatles.parse_band_str(str(the_beatles)))
    # print(Band.parse_band_str(str(the_beatles)))
    # print()

    # # Check the alternative constructor 1 (@classmethod from_band_str_year(<band_str>))
    # beatles = Band.from_band_str_year(str(the_beatles))
    # print(beatles)
    # print()

    # # Check the alternative constructor 2 (@classmethod from_band_str_date(<band_str>))
    # beatles = Band.from_band_str_date(str(the_beatles))
    # print(beatles)
    # print()

    # # Check date validator (@staticmethod is_date_valid(<date>))
    # print()

    # # Check the iterator
    # # for _ in range(len(the_beatles.members)):
    # #     print(the_beatles.__next__())
    # # print()
    # i = iter(the_beatles)
    # for _ in range(len(the_beatles.members)):
    #     print(next(i))
    # print()

    # Repeated attempt to run the iterator fails, because the iterator is exhausted
    # print(the_beatles.__next__())

    # # Demonstrate generators
    # # print(next_member(the_beatles))
    # # print(list(next_member(the_beatles)))
    # member_generator = next_member(the_beatles)             # get the generator object from the generator function
    # print(member_generator)
    # # print(next(member_generator))                         # call the next() built-in function on the generator object
    # # print(next(member_generator))
    # # print(next(member_generator))
    # # print(next(member_generator))
    # # print(next(member_generator))
    # print(next_member(the_beatles))
    # member_generator = next_member(the_beatles)             # get the generator object from the generator function
    # while True:
    #     try:
    #         print(next(member_generator))
    #     except StopIteration:
    #         break
    # print()

    # # Demonstrate generator expressions
    # print(i**2 for i in range(4))
    # print(next(i**2 for i in range(4)))     # 0
    # print(next(i**2 for i in range(4)))     # 0 again, since the generator is initialized again
    # print()
    # e = (i**2 for i in range(4))
    # print(next(e))                          # 0
    # print(next(e))                          # 1
    # print(next(e))                          # 4
    # print(next(e))                          # 9
    # # print(next(e))                        # raises StopIteration

    # Demonstrate JSON encoding/decoding of Band objects
    # Single object
    the_beatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
                       formed=date(1962, 8, 18), split=date(1970, 4, 10))
    the_beatles_json = json.dumps(the_beatles, default=band_py_to_json, indent=4)
    print(the_beatles_json)
    print()
    the_beatles_py = json.loads(the_beatles_json, object_hook=band_json_to_py)
    print(the_beatles_py)
    print()

    # List of objects
    the_beatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
                       formed=date(1962, 8, 18), split=date(1970, 4, 10))
    pink_floyd = Band('Pink Floyd', rogerWaters, nickMason, rickWright, davidGilmour,
                      formed=date(1965, 2, 12), split=date(1995, 3, 14))
    bands_json = json.dumps([the_beatles, pink_floyd], default=band_py_to_json, indent=4)
    print(bands_json)
    print()


