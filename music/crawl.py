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
    response = requests.get(url, allow_redirects=False)

    # Get text from the Response object, using <response>.text
    response_text = response.text

    # Create and return the corresponding BeautifulSoup object from the response text; use 'html.parser'
    return BeautifulSoup(response_text, 'html.parser')


def get_specific_page(start_url: str, page=1):
    """Returns a specific page from a Website where long lists of items are split in multiple pages.
    """

    if '&page=' in start_url:
        url_chunks = start_url.split('&page=')
        # return url_chunks[0] + '&page=' + str(page)
        return url_chunks[0] + '&page=' + str(page) + '&' + url_chunks[1].split('&', maxsplit=1)[1]
    else:
        return start_url


def get_next_soup(start_url: str, page=1):
    """Returns the BeautifulSoup object corresponding to a specific page
    in case there are multiple pages that list objects of interest.
    Parameters:
    - start_url: the starting page/url of a multi-page list of objects
    - page: the page number of a specific page of a multi-page list of objects
    """

    return get_soup(get_specific_page(start_url, page))


def crawl(url: str, max_pages=1):
    """Web crawler that collects info about movies from IMDb,
    implemented as a Python generator that yields BeautifulSoup objects (get_next_soup()) from multi-page movie lists.
    Parameters: the url of the starting IMDb page and the max number of pages to crawl in case of multi-page lists.
    """

    for page in range(max_pages):
        yield get_next_soup(url, page + 1)
        page += 1


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

    h3_list = []
    poster_list = []
    next_soup = crawl(start_url, max_pages)
    while True:
        try:
            s = next(next_soup)
            h3_list.extend(s.find_all('h3')[:-1])
            poster_list.extend(s.find_all('div', {'class': "lister-item-image ribbonize"}))
        except StopIteration:
            break

    info_list = []
    for h3 in h3_list:
        title = h3.a.text
        year = h3.find('span', {'class': "lister-item-year text-muted unbold"}).text.split()[-1].lstrip('(').rstrip(')')
        link = BASE_URL + h3.a['href'].lstrip('/')
        info_list.append((title, year, link))

    poster_link_list = []
    for poster in poster_list:
        poster_link = poster.a.img['loadlate']
        poster_link_list.append(poster_link)

    complete_list = []
    for info, poster_link in zip(info_list, poster_link_list):
        title, year, link = info
        complete_list.append((title, year, link, poster_link))

    return complete_list


