#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
# from ..websearcher import arg_reader
# put tests above websearcher directory
from websearcher import web_downloader_arg_reader


class TestWebDownloaderArgReader(unittest.TestCase):

    def setUp(self):
        pass

    def test_args_default(self):
        reader = web_downloader_arg_reader.WebDownloaderArgReader()
        args = reader.args(None)
        self.assertEqual("../data/input/urls.txt", args.urls_file, '')
        self.assertEqual("../data/downloads", args.out_directory, '')

    def test_args_from_argument(self):
        reader = web_downloader_arg_reader.WebDownloaderArgReader()

        urls_file = "my_urls.txt"
        out_directory = "../downloaded_pages"

        test_commandline = ["-urls_file", urls_file,
                            "-out_directory", out_directory,
                            ]
        args = reader.args(test_commandline)

        self.assertEqual(urls_file, args.urls_file, '')
        self.assertEqual(out_directory, args.out_directory, '')

    def test_args_from_argument_file(self):
        reader = web_downloader_arg_reader.WebDownloaderArgReader()

        # use fromfile_prefix_chars @ to read args from file
        args = reader.args(["@./data/input/web_downloader_args.txt"])

        self.assertEqual("./data/input/urls.txt", args.urls_file)
        self.assertEqual("./data/downloads", args.out_directory)


if __name__ == "__main__":
    unittest.main()
