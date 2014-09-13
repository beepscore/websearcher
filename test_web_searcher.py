#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import web_searcher
from websearcher import file_writer


class TestWebSearcher(unittest.TestCase):

    def setUp(self):
        pass

    def test_file_name_for_page_number(self):
        actual = web_searcher.WebSearcher.file_name_for_page_number("foo", 23, "bar.html")
        expected = "foo23bar.html"
        self.assertEqual(expected, actual)

    def test_url_for_page_number2(self):
        actual = web_searcher.WebSearcher.url_for_page_number("http://www.python-forum.org/viewforum.php?f=10&start=",
                                                                   2, "/foo.html")
        expected = "http://www.python-forum.org/viewforum.php?f=10&start=25/foo.html"
        self.assertEqual(expected, actual)

    def test_init(self):
        searcher = web_searcher.WebSearcher("@./test_args.txt")
        self.assertIsNotNone(searcher)
        self.assertIsNotNone(searcher.arg_reader)

    def test_request_page_write_response(self):
        searcher = web_searcher.WebSearcher("@./test_args.txt")
        searcher.request_page_write_response("http://www.python-forum.org/viewforum.php?f=10&start=2",
                                             "junk2.html")
        self.assertIsNotNone(searcher.arg_reader)

    def test_request_pages_write_responses(self):
        # searcher = web_searcher.WebSearcher("@../websearcher_args.txt")
        searcher = web_searcher.WebSearcher("@./test_args.txt")
        searcher.request_pages_write_responses()

    def test_search_file2(self):
        searcher = web_searcher.WebSearcher("@./test_args.txt")
        actual = web_searcher.WebSearcher.search_file("should", searcher.args.out_directory, "junk2.html")
        self.assertEqual(None, actual)

    def test_search_file3(self):
        searcher = web_searcher.WebSearcher("@./test_args.txt")
        actual = web_searcher.WebSearcher.search_file("should", searcher.args.out_directory, "junk3.html")
        self.assertEqual("junk3.html", actual)

    def test_search_directory(self):
        searcher = web_searcher.WebSearcher("@./test_args.txt")
        actual = web_searcher.WebSearcher.search_directory("should", searcher.args.out_directory)
        self.assertEqual(["junk3.html"], actual)


if __name__ == "__main__":
    unittest.main()
