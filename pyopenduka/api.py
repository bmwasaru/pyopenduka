import sys

import requests


def request_data(url):
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


def get_name(key, search_term):
    url = 'http://www.openduka.org/index.php/api/search?key={0}&term={1}'.format(key, search_term)
    request_data(url)


def get_id(key, entity_id):
    url = 'http://www.openduka.org/index.php/api/entity?key={0}&id={1}'.format(key, entity_id)
    request_data(url)


class WrongContent(requests.exceptions.RequestException):
    """The response has the wrong content."""