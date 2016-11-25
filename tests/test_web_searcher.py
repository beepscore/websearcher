#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import web_searcher


class TestWebSearcher(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        searcher = web_searcher.WebSearcher()
        self.assertIsNotNone(searcher)

    def test_search_file_returns_none(self):
        actual = web_searcher.WebSearcher.search_file("not there",
                                                      "./data/downloads",
                                                      "httpwww.beepscore.comhubcape")
        self.assertEqual(None, actual)

    def test_search_file_returns_file_name(self):
        actual = web_searcher.WebSearcher.search_file("Apps",
                                                      "./data/downloads",
                                                      "httpwww.beepscore.comhubcape")
        self.assertEqual("httpwww.beepscore.comhubcape", actual)

    def test_search_file_is_case_sensitive(self):
        actual = web_searcher.WebSearcher.search_file("Apps",
                                                      "./data/downloads",
                                                      "httpwww.beepscore.comhubcape")
        self.assertEqual("httpwww.beepscore.comhubcape", actual)

        actual = web_searcher.WebSearcher.search_file("apps",
                                                      "./data/downloads",
                                                      "httpwww.beepscore.comhubcape")
        self.assertEqual(None, actual)

    def test_search_directory_Apps(self):
        actual = web_searcher.WebSearcher.search_directory("Apps",
                                                           "./data/downloads")
        self.assertEqual(["httpwww.beepscore.comhubcape"], actual)

    def test_search_directory_Python(self):
        actual = web_searcher.WebSearcher.search_directory("Python",
                                                           "./data/downloads")
        self.assertEqual(['httppython.org',
                          'httpsen.wikipedia.orgwikiPython_%28programming_language%29'], actual)

    def test_search_directory_data(self):
        actual = web_searcher.WebSearcher.search_directory("dat*",
                                                           "./data/downloads")
        self.assertEqual(['httppython.org',
                          'httpsen.wikipedia.orgwikiPython_%28programming_language%29',
                          'httpswww.google.com#q=python',
                          'httpwww.beepscore.comhubcape'], actual)

    def test_search_directory_write_results_data(self):
        web_searcher.WebSearcher.search_directory_write_results("dat*",
                                                                "./data/downloads",
                                                                "./data/results",
                                                                "websearcher_results.txt")

if __name__ == "__main__":
    unittest.main()
