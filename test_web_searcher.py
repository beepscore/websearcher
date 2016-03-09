#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import web_searcher


class TestWebSearcher(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        searcher = web_searcher.WebSearcher("@./test_data/test_args.txt")
        self.assertIsNotNone(searcher)
        self.assertIsNotNone(searcher.arg_reader)

    def test_search_file_returns_none(self):
        searcher = web_searcher.WebSearcher("@./test_data/test_args.txt")
        actual = web_searcher.WebSearcher.search_file("not there", searcher.args.out_directory, "junk2.html")
        self.assertEqual(None, actual)

    def test_search_file_returns_file_name(self):
        searcher = web_searcher.WebSearcher("@./test_data/test_args.txt")
        actual = web_searcher.WebSearcher.search_file("apps", searcher.args.out_directory, "junk2.html")
        self.assertEqual("junk2.html", actual)

    def test_search_directory(self):
        searcher = web_searcher.WebSearcher("@./test_data/test_args.txt")
        actual = web_searcher.WebSearcher.search_directory("apps", searcher.args.out_directory)
        self.assertEqual(["junk2.html"], actual)

if __name__ == "__main__":
    unittest.main()
