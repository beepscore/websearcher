#!/usr/bin/env python3

import requests

class PageReader():
    '''
    Read a web page
    '''

    def __init__(self):
        pass

    def response_text(self, url):
        '''
        Read web page at url, return response text
        '''

        response = self.response(url)
        response_text = response.text
        return response_text

    def response(self, url):
        '''
        Read web page at url, return response
        '''
        response = None

        # http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
        response = requests.get(url)
        # response = requests.post(url=url, data=body, headers={'Connection':'close'})
        # http://stackoverflow.com/questions/10115126/python-requests-close-http-connection?rq=1
        response.connection.close()

        return response
