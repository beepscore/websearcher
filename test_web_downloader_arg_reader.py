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
        self.assertEqual(None, args.url, '')
        self.assertEqual("../websearcher_results", args.out_directory, '')
        self.assertEqual("results.txt", args.out_file, '')

    def test_args_from_argument(self):
        reader = web_downloader_arg_reader.WebDownloaderArgReader()

        test_url = "bar"
        test_out_directory = "../pages"
        test_out_file = "junk.txt"

        test_commandline = ["-url", test_url,
                            "-out_directory", test_out_directory,
                            "-out_file", test_out_file
                            ]
        args = reader.args(test_commandline)

        self.assertEqual(test_url, args.url, '')
        self.assertEqual(test_out_directory, args.out_directory, '')
        self.assertEqual(test_out_file, args.out_file, '')

    def test_args_from_argument_file(self):
        reader = web_downloader_arg_reader.WebDownloaderArgReader()

        # use fromfile_prefix_chars @ to read args from file
        args = reader.args(["@./test_data/web_downloader_args.txt"])

        self.assertEqual("http://www.beepscore.com", args.url)
        self.assertEqual("../websearcher_results", args.out_directory)
        self.assertEqual("websearcher_results_test.html", args.out_file)

if __name__ == "__main__":
    unittest.main()
