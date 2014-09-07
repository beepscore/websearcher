#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
# from ..websearcher import arg_reader
# put tests above websearcher directory
from websearcher import arg_reader


class TestArgReader(unittest.TestCase):

    def setUp(self):
        pass

    def test_args_default(self):
        reader = arg_reader.ArgReader()
        args = reader.args()
        self.assertEqual(None, args.expression, '')
        self.assertEqual(None, args.uri_start, '')
        self.assertEqual('', args.uri_end, '')
        self.assertEqual(1, args.item_start, '')
        self.assertEqual(2, args.item_end, '')
        self.assertEqual("./search_results.txt", args.outfile, '')


if __name__ == "__main__":
    unittest.main()
