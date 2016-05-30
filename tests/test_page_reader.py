#!/usr/bin/env python3

import unittest
import requests

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import page_reader


class TestPageReader(unittest.TestCase):

    def setUp(self):
        pass

    def test_response_status_code(self):
        reader = page_reader.PageReader()
        expected = requests.codes.ok
        response = reader.response("http://www.google.com")
        self.assertEqual(expected, response.status_code, '')

    def test_response_headers_content_type(self):
        reader = page_reader.PageReader()
        response = reader.response("http://www.google.com")
        self.assertEqual('text/html; charset=ISO-8859-1', response.headers['content-type'], '')

    def test_response_text(self):
        reader = page_reader.PageReader()
        response = reader.response("http://www.google.com")
        expected = "<!doctype html><html itemscope"
        self.assertEqual(expected, response.text[:30], '')

    def test_response_text_astma(self):
        reader = page_reader.PageReader()
        # google returns mix of html and javascript
        # could use google api instead (free use is limited, then pay)
        # could try something like dryscrape
        # https://github.com/niklasb/dryscrape
        # https://pypi.python.org/pypi/dryscrape/1.0
        # https://dryscrape.readthedocs.io/en/latest/
        # http://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python

##################
        # http://stackoverflow.com/questions/11804497/python-3-web-scraping-and-javascript-oh-my?rq=1
##################

        actual = reader.spell_from_url("https://www.google.com/#q=astma")
        # for now, use duckduckgo instead
        # actual = reader.spell_from_url("https://duckduckgo.com/?q=astma&t=ffnt&ia=about")
        # actual = reader.spell_from_url("https://duckduckgo.com/?q=astma")
        expected = "foo"
        self.assertEqual(expected, actual, '')

if __name__ == "__main__":
    unittest.main()
