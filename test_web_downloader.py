#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import web_downloader


class TestWebDownloader(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        downloader = web_downloader.WebDownloader("@./test_data/test_args.txt")
        self.assertIsNotNone(downloader)
        self.assertIsNotNone(downloader.arg_reader)

    def test_request_url_write_to_out_file(self):
        downloader = web_downloader.WebDownloader("@./test_data/test_args.txt")
        downloader.request_url_write_to_out_file("http://www.beepscore.com", "junk2.html")
        self.assertIsNotNone(downloader.arg_reader)

if __name__ == "__main__":
    unittest.main()
