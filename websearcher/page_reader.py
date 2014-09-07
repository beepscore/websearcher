#!/usr/bin/env python3

import requests

class PageReader():
    '''
    Requests a url and returns the response.
    '''

    def __init__(self):
        pass

    def response_status_code(self, url):
        '''
        Request web page at url, return response status code
        '''
        response = self.response(url)
        return response.status_code

    def response_text(self, url):
        '''
        Request web page at url, return response text
        '''
        response = self.response(url)
        return response.text

    def response(self, url):
        '''
        Request web page at url, return response
        '''
        response = None

        # http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
        response = requests.get(url)
        # response = requests.post(url=url, data=body, headers={'Connection':'close'})
        # http://stackoverflow.com/questions/10115126/python-requests-close-http-connection?rq=1
        response.connection.close()

        return response