if __name__ == "__main__":

    # # Getting started
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
    #             'mode=detail&page=1&sort=moviemeter,asc'

    # # Create Response object from GET request, using requests.get(<url>, allow_redirects=False)
    # response = requests.get(start_url, allow_redirects=False)
    # # print(type(response))
    # # print(response)

    # # Get response text from Response object, using <response>.text
    # response_text = response.text
    # # print(type(response_text))
    # # print(response_text[:1000])
    # # print()

    # # Get BeautifulSoup object from response text, using BeautifulSoup(<response text>, 'html.parser')
    # soup = BeautifulSoup(response_text, 'html.parser')
    # # print(type(soup))
    # # print(soup)
    # print()

    # # Save BeautifulSoup object to file,
    # # using <Path-file-object>.write_text(str(<BeautifulSoup object>), encoding='utf-8', errors='replace')
    # soup_file = utility.get_data_dir() / 'soup.html'
    # soup_file.write_text(str(soup), encoding='utf-8', errors='replace')

    # # Test <BeautifulSoup object>.find('<tag>'), <BeautifulSoup object>.find_all(<tag>),
    # # <BeautifulSoup object>.find_all(<tag>, {'<tag_attr_name>': "<tag_attr_value>"})
    # # # print(soup.find('h3'))
    # # for h3 in soup.find_all('h3'):
    # #     print(h3)
    # # print()
    # # movie_items = soup.find_all('div', {'class': "lister-list"})
    # # print(type(movie_items))
    # # print(len(movie_items))
    # movie_items = soup.find_all('div', {'class': "lister-item mode-detail"})
    # print(type(movie_items))
    # # print(len(movie_items))
    # # print(movie_items)
    # # print()
    # # print()
    # # print()

    # print(type(movie_items[0]))
    # print(movie_items[0])

    # # Each bs4.element.ResultSet, bs4.element.Tag,... can be used to create another BeautifulSoup object,
    # # using BeautifulSoup(str(<bs4.element object>), 'html.parser')
    # movie_items_soup = BeautifulSoup(str(movie_items[0]), 'html.parser')
    # print(type(movie_items_soup))

    # # Get/Return and remove a specific item from a bs4.element.ResultSet using <result set>.pop(<index>) (default: last)
    # movie_items_h3 = soup.find_all('h3')
    # # # print(type(movie_items_h3))
    # # # print(movie_items_h3)
    # # print(len(movie_items_h3))
    # # # movie_items_h3.pop(50)
    # # item = movie_items_h3.pop(23)
    # # print(type(item))
    # # print()
    # # print(item)
    # # print()
    # #
    # # # Get/Return all text from a bs4.element.Tag object, using <bs4.element.Tag object>.text
    # # print(type(item.text))
    # # # print(item.text)
    # # print(item.text.strip())
    # # print()
    # # print(len(movie_items_h3))
    # # print()
    # # item_soup = BeautifulSoup(str(item), 'html.parser')
    # # print(type(item_soup))
    # # print(item_soup)
    # # # print(movie_items_h3)

    # # Get all movie titles from an IMDb page
    # movie_items_h3.pop()                # remove the last one; it is not a movie item
    # for h3 in movie_items_h3:
    #     # print(h3)
    #     # print(type(h3))
    #
    #     # print(h3.text)
    #
    #     # print(h3.text.split('.\n')[1])
    #     print(h3.text.split('.\n')[1].split('\n(')[0])
    print()

    # # Demonstrate shorthand notation (e.g., h3.find('<tag>').text is equivalent to h3.<tag>.text (or .string),
    # # h3.find('<tag>')['<attr>'] is equivalent to h3.<tag>.['<attr>'],...)
    # print(movie_items_h3[0])
    # print()
    # print(movie_items_h3[0].span)
    # print(movie_items_h3[0].span.text)
    # print(movie_items_h3[0].span.string)
    # print(movie_items_h3[0].span['class'])
    # print()
    # print(movie_items_h3[0].a)
    # print(movie_items_h3[0].a.text)
    # print(movie_items_h3[0].a.string)
    # print()

    # # Demonstrate <tag>.find_next_siblings() (returns all <tag>'s siblings) and
    # # <tag>.find_next_sibling() (returns just the first one)
    # print(movie_items_h3[0].find_next_siblings())
    # print()
    # print(movie_items_h3[0].find_next_siblings()[0])
    # print()
    # print(movie_items_h3[0].find_next_sibling())
    # print()
    # print(len(movie_items_h3[0].find_next_siblings()))
    # print(type(movie_items_h3[0].find_next_siblings()))
    # print(type(movie_items_h3[0].find_next_siblings()[0]))
    # print()

    # Test get_soup()
    start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
                'mode=detail&page=1&sort=moviemeter,asc'
    # soup = get_soup(start_url)
    # print(type(soup))
    # print(soup)
    # print()

    # # Test get_specific_page()
    # page = get_specific_page(start_url, 3)
    # print(page)
    # print()

    # # Test get_next_soup()
    # next_soup = crawl(start_url, 3)
    # while True:
    #     try:
    #         print(next(next_soup).find_all('h3')[:-1])      # [:-1] eliminates the 'Recently Viewed' item (not a movie)
    #         print()
    #         print()
    #     except StopIteration:
    #         break
    # print()
    #
    # # Test crawl()
    # print()
    #
    # Test get_m_info()
    movies = get_m_info(start_url, max_pages=3)
    for movie in movies:
        print(movie)
    print()



    # # Just testing
    # print(soup.find('h3'))
    # print()
    # print(type(soup.find('h3')))
    # print(soup.find('h3').find('span', {'class', "lister-item-year text-muted unbold"}).text.split()[-1].lstrip('(').rstrip(')'))
    # print()
    # h3_typical = soup.find_all('h3')[3]
    # print(h3_typical.find('span', {'class', "lister-item-year text-muted unbold"}).text.split()[-1].lstrip('(').rstrip(')'))

