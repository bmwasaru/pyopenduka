import sys

import requests


def request_data(url):
    try:
        response = requests.get(url).json()
    except requests.exceptions.RequestException as e:
        print e
        sys, exit(1)

    print response


def get_name(key, search_term):
    url = 'http://www.openduka.org/index.php/api/search?key={0}&term={1}'.format(key, search_term)
    request_data(url)


def get_id(key, entity_id):
    url = 'http://www.openduka.org/index.php/api/entity?key={0}&id={1}'.format(key, entity_id)
    request_data(url)
