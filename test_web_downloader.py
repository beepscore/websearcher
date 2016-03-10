#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import web_downloader


class TestWebDownloader(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        downloader = web_downloader.WebDownloader("@./websearcher_data/inputs/web_downloader_args.txt")
        self.assertIsNotNone(downloader)
        self.assertIsNotNone(downloader.arg_reader)

    def test_urls_from_urls_file(self):
        downloader = web_downloader.WebDownloader("@./websearcher_data/inputs/web_downloader_args.txt")
        urls_list = downloader.urls_from_urls_file(downloader.urls_file)
        expected = ['http://python.org',
                    'http://www.beepscore.com/hubcape/',
                    'https://en.wikipedia.org/wiki/Python_%28programming_language%29',
                    'https://www.google.com/#q=python'
                    ]
        self.assertEqual(expected, urls_list)

    def test_request_url_write_to_out_file(self):
        downloader = web_downloader.WebDownloader("@./websearcher_data/inputs/web_downloader_args.txt")
        downloader.request_url_write_to_out_file("http://www.beepscore.com/hubcape/",
                                                 "httpwww.beepscore.comhubcape")
        self.assertIsNotNone(downloader.arg_reader)

    def test_request_urls_write_to_files(self):
        downloader = web_downloader.WebDownloader("@./websearcher_data/inputs/web_downloader_args.txt")
        downloader.request_urls_write_to_files()

if __name__ == "__main__":
    unittest.main()
