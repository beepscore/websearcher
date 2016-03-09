#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import web_searcher
from websearcher import file_writer


class TestWebSearcher(unittest.TestCase):

    def setUp(self):
        pass

    def test_filename_from_url_root(self):
        actual = web_searcher.WebSearcher.filename_from_url("http://www.beepscore.com")
        expected = "httpwww.beepscore.com"
        self.assertEqual(expected, actual)

    def test_filename_from_url(self):
        actual = web_searcher.WebSearcher.filename_from_url("http://beepscore.com/hubcape/")
        expected = "httpbeepscore.comhubcape"
        self.assertEqual(expected, actual)

    def test_init(self):
        searcher = web_searcher.WebSearcher("@./test_args.txt")
        self.assertIsNotNone(searcher)
        self.assertIsNotNone(searcher.arg_reader)

    def test_request_page_write_response(self):
        searcher = web_searcher.WebSearcher("@./test_args.txt")
        searcher.request_page_write_response("http://www.beepscore.com", "junk2.html")
        self.assertIsNotNone(searcher.arg_reader)

#   def test_request_pages_write_responses(self):
#       # searcher = web_searcher.WebSearcher("@../websearcher_args.txt")
#       searcher = web_searcher.WebSearcher("@./test_args.txt")
#       searcher.request_pages_write_responses()

    def test_search_file_returns_none(self):
        searcher = web_searcher.WebSearcher("@./test_args.txt")
        actual = web_searcher.WebSearcher.search_file("not there", searcher.args.out_directory, "junk2.html")
        self.assertEqual(None, actual)

    def test_search_file_returns_file_name(self):
        searcher = web_searcher.WebSearcher("@./test_args.txt")
        actual = web_searcher.WebSearcher.search_file("apps", searcher.args.out_directory, "junk2.html")
        self.assertEqual("junk2.html", actual)

    def test_search_directory(self):
        searcher = web_searcher.WebSearcher("@./test_args.txt")
        actual = web_searcher.WebSearcher.search_directory("apps", searcher.args.out_directory)
        self.assertEqual(["junk2.html"], actual)

#   def test_request_pages_search_responses(self):
#       searcher = web_searcher.WebSearcher("@./test_args.txt")
#       actual = searcher.request_pages_search_responses()
#       self.assertEqual(["junk3.html"], actual)

if __name__ == "__main__":
    unittest.main()
