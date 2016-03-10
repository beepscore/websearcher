#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import web_searcher


class TestWebSearcher(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        searcher = web_searcher.WebSearcher("@./websearcher_data/inputs/web_searcher_args.txt")
        self.assertIsNotNone(searcher)
        self.assertIsNotNone(searcher.arg_reader)
        self.assertEqual("app*", searcher.expression, '')

    def test_search_file_returns_none(self):
        actual = web_searcher.WebSearcher.search_file("not there",
                                                      "./websearcher_data/downloads",
                                                      "httpwww.beepscore.comhubcape")
        self.assertEqual(None, actual)

    def test_search_file_returns_file_name(self):
        actual = web_searcher.WebSearcher.search_file("Apps",
                                                      "./websearcher_data/downloads",
                                                      "httpwww.beepscore.comhubcape")
        self.assertEqual("httpwww.beepscore.comhubcape", actual)

    def test_search_file_is_case_sensitive(self):
        actual = web_searcher.WebSearcher.search_file("Apps",
                                                      "./websearcher_data/downloads",
                                                      "httpwww.beepscore.comhubcape")
        self.assertEqual("httpwww.beepscore.comhubcape", actual)

        actual = web_searcher.WebSearcher.search_file("apps",
                                                      "./websearcher_data/downloads",
                                                      "httpwww.beepscore.comhubcape")
        self.assertEqual(None, actual)

    def test_search_directory(self):
        actual = web_searcher.WebSearcher.search_directory("Apps",
                                                           "./websearcher_data/downloads")
        self.assertEqual(["httpwww.beepscore.comhubcape"], actual)

if __name__ == "__main__":
    unittest.main()
