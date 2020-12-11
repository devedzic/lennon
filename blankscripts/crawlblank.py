"""Web crawling and scraping.
BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

import requests
from bs4 import BeautifulSoup

from util import utility

BASE_URL = 'https://www.imdb.com/'


def get_soup(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Creates Response object from HTTP GET request, using requests.get(<url string>, allow_redirects=False),
    and then uses the text field of the Response object and the 'html.parser' to create the BeautifulSoup object.
    """

    # Create Response object from HTTP GET request; assume that no redirection is allowed (allow_redirects=False)

    # Get text from the Response object, using <response>.text

    # Create and return the corresponding BeautifulSoup object from the response text; use 'html.parser'


def get_specific_page(start_url: str, page=1):
    """Returns a specific page from a Website where long lists of items are split in multiple pages.
    """


def get_next_soup(start_url: str, page=1):
    """Returns the BeautifulSoup object corresponding to a specific page
    in case there are multiple pages that list objects of interest.
    Parameters:
    - start_url: the starting page/url of a multi-page list of objects
    - page: the page number of a specific page of a multi-page list of objects
    """


def crawl(url: str, max_pages=1):
    """Web crawler that collects info about movies from IMDb,
    implemented as a Python generator that yields BeautifulSoup objects (get_next_soup()) from multi-page movie lists.
    Parameters: the url of the starting IMDb page and the max number of pages to crawl in case of multi-page lists.
    """


def get_4_digit_substring(a_string):
    """Returns the first 4-digit substring from a_string.
    It assumes that a_string contains a 4-digit substring representing a year.
    Useful when the year of a movie release on IMDb is represented like '(1988, part 2)', or '(video, 2002)'."""


def get_m_info(start_url: str, max_pages=1):
    """
    Returns structured information about movies from a multi-page IMDb movie list.
    :param start_url: the url of the starting page of a multi-page IMDb movie list
    :param max_pages: the max number of pages to crawl
    :return: a list of tuples of info-items about the movies from a multi-page IMDb movie list
    Creates and uses the following data:
    - h3_list - a list of all 'h3' tags from multiple IMDb pages
                (each 'h3' tag contains: movie title, year of release, and (relative) link to the movie's IMDb page)
    - poster_list - a list of all relevant 'div' tags from multiple IMDb pages
                    (each such a 'div' tag contains the link to the poster of the corresponding movie)
    - info_list - a list of 3-tuples of information about each movie from h3_list
    - poster_link_list - a list of links to the posters of the movies from poster_list
    - complete_list - a list of 4-tuples of information about each movie from h3_list and poster_list
    """


if __name__ == "__main__":

    # Getting started
    start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
                'mode=detail&page=1&sort=moviemeter,asc'

    # Create Response object from GET request, using requests.get(<url>, allow_redirects=False)
    print()

    # Get response text from Response object, using <response>.text
    print()

    # Get BeautifulSoup object from response text, using BeautifulSoup(<response text>, 'html.parser')
    print()

    # Save BeautifulSoup object to an HTML file,
    # using <Path-file-object>.write_text(str(<BeautifulSoup object>), encoding='utf-8', errors='replace')
    print()

    # Demonstrate <BeautifulSoup object>.find('<tag>'), <BeautifulSoup object>.find_all(<tag>),
    # <BeautifulSoup object>.find_all(<tag>, {'<tag_attr_name>': "<tag_attr_value>"});
    # use, e.g., 'h3' or 'div' as the tags in the examples
    print()

    # Demonstrate getting a 'subtag' for a tag (a bs4.element.Tag object), e.g. h3.find('<subtag>')
    print()

    # Demonstrate getting an attribute value for a tag (a bs4.element.Tag object),
    # e.g. h3.find('<subtag>'), filtered with <{'class': "<class name>"}>;
    # alternatively: h3.find('<tag>')['<attr>'], h3.find('<subtag>').get('<attribute>'),
    # h3.find('<subtag>').<attribute>,... (<attribute>: e.g. text)
    print()

    # Demonstrate shorthand notation (e.g., h3.find('<tag>').text is equivalent to h3.<tag>.text),
    # h3.<tag>.find_next_siblings() and h3.<tag>.string
    print()

    # Each bs4.element.ResultSet, bs4.element.Tag,... can be used to create another BeautifulSoup object,
    # using BeautifulSoup(str(<bs4.element object>), 'html.parser')
    print()

    # Demonstrate shorthand notation (e.g., h3.find('<tag>').text is equivalent to h3.<tag>.text (or .string),
    # h3.find('<tag>')['<attr>'] is equivalent to h3.<tag>.['<attr>'],...)
    print()

    # Get/Return all text from a bs4.element.Tag object, using <bs4.element.Tag object>.text
    print()

    # Demonstrate <tag>.find_next_siblings() (returns all <tag>'s siblings) and
    # <tag>.find_next_sibling() (returns just the first one)
    print()

    # Get/Return and remove a specific item from a bs4.element.ResultSet using <result set>.pop(<index>) (default: last)
    print()

    # Example: get all movie titles from an IMDb page
    print()

    # # Test get_soup()
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
    #             'mode=detail&page=1&sort=moviemeter,asc'
    print()

    # Test get_specific_page()
    print()

    # Test get_next_soup()
    print()

    # Test crawl()
    print()

    # Test get_m_info()
    print()


