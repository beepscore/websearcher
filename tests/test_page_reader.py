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
        actual = reader.spell_from_url("https://www.google.com/#q=astma")
        expected = "foo"
        self.assertEqual(expected, actual, '')

if __name__ == "__main__":
    unittest.main()
