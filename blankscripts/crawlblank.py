"""Web crawling and scraping
"""

import requests
from bs4 import BeautifulSoup

from woodstock.util import utility

BASE_URL = 'https://www.imdb.com/'


def get_soup(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Creates Response object from HTTP GET request, using requests.get(<url string>, allow_redirects=False),
    and then uses the text field of the Response object and the 'html.parser' to create the BeautifulSoup object.
    """

    # Create Response object from HTTP GET request; assume that no redirection is allowed

    # Get text from the Response object

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

    # Test get_soup()
    start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
                'mode=detail&page=1&sort=moviemeter,asc'
    print()

    # Write BeautifulSoup info to an HTML file (using write_text(str(<soup>), encoding='utf-8', errors='replace')
    print()

    # Demonstrate <soup>.find_all('<tag_name>') for 'h3' - attribute h3.text
    print()

    # Demonstrate <soup>.find_all('<tag_name>') for 'div' (filter ResultSet with <{'class': "<class name>"}), 'h3',...
    print()

    # Demonstrate attribute h3.find('<subtag>'), h3.find('<subtag>').text, h3.find('<subtag>').get('<attribute>')
    print()

    # Demonstrate attribute h3.find('<subtag>'), filtered with <{'class': "<class name>"}
    print()

    # Demonstrate shorthand notation (e.g., h3.find('<tag>').text is equivalent to h3.<tag>.text),
    # h3.<tag>.find_next_siblings() and h3.<tag>.string
    print()

    # Test get_specific_page()
    print()

    # Test get_next_soup()
    print()

    # Test crawl()
    print()

    # Test get_m_info()
    print()


