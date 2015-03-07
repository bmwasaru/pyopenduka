import sys

import requests


class OpendukaClient(object):
    """Client for Open Duka's HTTP-based API"""

    def __init__(self, api_key=None):
        """Initialize the client with the provided api key"""
        if api_key:
            self.api_key = api_key

    # @staticmethod
    # def request_data(self, url):
    #     try:
    #         response = requests.get(url).json()
    #         print response
    #     except requests.exceptions.RequestException as e:
    #         print e
    #         sys, exit(1)

    def id(self, entity_id):
        url = 'http://www.openduka.org/index.php/api/entity?key={0}&id={1}'.format(self.api_key, entity_id)
        try:
            response = requests.get(url).json()
            print response
        except requests.exceptions.RequestException as e:
            print e
            sys, exit(1)

    def name(self, search_term):
        url = 'http://www.openduka.org/index.php/api/search?key={0}&term={1}'.format(self.api_key, search_term)
        try:
            response = requests.get(url).json()
            print response
        except requests.exceptions.RequestException as e:
            print e
            sys, exit(1)