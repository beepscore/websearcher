#!/usr/bin/env python3

import requests


def response(url):
    """
    Request web page at url, return response
    Then caller can read response.status_code, response.text
    """
    # http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
    response = requests.get(url)
    # response = requests.post(url=url, data=body, headers={'Connection':'close'})
    # http://stackoverflow.com/questions/10115126/python-requests-close-http-connection?rq=1
    response.connection.close()

    return response
