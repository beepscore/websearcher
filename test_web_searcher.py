#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import web_searcher
#from websearcher import arg_reader


class TestWebSearcher(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        searcher = web_searcher.WebSearcher("@../websearcher_args.txt")
        self.assertIsNotNone(searcher)
        self.assertIsNotNone(searcher.arg_reader)

    def test_request_page_write_response(self):
        searcher = web_searcher.WebSearcher("@../websearcher_args.txt")
        searcher.request_page_write_response()
        self.assertIsNotNone(searcher.arg_reader)

if __name__ == "__main__":
    unittest.main()
