#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import web_searcher


class TestWebSearcher(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        searcher = web_searcher.WebSearcher("@./test_args/web_searcher_args.txt")
        self.assertIsNotNone(searcher)
        self.assertIsNotNone(searcher.arg_reader)
        self.assertEqual("app*", searcher.expression, '')

    def test_search_file_returns_none(self):
        actual = web_searcher.WebSearcher.search_file("not there",
                                                      "./test_websearcher_downloaded_files",
                                                      "httpbeepscore.comhubcape")
        self.assertEqual(None, actual)

    def test_search_file_returns_file_name(self):
        actual = web_searcher.WebSearcher.search_file("Apps",
                                                      "./test_websearcher_downloaded_files",
                                                      "httpbeepscore.comhubcape")
        self.assertEqual("httpbeepscore.comhubcape", actual)

    def test_search_file_is_case_sensitive(self):
        actual = web_searcher.WebSearcher.search_file("Apps",
                                                      "./test_websearcher_downloaded_files",
                                                      "httpbeepscore.comhubcape")
        self.assertEqual("httpbeepscore.comhubcape", actual)

        actual = web_searcher.WebSearcher.search_file("apps",
                                                      "./test_websearcher_downloaded_files",
                                                      "httpbeepscore.comhubcape")
        self.assertEqual(None, actual)

    def test_search_directory(self):
        actual = web_searcher.WebSearcher.search_directory("Apps",
                                                           "./test_websearcher_downloaded_files")
        self.assertEqual(["httpbeepscore.comhubcape"], actual)

if __name__ == "__main__":
    unittest.main()
