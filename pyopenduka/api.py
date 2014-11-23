import sys

import requests


def get(key, search_term):
    url = 'http://www.openduka.org/index.php/api/search?key={0}&term={1}'.format(key, search_term)
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print e
        sys, exit(1)

    try:
        data = response.json()
    except ValueError:
        raise WrongContent(response=response)

    print data


class WrongContent(requests.exceptions.RequestException):
    """The response has the wrong content."""