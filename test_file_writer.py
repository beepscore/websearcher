#!/usr/bin/env python3

import unittest
import os

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import file_writer


class TestFileWriter(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        test_path = "~/Desktop/junk"
        test_filename = "foo.html"
        test_content = "junk_text"
        writer = file_writer.FileWriter(test_path, test_filename, test_content)
        self.assertEqual(test_path, writer.path, '')
        self.assertEqual(test_filename, writer.filename, '')
        self.assertEqual(test_content, writer.content, '')

    def test_create_directory(self):
        # Note Python does not expand ~ in path as on OS X
        writer = file_writer.FileWriter("../junk", "foo.html", "junk_text")
        writer.create_directory(writer.path)
        self.assertTrue(os.path.isdir(writer.path), '')


if __name__ == "__main__":
    unittest.main()
