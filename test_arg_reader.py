#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
#from ..websearcher import arg_reader
# put tests above websearcher directory
from websearcher import arg_reader

class TestArgReader(unittest.TestCase):

    def setUp(self):
        pass

    def test_args(self):
        reader = arg_reader.ArgReader()
        self.assertEqual(1, 1, '')

if __name__ == "__main__":
    unittest.main()
